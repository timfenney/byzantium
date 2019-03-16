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
from .keyboardraw import Keyboard

# fixme: keyboard is hardcoded
fp = open('/dev/hidraw0', 'rb')

def main():
    while True:
        buffer = fp.read(8)
        keeb = Keyboard(**{'raw': buffer})
        event = keeb.as_data()
        serialized = serialize(event)
        publish(serialized)
    
if __name__ == '__main__':
    main()
