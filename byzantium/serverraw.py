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
from .keyboardraw import Keyboard
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

def read_and_empty():
    with open(DEVICE, 'rb') as f:
        f.read(1)        


def main():
    pubsub.psubscribe(PATTERN)
    while True:
        for message in pubsub.listen():
            message_dict = deserialize(message['data'])
            print(message_dict)
            print('.')
            print('keyboard state:')
            keeb = Keyboard(**message_dict)
            print(str(keeb.as_data()))
            report = keeb.as_raw_event()
            write_default(report)
            read_and_empty()

            
if __name__ == '__main__':
    main()
