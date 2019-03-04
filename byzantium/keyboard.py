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

# This dict allows us to detect modifiers, so they can be handled differently in reports.
MODIFIERS = {
    29:  KEY_LEFTCTRL,
    56:  KEY_LEFTALT,
    125: KEY_LEFTMETA,
    42:  KEY_LEFTSHIFT,
    100: KEY_RIGHTALT,
    126: KEY_RIGHTMETA,
    54:  KEY_RIGHTSHIFT,
    97:  KEY_RIGHTCTRL
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
        if key in MODIFIERS:
            index = MODIFIERS[key]
            self.modifiers[index] = True
        else:
            if len(self.non_modifiers) < MAX_KEYS:
                self.non_modifiers.append(key)

    def key_up(self, key):
        '''Release the key. If it is a mod, clear the flag, otherwise remove the key.'''
        if key in MODIFIERS:
            index = MODIFIERS[key]
            self.modifiers[index] = False
        else:
            # This might raise, in the case that we have pressed more keys than MAX_KEYS.
            try:
                self.non_modifiers.remove(key)
            except:
                pass

class ReportFormatter(object):
    '''This class is responsibile for formatting StateMachine data for HID reports.'''
    def format_modifiers(self, modifiers):
        '''Format the modifiers as a bitmask. `modifiers` is an iterable of booleans.'''
        value = 0
        for i, flag in enumerate(modifiers):
            if flag:
                value += 2**i
        return value

    def format_non_modifiers(self, non_modifiers):
        '''Return the non-modifier keys formatted as a string of bytes up to, and padded to MAX_KEYS length.'''
        value = ''
        for key in non_modifiers:
            value += chr(key)
        padding = MAX_KEYS - len(non_modifiers)
        if padding > 0:
            for i in range(padding):
                value += chr(0)
        return value

    def format(self, state_machine):
        '''Return the formatted report.'''
        return (self.render_modifiers(state_machine.modifiers)
                + chr(0)
                + self.render_non_modifiers(state_machine.non_modifiers))

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
        self.report()

    def keyup(self, key):
        '''Dispatch to the state machine for changes, then report.'''
        self._state_machine.key_up(key)
        self.report()

    def _report(self):
        '''Dispatch the formatted report.'''
        report = self._formatter.format(self._state_machine)
        self._reporter.write(report)

def build_keyboard(device):
    '''This function will create the object graph, requiring only a device file such as `/dev/input/event3`.'''
    return Keyboard(state_machine=StateMachine(),
                    formatter=ReportFormatter(),
                    reporter=Reporter(device))
