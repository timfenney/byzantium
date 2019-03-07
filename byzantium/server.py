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
CODE = 'scancode'
DEVICE = '/dev/hidg0'
PATTERN = NAMESPACE + '-*'

def main():
    # keyboard = build_keyboard(DEVICE)
    keyboard = build_debug_keyboard(DEVICE)
    pubsub.psubscribe(PATTERN)

    while True:
        for message in pubsub.listen():
            message_dict = deserialize(message[DATA])
            key = message_dict[CODE]
            print 'message: ' + message[DATA]
            if message_dict[TYPE] == KEYDOWN:
                keyboard.keydown(key)
            elif message_dict[TYPE] == KEYUP:
                keyboard.keyup(key)
            elif message_dict[TYPE] == KEYHOLD:
                print 'holding!'

if __name__ == '__main__':
    main()
