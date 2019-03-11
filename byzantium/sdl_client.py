# -*- coding: utf-8 -*-
#
# This is the client code. Here `client` means the role that listens for
# keyboard events from a hardware keyboard and broadcasts them for the
# server (which replays them to another host).
# (fixme: rename client and server).

from . import events
from .connect import publish
from .serialize import serialize

import pdb
import sys
import sdl2
import sdl2.ext

def make_keypress(code, up):
    type_ = 'keyup' if up else 'keydown'
    return serialize({
        'type': type_,
        'keycode': code
    })

def emit(event):
    up = event.type == sdl2.SDL_KEYUP
    keypress = make_keypress(code=event.key.keysym.scancode, up=up)
    publish(keypress)

def main():
    # init
    sdl2.ext.init()
    window = sdl2.ext.Window("Hello, World!", size=(640, 480))
    window.show()

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            elif event.type == sdl2.SDL_KEYDOWN or event.type == sdl2.SDL_KEYUP:
                emit(event)
                    
        window.refresh()
    return 0


if __name__ == '__main__':
    main()
