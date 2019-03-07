# -*- coding: utf-8 -*-
#
# This is the client code. Here `client` means the role that listens for
# keyboard events from a hardware keyboard and broadcasts them for the
# server (which replays them to another host).
# (fixme: rename client and server).

from . import events
from .events import get_keyboard, listen
from .connect import publish

def main():
    # ensure we have a keyboard
    # get_keyboard()

    # fixme: don't hard-code the keyboard device file
    # while the hardware should be roughly the same with other pi owners,
    # one issue is keyboards often have internal hubs, and other usb devices connected.
    # The assignment of these paths is non-deterministic.
    keyboard="/dev/input/event3"
    listen(keyboard=keyboard, emit=publish)
    

if __name__ == '__main__':
    main()
