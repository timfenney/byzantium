# -*- coding: utf-8 -*-
#
# This is the client code. Here `client` means the role that listens for
# keyboard events from a hardware keyboard and broadcasts them for the
# server (which replays them to another host).
# (fixme: rename client and server).

from . import events
from .connect import publish
from .serialize import serialize
from .keyboard import BITS_FOR_MODIFIER_KEYCODES

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

def make_release_modifiers():
    return serialize({
        'type': 'release-modifiers'
    })

def make_release_nonmodifiers():
    return serialize({
        'type': 'release-nonmodifiers'
    })


def emit(event, modifiers, non_modifiers):
    up = event.type == sdl2.SDL_KEYUP
    key = event.key.keysym.scancode
    keypress = make_keypress(code=key, up=up)
    publish(keypress)
    if (!up):
        if key in BITS_FOR_MODIFIERS_KEYCODES:
            modifiers[key] = True
        else:
            non_modifiers[key] = True
    else:
        if key in BITS_FOR_MODIFIERS_KEYCODES:
            modifiers.pop(key, None)
            if not modifiers:
                release_modifiers()
        else:
            non_modifiers.pop(key, None)
            if not non_modifiers:
                release_nonmodifiers()
            

def release_modifiers():
    publish(make_release_modifiers())

def release_nonmodifiers():
    publish(make_release_nonmodifiers())

def main():
    # init
    sdl2.ext.init()
    window = sdl2.ext.Window("Hello, World!", size=(640, 480))
    window.show()

    modifiers = {}
    non_modifiers = {}

    running = True
    while running:
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                running = False
                break
            elif event.type == sdl2.SDL_KEYDOWN or event.type == sdl2.SDL_KEYUP:
                emit(event, modifiers, non_modifiers)
                    
        window.refresh()
    return 0


if __name__ == '__main__':
    main()
