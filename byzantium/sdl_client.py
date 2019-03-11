# -*- coding: utf-8 -*-
#
# This is the client code. Here `client` means the role that listens for
# keyboard events from a hardware keyboard and broadcasts them for the
# server (which replays them to another host).
# (fixme: rename client and server).

from . import events
from .connect import publish

import pdb
import sys
import sdl2hl

def make_keypress(code):
    return json.dumps({
        'type': 'keydown',
        'code': code
    })

def main():
    sdl2hl.init()
    window = sdl2hl.Window()
    renderer = sdl2hl.Renderer(window)
    avatar = sdl2hl.Rect(w=64, h=64)

    while True:
        for event in sdl2hl.events.poll():
            if event.type == sdl2hl.QUIT:
                sdl2hl.quit()
                sys.exit()
            elif event.type == sdl2hl.EventType.keydown:
                pdb.set_trace()
                message = make_keypress(code=1)
                publish(message)


if __name__ == '__main__':
    main()
