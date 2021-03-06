# -*- coding: utf-8 -*-
#
# This file contains the Keyboard state machine, used to reconstruct
# HID events
from . import connect
from .serialize import deserialize
from .events import KEYDOWN, KEYHOLD, KEYUP

# event keycodes for modifiers
from evdev.ecodes import ecodes

# bit posititions for modifiers in HID reports
# these are valid indexes for storage in a list;
# the positions are such that 2**CONSTANT will be
# the value of the flag for the HID report
# the constants are named as in:
# https://github.com/torvalds/linux/blob/master/include/uapi/linux/input-event-codes.h
KEY_LEFTCTRL   = 0
KEY_LEFTSHIFT  = 1
KEY_LEFTALT    = 2
KEY_LEFTMETA   = 3
KEY_RIGHTCTRL  = 4
KEY_RIGHTSHIFT = 5
KEY_RIGHTALT   = 6
KEY_RIGHTMETA  = 7
NUM_MODIFIERS  = 8

MAX_KEYS = 6 # no more than these can be pressed

# The keys are evdev modifier keycodes. The values are the bit positions above.
BITS_FOR_MODIFIER_KEYCODES = {
    'KEY_LEFTCTRL': KEY_LEFTCTRL,
    'KEY_LEFTCTRL': KEY_LEFTCTRL,
    'KEY_LEFTALT': KEY_LEFTALT,
    'KEY_LEFTMETA': KEY_LEFTMETA,
    'KEY_LEFTSHIFT': KEY_LEFTSHIFT,
    'KEY_RIGHTALT': KEY_RIGHTALT,
    'KEY_RIGHTMETA': KEY_RIGHTMETA,
    'KEY_RIGHTSHIFT': KEY_RIGHTSHIFT,
    'KEY_RIGHTCTRL': KEY_RIGHTCTRL
}

CODES_FOR_KEYCODES = {
    # abc's
    'KEY_A': 4,
    'KEY_B': 5,
    'KEY_C': 6,
    'KEY_D': 7,
    'KEY_E': 8,
    'KEY_F': 9,
    'KEY_G': 10,
    'KEY_H': 11,
    'KEY_I': 12,
    'KEY_J': 13,
    'KEY_K': 14,
    'KEY_L': 15,
    'KEY_M': 16,
    'KEY_N': 17,
    'KEY_O': 18,
    'KEY_P': 19,
    'KEY_Q': 20,
    'KEY_R': 21,
    'KEY_S': 22,
    'KEY_T': 23,
    'KEY_U': 24,
    'KEY_V': 25,
    'KEY_W': 26,
    'KEY_X': 27,
    'KEY_Y': 28,
    'KEY_Z': 29,

    # others
    'KEY_TAB':       43,
    'KEY_ENTER':     40,
    'KEY_UP':        82,
    'KEY_DOWN':      81,
    'KEY_LEFT':      80,
    'KEY_RIGHT':     79,
    'KEY_CAPSLOCK':  57,
    'KEY_BACKSPACE': 42,
    'KEY_1':         30,
    'KEY_2':         31,
    'KEY_3':         32,
    'KEY_4':         33,
    'KEY_5':         34,
    'KEY_6':         35,
    'KEY_7':         36,
    'KEY_8':         37,
    'KEY_9':         38,
    'KEY_0':         39,
    'KEY_GRAVE':     53,
    'KEY_VOLUMEUP':  128,
    'KEY_VOLUMEDOWN': 129,
    'KEY_MUTE':       127,
    'KEY_EQUAL':      46,
    'KEY_MINUS':      45,
    'KEY_NEXTSONG':  0xeb, # from https://source.android.com/devices/input/keyboard-devices#hid-keyboard-and-keypad-page-0x07
    'KEY_PLAYPAUSE': 0xe8, # from https://source.android.com/devices/input/keyboard-devices#hid-keyboard-and-keypad-page-0x07
    'KEY_PREVIOUSSONG': 0xea,
    'KEY_KBDILLUMUP': 23, # wtf?
    'KEY_KBDILLUMDOWN': 23, #wtf?
    'KEY_DASHBOARD': 23, # wtf?
    'KEY_SCALE': 23, #wtf?
    'KEY_BRIGHTNESSUP': 23, #wtf?
    'KEY_BRIGHTNESSDOWN': 23, #wtf?
    'KEY_ESC': 41,
    'KEY_FN': 23,
    'KEY_F1': 58,
    'KEY_F2': 59,
    'KEY_F3': 60,
    'KEY_F4': 61,
    'KEY_F5': 62,
    'KEY_F6': 63,
    'KEY_F7': 64,
    'KEY_F8': 65,
    'KEY_F9': 66,
    'KEY_F10': 67,
    'KEY_F11': 68,
    'KEY_F12': 69
}

class StateMachine(object):
    '''This is a state machine for producing HID keyboard reports. The protocol has
       inherent limitations, such as only 6 non-modifier keys may be pressed at a time.
       Additional keys are thrown away; we could switch to LRU or something if necessary.'''
    
    def __init__(self):
        '''Set attributes for modelling the state.'''
        self.modifiers = [False] * NUM_MODIFIERS
        self.non_modifiers = []

    def key_down(self, key):
        '''Press the key. If it is a mod, set the flag, otherwise add the key if it fits.'''
        self._key_up_down(key, up=False)

    def key_up(self, key):
        '''Release the key. If it is a mod, clear the flag, otherwise remove the key.'''
        self._key_up_down(key, up=True)

    def release_nonmodifiers(self):
        self._non_modifiers = []

    def release_modifiers(self):
        self._modifiers = [False] * NUM_MODIFIERS

    def _key_up_down(self, key, up):
        '''Press or release the key, based on up argument.'''

        if key in BITS_FOR_MODIFIER_KEYCODES:
            index = self._index(key)
            self.modifiers[index] = not up

        else:
            if up:
                # catch in case the key isn't in the list
                try:
                    self.non_modifiers.remove(key)
                except ValueError:
                    pass

            elif len(self.non_modifiers) < MAX_KEYS:
                self.non_modifiers.append(key)
                    
    def _index(self, key):
        index = BITS_FOR_MODIFIER_KEYCODES[key]
        return index

class PassThroughTranslator(object):
    '''Pass keycodes through untranslated.'''
    def translate(self, keycode):
        return keycode
    
class Translator(object):
    def translate(self, keycode):
        '''Translate the evdev keycode, e.g. 'KEY_A', into a USB report code, e.g. 0x04.
           Cf. https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf,
           specifically sections 0x07 Keyboard/Keypad Page, and 0x0c, Consumer Page.'''
        return CODES_FOR_KEYCODES[keycode]

class ReportFormatter(object):
    '''This class is responsibile for formatting StateMachine data for HID reports.'''
    def format_modifiers(self, modifiers):
        '''Format the modifiers as a bitmask. `modifiers` is an iterable of booleans.'''
        value = 0
        for i, flag in enumerate(modifiers):
            if flag:
                value += 2**i
        return chr(value)

    def format_non_modifiers(self, non_modifiers):
        '''Return the non-modifier keys formatted as a string of bytes up to, and padded to MAX_KEYS length.'''
        value = ''
        excepted = 0
        for key in non_modifiers:
            try:
                value += chr(key)
            except:
                excepted += 1

        padding = MAX_KEYS - len(non_modifiers) + excepted
        if padding > 0:
            for i in range(padding):
                value += chr(0)
        return value

    def format(self, state_machine):
        '''Return the formatted report.'''
        return (self.format_modifiers(state_machine.modifiers)
                + chr(0)
                + self.format_non_modifiers(state_machine.non_modifiers))

class DebugFormatter(object):
    def format(self, state_machine):
        return {
            'modifiers': state_machine.modifiers,
            'non_modifiers': state_machine.non_modifiers
        }
    
class Reporter(object):
    '''This is responsible only for writing the report to the relevant device file.
       The write needs to be flushed immediately. Also, the file may be opened for
       reading, to detect events from the host, such as LED state changes.'''
    def __init__(self, device):
        '''Set attributes for collaborators.'''
        self._device = device

    def write(self, report):
        '''Write the report to the device file.'''
        with open(self._device, 'wb') as f:
            f.write(report)

class PrintReporter(object):
    '''Just for debugging :-)'''
    def write(self, report):
        print report
            
class Keyboard(object):
    '''This is a keyboard which is controlled programatically, and which writes HID reports.'''
    def __init__(self, state_machine, formatter, reporter):
        '''Set attributes for collaborators.'''
        self._state_machine = state_machine
        self._formatter = formatter
        self._reporter = reporter
        
    def keydown(self, key):
        '''Dispatch to the state machine for changes, then report.'''
        self._state_machine.key_down(key)
        self._report()

    def keyup(self, key):
        '''Dispatch to the state machine for changes, then report.'''
        self._state_machine.key_up(key)
        self._report()

    def hold(self, key):
        pass

    def _report(self):
        '''Dispatch the formatted report.'''
        report = self._formatter.format(self._state_machine)
        self._reporter.write(report)

    def release_nonmodifiers(self):
        self._state_machine.release_nonmodifiers()

    def release_modifiers(self):
        self._state_machine.release_modifiers()

def build_debug_keyboard(device=None):
    '''This function will create the object graph. For compatibility it takes an unused device file argument.'''
    return Keyboard(state_machine=StateMachine(),
                    formatter=DebugFormatter(),
                    reporter=PrintReporter())

def build_keyboard(device):
    '''This function will create the object graph, requiring only a device file such as `/dev/input/event3`.'''
    return Keyboard(state_machine=StateMachine(),
                    formatter=ReportFormatter(),
                    reporter=Reporter(device))
