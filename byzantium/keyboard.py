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
LEFT_CONTROL  =   1
LEFT_SHIFT    =   2
LEFT_ALT      =   4
LEFT_META     =   8
RIGHT_CONTROL =  16
RIGHT_SHIFT   =  32
RIGHT_ALT     =  64
RIGHT_META    = 128

BIT_FOR_EVENT_MODIFIER = {
}

MAX_KEYS = 6 # no more than these can be pressed
NO_KEY = -1 # sentinel value

class KeyBoard(object):
    def __init__(self):
        self.modifiers_bitmask = 0
        self.non_modifiers = []
        
    def keydown(self, key):
        if not is_modifier(key):
            current_keys = len(self.non_modifiers)
            if current_keys < MAX_KEYS:
                self.non_modifiers.append(key)
            else:
                self.non_modifiers[0] = key
        else:
            if not key in BIT_FOR_EVENT_MODIFIER:
                print 'arrgghh, key not found: ' + key
                raise Exception
            else:
                bit = BIT_FOR_EVENT_MODIFIER[key]
                self.modifiers_bitmask |= bit # set bit
                
    def keyup(self, key):
        if not is_modifier(key):
            try:
                self.non_modifiers.remove(key)
            except:
                pass
        else:
            if not key in BIT_FOR_EVENT_MODIFIER:
                print 'arrgghh, key not found: ' + key
                raise Exception
            else:
                bit = BIT_FOR_EVENT_MODIFIER[key]
                mask = ~bit
                self.modifiers_bitmask &= mask

    # fixme: have to do something like comment below, also see
    # the url: https://www.rmedgar.com/blog/using-rpi-zero-as-keyboard-send-reports
    def report(self):
        pass
        # return chr(self.modifiers_bitmask) + chr(0) + chr(0)*5
