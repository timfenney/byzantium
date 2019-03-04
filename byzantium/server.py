# -*- coding: utf-8 -*-
#
# This file is a placeholder for the server logic
from . import connect
from .serialize import deserialize
from .events import KEYDOWN, KEYHOLD, KEYUP

DATA = 'data'
TYPE = 'type'
NULL_CHAR = chr(0)
CODE = 'scancode'

# fixme: redis details leaking into server.py
p = connection().pubsub(ignore_subscribe_messages=True)
p.subscribe()

device = open('/dev/hidg0', 'w')

def write_report(code):
    report = NULL_CHAR * 2 + chr(code) + NULL_CHAR * 5
    device.write(report)
    device.flush()

def main():
    for message in p.listen():
        message_dict = deserialize(message[DATA])
        if message_obj[TYPE] == KEYDOWN:
            key = message_obj[CODE]
            write_report(key)
        elif message_obj[TYPE] == KEYUP:
            # fixme: need states to hold mods
            write_report(0)
        elif message_obj[TYPE] == KEYHOLD:
            print 'holding!'

if __name__ == '__main__':
    main()
