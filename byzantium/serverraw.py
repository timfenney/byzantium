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

# fixme, get rid of client code in server
#fp = open('/dev/hidraw', 'rb')

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
        
        elif 'state' in kwargs:
            state = kwargs['state']
            self._mods = state['_mods'] + []
            self._norms = state['_norms'] + []

    def as_data(self):
        return {
            'type': 'RawBootHIDKeyboard',
            'state': {
                '_mods': self._mods,
                '_norms': self._norms
            }
        }
    
    def as_raw_event(self):
        report = []
        mods = 0
        for i, mod in enumerate(MODIFIERS):
            if self._mods[i]:
                mods += mod
        
        report.append(chr(mods))
        report.append(chr(0)) # unused
        for norm in self._norms:
            report.append(chr(norm))
        
        str_report = report[0]
        for r in report[1:]:
            str_report += r

        str_report = ''.join(report)
        return str_report  # fixme : .encode() ? -> looks like no for python 2.x .

    @classmethod
    def from_data(cls, **kwargs):
        return cls(**kwargs['state'])

from .connect import pubsub, NAMESPACE
from .serialize import deserialize

DEVICE = '/dev/hidg0'
PATTERN = NAMESPACE + '-*'

def write(device, report):
    '''Write the report to the device file.'''
    with open(DEVICE, 'wb') as f:
        f.write(report)

def write_default(report):
    '''Write the report to the default device.'''
    write(DEVICE, report)

def main():
    pubsub.psubscribe(PATTERN)
    while True:
        for message in pubsub.listen():
            message_dict = deserialize(message['data'])
            print(message_dict)
            print('.')
            print('keyboard state:')
            keeb = RawBootHIDKeyboard(**message_dict)
            print(str(keeb.as_data()))
            report = keeb.as_raw_event()
            write_default(report)

            
if __name__ == '__main__':
    main()
