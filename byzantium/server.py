# -*- coding: utf-8 -*-
#
# This file is a placeholder for the server logic
import time
from .connect import pubsub, NAMESPACE
from .serialize import deserialize
from .events import KEYDOWN, KEYHOLD, KEYUP
from .keyboard import build_keyboard, build_debug_keyboard

DATA = 'data'
TYPE = 'type'
NULL_CHAR = chr(0)
CODE = 'keycode'
DEVICE = '/dev/hidg0'
PATTERN = NAMESPACE + '-*'
RELEASE_MODIFIERS = 'release-modifiers'
RELEASE_NONMODIFIERS = 'release-nonmodifiers'

def main():
    keyboard = build_keyboard(DEVICE)
    # keyboard = build_debug_keyboard(DEVICE)
    pubsub.psubscribe(PATTERN)

    while True:
        for message in pubsub.listen():
            message_dict = deserialize(message[DATA])
            print message_dict
            key = message_dict[CODE]

            try:
                if message_dict[TYPE] == KEYDOWN:
                    keyboard.keydown(key)
                elif message_dict[TYPE] == KEYUP:
                    keyboard.keyup(key)
                elif message_dict[TYPE] == KEYHOLD:
                    keyboard.hold(key)
                elif message_dict[TYPE] == RELEASE_MODIFIERS:
                    keyboard.release_modifiers()
                elif message_dict[TYPE] == RELEASE_NONMODIFIERS:
                    keyboard.release_nonmodifiers()
            except KeyError as e:
                print e


if __name__ == '__main__':
    main()
