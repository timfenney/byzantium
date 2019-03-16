# -*- coding: utf-8 -*-
#
# This is the client code. Here `client` means the role that listens for
# keyboard events from a hardware keyboard and broadcasts them for the
# server (which replays them to another host).
# (fixme: rename client and server).

# from . import events
from .connect import publish
from .serialize import serialize
import sys
import json

fp = open('/dev/hidraw', 'rb')

HID_LEFTCTRL   = 0x01
HID_LEFTSHIFT  = 0x02
HID_LEFTALT    = 0x04
HID_LEFTMETA   = 0x08
HID_RIGHTMETA  = 0x10
HID_RIGHTALT   = 0x20
HID_RIGHTSHIFT = 0x40
HID_RIGHTCTRL  = 0x80

# largest to smallest to smallest
MODIFIERS = [
    HID_RIGHTCTRL,
    HID_RIGHTSHIFT,
    HID_RIGHTALT,
    HID_RIGHTMETA,
    HID_LEFTMETA,
    HID_LEFTALT,
    HID_LEFTSHIFT,    
    HID_LEFTCTRL
]

MODIFIERS_INDICES = {
    HID_LEFTCTRL: 0,
    HID_LEFTSHIFT: 1,
    HID_LEFTALT: 2,
    HID_LEFTMETA: 3,
    HID_RIGHTMETA: 4,
    HID_RIGHTALT: 5,
    HID_RIGHTSHIFT: 6,
    HID_RIGHTCTRL: 7
}

MOD_NAMES = {
    HID_LEFTCTRL: 'HID_LEFTCTRL',
    HID_LEFTSHIFT: 'HID_LEFTSHIFT',
    HID_LEFTALT: 'HID_LEFTALT',
    HID_LEFTMETA: 'HID_LEFTMETA',
    HID_RIGHTMETA: 'HID_RIGHTMETA',
    HID_RIGHTALT: 'HID_RIGHTALT',
    HID_RIGHTSHIFT: 'HID_RIGHTSHIFT',
    HID_RIGHTCTRL: 'HID_RIGHTCTRL'
}

class RawBootHIDKeyboard(object):
    def __init__(self, **kwargs):
        super(RawBootHIDKeyboard, self)
        self._mods = [False] * len(MODIFIERS)
        self._norms = []

        if 'raw' in kwargs:
            raw = kwargs['raw']
            modifiers = ord(raw[0])
            for mod in MODIFIERS:
                if mod <= modifiers:
                    index = MODIFIERS_INDICES[mod]
                    self._mods[index] = True
                    modifiers -= mod
            
            for byte in raw[2:]:
                val = ord(byte)
                if val > 0:
                    self._norms.append(val)

    def as_data(self):
        return {
            'type': 'RawBootHIDKeyboard',
            'state': {
                '_mods': self._mods,
                '_norms': self._norms
            }
        }
    
    @classmethod
    def from_data(cls, **kwargs):
        return cls(**kwargs['state'])


def main():
    while True:
        buffer = fp.read(8)
        keeb = RawBootHIDKeyboard(**{'raw': buffer})
        event = keeb.as_data()
        serialized = serialize(event)
        publish(serialized)
    

if __name__ == '__main__':
    main()
