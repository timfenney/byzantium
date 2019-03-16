import sys

fp = open('/dev/hidraw1', 'rb')

HID_LEFTCTRL   = 0x01
HID_LEFTSHIFT  = 0x02
HID_LEFTALT    = 0x04
HID_LEFTMETA   = 0x08
HID_RIGHTMETA  = 0x10
HID_RIGHTALT   = 0x20
HID_RIGHTSHIFT = 0x40
HID_RIGHTCTRL  = 0x80

# largest to smallest to smallest
MODIFIERS = [
    HID_RIGHTCTRL,
    HID_RIGHTSHIFT,
    HID_RIGHTALT,
    HID_RIGHTMETA,
    HID_LEFTMETA,
    HID_LEFTALT,
    HID_LEFTSHIFT,    
    HID_LEFTCTRL
]

MOD_NAMES = {
    HID_LEFTCTRL: 'HID_LEFTCTRL',
    HID_LEFTSHIFT: 'HID_LEFTSHIFT',
    HID_LEFTALT: 'HID_LEFTALT',
    HID_LEFTMETA: 'HID_LEFTMETA',
    HID_RIGHTMETA: 'HID_RIGHTMETA',
    HID_RIGHTALT: 'HID_RIGHTALT',
    HID_RIGHTSHIFT: 'HID_RIGHTSHIFT',
    HID_RIGHTCTRL: 'HID_RIGHTCTRL'
}

while True:
    print "~~~~~~~~~~~~~~~~~~~~~~:keyboard event:~~~~~~~~~~~~~~~~~~~~~~"
    print "~~~~~~~~~~~~~~~~~~~~~~:modifiers:~~~~~~~~~~~~~~~~~~~~~~"
    buffer = fp.read(8)
    modifiers = ord(buffer[0])
    print 'modifiers = ' + str(modifiers)
    for mod in MODIFIERS:
        print 'mod: ' + str(mod)
        if mod == modifiers:
            modifiers -= mod
            print 'mod: ' + MOD_NAMES[mod]
    print "~~~~~~~~~~~~~~~~~~~~~~:regulars:~~~~~~~~~~~~~~~~~~~~~~"    
    buffer_rest = buffer[1:]
    for c in buffer_rest:
        print ord(c),
    print
