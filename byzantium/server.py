# -*- coding: utf-8 -*-
#
# This file is a placeholder for the server logic
from .connect import connection
from .serialize import deserialize
from .events import KEYDOWN, KEYHOLD, KEYUP
from .keyboard import build_keyboard

DATA = 'data'
TYPE = 'type'
NULL_CHAR = chr(0)
CODE = 'scancode'
DEVICE = '/dev/hidg0'

def main():
    # fixme: redis details leaking into server.py
    p = connection().pubsub(ignore_subscribe_messages=True)
    p.subscribe()

    keyboard = build_keyboard(DEVICE)

    while True:
        for message in p.listen():
            message_dict = deserialize(message[DATA])
            key = message_obj[CODE]
            if message_obj[TYPE] == KEYDOWN:
                keyboard.keydown(key)
            elif message_obj[TYPE] == KEYUP:
                keyboard.keyup(key)
            elif message_obj[TYPE] == KEYHOLD:
                print 'holding!'

if __name__ == '__main__':
    main()
