# -*- coding: utf-8 -*-
#
# This file provides the abstraction between detected/generated events and
# data passed around the system.

from evdev import InputDevice, categorize, ecodes
import os
from os import listdir
from os.path import isdir, join
import re
import time
import sys
from connect import get_device, set_device

INPUT_PATH = '/dev/input/'
KEYUP = 'keyup'
KEYDOWN = 'keydown'
KEYHOLD = 'keyhold'

def device_path(name):
    join(INPUT_PATH, name)

def millis():
    return int(round(time.time() * 1000))

def ismouse(device_str):
    return re.findall(r'mouse|mice', device_str)

def devices():
    result = []
    for item in listdir(INPUT_PATH):
        if not isdir(device_path(item)) and not ismouse(item):
            result.append(item)

def detect_device(candidates):
    for counter, candidate in enumerate(candidates):
        print 'checking result for ' + candidate + ' ...'
        filename = device_path
        device = InputDevice(filename)
        last_millis = millis()
        while millis() - last_millis < 3000:
            active = device.active_keys(verbose=True)
            if len(active) > 0:
                print 'found keyboard!'
                print active
                return candidate
        print 'result not found for ' + candidate + ' ...'

def detect_keyboard():
    candidates = devices()
    candidate = detect_device(candidates)
    device = InputDevice(device_path(candidate))
    return device

def get_keyboard():
    keyboard_device = get_device()
    if keyboard_device:
        keyboard = InputDevice(keyboard_device)
    else:
        print 'not keyboard: ' + keyboard
        keyboard = detect_keyboard
    return keyboard

def event_type(key_event):
    keystate = key_event.keystate
    if keystate == KeyEvent.key_up:
        event_type = KEYUP
    elif keystate == KeyEvent.key_down:
        event_type = KEYDOWN
    elif keystate == KeyEvent.key_hold:
        event_type = KEYHOLD
    return keystate

def event_to_dict(event):
    return {
        'sec': event.sec,
        'type': event.type,
        'code': event.code,
        'value': event.value
    }

def key_event_to_dict(event):
    return {
        'type': event_type(key_event),
        'keycode': key_event.keycode,
        'keystate': key_event,
        'scancode': key_event.scandcode,
        'event': event_to_dict(key_event.event)
    }

def raw_event_to_dict(event):
    key_event = KeyEvent(event)
    return key_event_to_dict(key_event)

def listen(emit, keyboard=None):
    if not keyboard:
        keyboard = get_keyboard()
    device = InputDevice(device_path(keyboard))
    for event in device.read_loop():
        if event.type == ecodes.EV_KEY:
            emit(raw_event_to_dict(event))
