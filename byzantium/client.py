# -*- coding: utf-8 -*-
#
# This file has the core functionality.
from . import events
from .events import get_keyboard, listen
from .connect import publish

def main():
    # ensure we have a keyboard
    # get_keyboard()
    keyboard="/dev/input/event3"
    listen(keyboard=keyboard, emit=publish)
    

if __name__ == '__main__':
    main()
