HID_LEFTCTRL   = 0x01
HID_LEFTSHIFT  = 0x02
HID_LEFTALT    = 0x04
HID_LEFTMETA   = 0x08
HID_RIGHTCTRL  = 0x10
HID_RIGHTSHIFT = 0x20
HID_RIGHTALT   = 0x40
HID_RIGHTMETA  = 0x80

MODIFIERS = [
    HID_LEFTCTRL,
    HID_LEFTSHIFT,
    HID_LEFTALT,
    HID_LEFTMETA,
    HID_RIGHTCTRL,
    HID_RIGHTSHIFT,
    HID_RIGHTALT,
    HID_RIGHTMETA
]

MODIFIERS_INDICES = {
    HID_LEFTCTRL:   0,
    HID_LEFTSHIFT:  1,
    HID_LEFTALT:    2,
    HID_LEFTMETA:   3,
    HID_RIGHTCTRL:  4,
    HID_RIGHTSHIFT: 5,
    HID_RIGHTALT:   6,
    HID_RIGHTMETA:  7
}

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

class Keyboard(object):
    def __init__(self, **kwargs):
        super(Keyboard, self)
        self._mods = [False] * len(MODIFIERS)
        self._norms = []

        # build state from 'raw'
        if 'raw' in kwargs:
            raw = kwargs['raw']
            modifiers = ord(raw[0])
            for mod in reversed(MODIFIERS):
                if mod <= modifiers:
                    index = MODIFIERS_INDICES[mod]
                    self._mods[index] = True
                    modifiers -= mod
            
            for byte in raw[2:]:
                val = ord(byte)
                if val > 0:
                    self._norms.append(val)

        # build state from serialized 'state'
        elif 'state' in kwargs:
            state = kwargs['state']
            self._mods = state['_mods'] + []
            self._norms = state['_norms'] + []

    def as_data(self):
        return {
            'type': 'RawBootHIDKeyboard',
            'state': {
                '_mods': self._mods,
                '_norms': self._norms
            }
        }

    def as_raw_event(self):
        report = []
        mods = 0
        for i, mod in enumerate(MODIFIERS):
            if self._mods[i]:
                mods += mod
        
        report.append(chr(mods))
        report.append(chr(0)) # unused
        for norm in self._norms:
            report.append(chr(norm))
        
        # pad to 8 chars
        for i in range(8 - len(report)):
            report.append(chr(0))

        # print("report: " + str(report))
        # str_report = report[0]
        # for r in report[1:]:
        #     str_report += r

        str_report = ''.join(report)
        return str_report  # fixme : .encode() ? -> looks like no for python 2.x .

    @classmethod
    def from_data(cls, **kwargs):
        return cls(**kwargs['state'])