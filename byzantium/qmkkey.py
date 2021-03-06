# qmkkey.py
# constants from the qmk firmware
# defines have been switched basically to python constant assignment


#define IS_ERROR(code)           (KC_ROLL_OVER <= (code) && (code) <= KC_UNDEFINED)
#define IS_ANY(code)             (KC_A         <= (code) && (code) <= 0xFF)
#define IS_KEY(code)             (KC_A         <= (code) && (code) <= KC_EXSEL)
#define IS_MOD(code)             (KC_LCTRL     <= (code) && (code) <= KC_RGUI)

#define IS_SPECIAL(code)         ((0xA5 <= (code) && (code) <= 0xDF) || (0xE8 <= (code) && (code) <= 0xFF))
#define IS_SYSTEM(code)          (KC_PWR       <= (code) && (code) <= KC_WAKE)
#define IS_CONSUMER(code)        (KC_MUTE      <= (code) && (code) <= KC_BRID)

#define IS_FN(code)              (KC_FN0       <= (code) && (code) <= KC_FN31)

#define IS_MOUSEKEY(code)        (KC_MS_UP     <= (code) && (code) <= KC_MS_ACCEL2)
#define IS_MOUSEKEY_MOVE(code)   (KC_MS_UP     <= (code) && (code) <= KC_MS_RIGHT)
#define IS_MOUSEKEY_BUTTON(code) (KC_MS_BTN1   <= (code) && (code) <= KC_MS_BTN5)
#define IS_MOUSEKEY_WHEEL(code)  (KC_MS_WH_UP  <= (code) && (code) <= KC_MS_WH_RIGHT)
#define IS_MOUSEKEY_ACCEL(code)  (KC_MS_ACCEL0 <= (code) && (code) <= KC_MS_ACCEL2)

#define MOD_BIT(code)            (1 << MOD_INDEX(code))
#define MOD_INDEX(code)          ((code) & 0x07)

# MOD_MASK_CTRL             = (MOD_BIT(KC_LCTRL)  | MOD_BIT(KC_RCTRL))
# MOD_MASK_SHIFT            = (MOD_BIT(KC_LSHIFT) | MOD_BIT(KC_RSHIFT))
# MOD_MASK_ALT              = (MOD_BIT(KC_LALT)   | MOD_BIT(KC_RALT))
# MOD_MASK_GUI              = (MOD_BIT(KC_LGUI)   | MOD_BIT(KC_RGUI))
# MOD_MASK_CS               = (MOD_MASK_CTRL  | MOD_MASK_SHIFT)
# MOD_MASK_CA               = (MOD_MASK_CTRL  | MOD_MASK_ALT)
# MOD_MASK_CG               = (MOD_MASK_CTRL  | MOD_MASK_GUI)
# MOD_MASK_SA               = (MOD_MASK_SHIFT | MOD_MASK_ALT)
# MOD_MASK_SG               = (MOD_MASK_SHIFT | MOD_MASK_GUI)
# MOD_MASK_AG               = (MOD_MASK_ALT   | MOD_MASK_GUI)
# MOD_MASK_CSA              = (MOD_MASK_CTRL  | MOD_MASK_SHIFT | MOD_MASK_ALT)
# MOD_MASK_CSG              = (MOD_MASK_CTRL  | MOD_MASK_SHIFT | MOD_MASK_GUI)
# MOD_MASK_CAG              = (MOD_MASK_CTRL  | MOD_MASK_ALT   | MOD_MASK_GUI)
# MOD_MASK_SAG              = (MOD_MASK_SHIFT | MOD_MASK_ALT   | MOD_MASK_GUI)
# MOD_MASK_CSAG             = (MOD_MASK_CTRL  | MOD_MASK_SHIFT | MOD_MASK_ALT | MOD_MASK_GUI)

#define FN_BIT(code)             (1 << FN_INDEX(code))
#define FN_INDEX(code)           ((code) - KC_FN0)


# Keyboard/Keypad Page (0x07)
KC_NO = 0
KC_ROLL = 1
KC_POST = 2
KC_UNDEFINED = 3
KC_A = 4
KC_B = 5
KC_C = 6
KC_D = 7
KC_E = 8
KC_F = 9
KC_G = 10
KC_H = 11
KC_I = 12
KC_J = 13
KC_K = 14
KC_L = 15
KC_M = 16
KC_N = 17
KC_O = 18
KC_P = 19
KC_Q = 20
KC_R = 21
KC_S = 22
KC_T = 23
KC_U = 24
KC_V = 25
KC_W = 26
KC_X = 27
KC_Y = 28
KC_Z = 29
KC_1 = 30
KC_2 = 31
KC_3 = 32
KC_4 = 33
KC_5 = 34
KC_6 = 35
KC_7 = 36
KC_8 = 37
KC_9 = 38
KC_0 = 39
KC_ENTER = 40
KC_ESCAPE = 41
KC_BSPACE = 42
KC_TAB = 43
KC_SPACE = 44
KC_MINUS = 45
KC_EQUAL = 46
KC_LBRACKET = 47
KC_RBRACKET = 48
KC_BSLASH = 49
KC_NONUS_HASH = 50
KC_SCOLON = 51
KC_QUOTE = 52
KC_GRAVE = 53
KC_COMMA = 54
KC_DOT = 55
KC_SLASH = 56
KC_CAPSLOCK = 57
KC_F1 = 58
KC_F2 = 59
KC_F3 = 60
KC_F4 = 61
KC_F5 = 62
KC_F6 = 63
KC_F7 = 64
KC_F8 = 65
KC_F9 = 66
KC_F10 = 67
KC_F11 = 68
KC_F12 = 69
KC_PSCREEN = 70
KC_SCROLLLOCK = 71
KC_PAUSE = 72
KC_INSERT = 73
KC_HOME = 74
KC_PGUP = 75
KC_DELETE = 76
KC_END = 77
KC_PGDOWN = 78
KC_RIGHT = 79
KC_LEFT = 80
KC_DOWN = 81
KC_UP = 82
KC_NUMLOCK = 83
KC_KP_SLASH = 84
KC_KP_ASTERISK = 85
KC_KP_MINUS = 86
KC_KP_PLUS = 87
KC_KP_ENTER = 88
KC_KP_1 = 89
KC_KP_2 = 90
KC_KP_3 = 91
KC_KP_4 = 92
KC_KP_5 = 93
KC_KP_6 = 94
KC_KP_7 = 95
KC_KP_8 = 96
KC_KP_9 = 97
KC_KP_0 = 98
KC_KP_DOT = 99
KC_NONUS_BSLASH = 100
KC_APPLICATION = 101
KC_POWER = 102
KC_KP_EQUAL = 103
KC_F13 = 104
KC_F14 = 105
KC_F15 = 106
KC_F16 = 107
KC_F17 = 108
KC_F18 = 109
KC_F19 = 110
KC_F20 = 111
KC_F21 = 112
KC_F22 = 113
KC_F23 = 114
KC_F24 = 115
KC_EXECUTE = 116
KC_HELP = 117
KC_MENU = 118
KC_SELECT = 119
KC_STOP = 120
KC_AGAIN = 121
KC_UNDO = 122
KC_CUT = 123
KC_COPY = 124
KC_PASTE = 125
KC_FIND = 126
KC__MUTE = 127
KC__VOLUP = 128
KC__VOLDOWN = 129
KC_LOCKING_CAPS = 130
KC_LOCKING_NUM = 131
KC_LOCKING_SCROLL = 132
KC_KP_COMMA = 133
KC_KP_EQUAL_AS400 = 134
KC_INT1 = 135
KC_INT2 = 136
KC_INT3 = 137
KC_INT4 = 138
KC_INT5 = 139
KC_INT6 = 140
KC_INT7 = 141
KC_INT8 = 142
KC_INT9 = 143
KC_LANG1 = 144
KC_LANG2 = 145
KC_LANG3 = 146
KC_LANG4 = 147
KC_LANG5 = 148
KC_LANG6 = 149
KC_LANG7 = 150
KC_LANG8 = 151
KC_LANG9 = 152
KC_ALT_ERASE = 153
KC_SYSREQ = 154
KC_CANCEL = 155
KC_CLEAR = 156
KC_PRIOR = 157
KC_RETURN = 158
KC_SEPARATOR = 159
KC_OUT = 160
KC_OPER = 161
KC_CLEAR_AGAIN = 162
KC_CRSEL = 163
KC_EXSEL = 164

# ***************************************************************
# These keycodes are present in the HID spec, but are           *
# nonfunctional on modern OSes. QMK uses this range (0xA5-0xDF) *
# for the media and function keys instead - see below.          *
# ***************************************************************
KC_KP_00 = 176
KC_KP_000 = 177
KC_THOUSANDS_SEPARATOR = 178
KC_DECIMAL_SEPARATOR = 179
KC_CURRENCY_UNIT = 180
KC_CURRENCY_SUB_UNIT = 181
KC_KP_LPAREN = 182
KC_KP_RPAREN = 183
KC_KP_LCBRACKET = 184
KC_KP_RCBRACKET = 185
KC_KP_TAB = 186
KC_KP_BSPACE = 187
KC_KP_A = 188
KC_KP_B = 189
KC_KP_C = 190
KC_KP_D = 191
KC_KP_E = 192
KC_KP_F = 193
KC_KP_XOR = 194
KC_KP_HAT = 195
KC_KP_PERC = 196
KC_KP_LT = 197
KC_KP_GT = 198
KC_KP_AND = 199
KC_KP_LAZYAND = 200
KC_KP_OR = 201
KC_KP_LAZYOR = 202
KC_KP_COLON = 203
KC_KP_HASH = 204
KC_KP_SPACE = 205
KC_KP_ATMARK = 206
KC_KP_EXCLAMATION = 207
KC_KP_MEM_STORE = 208
KC_KP_MEM_RECALL = 209
KC_KP_MEM_CLEAR = 210
KC_KP_MEM_ADD = 211
KC_KP_MEM_SUB = 212
KC_KP_MEM_MUL = 213
KC_KP_MEM_DIV = 214
KC_KP_PLUS_MINUS = 215
KC_KP_CLEAR = 216
KC_KP_CLEAR_ENTRY = 217
KC_KP_BINARY = 218
KC_KP_OCTAL = 219
KC_KP_DECIMAL = 220
KC_KP_HEXADECIMAL = 221

# Modifiers
KC_LCTRL = 224
KC_LSHIFT = 225
KC_LALT = 226
KC_LGUI = 227
KC_RCTRL = 228
KC_RSHIFT = 229
KC_RALT = 230
KC_RGUI = 231

## Media and Function Keys
# Generic Desktop Page (0x01)
KC_SYSTEM_POWER = 165
KC_SYSTEM_SLEEP = 166
KC_SYSTEM_WAKE = 167

# Consumer Page (0x0C)
KC_AUDIO_MUTE = 168
KC_AUDIO_VOL_UP = 169
KC_AUDIO_VOL_DOWN = 170
KC_MEDIA_NEXT_TRACK = 171
KC_MEDIA_PREV_TRACK = 172
KC_MEDIA_STOP = 173
KC_MEDIA_PLAY_PAUSE = 174
KC_MEDIA_SELECT = 175
KC_MEDIA_EJECT = 176
KC_MAIL = 177
KC_CALCULATOR = 178
KC_MY_COMPUTER = 179
KC_WWW_SEARCH = 180
KC_WWW_HOME = 181
KC_WWW_BACK = 182
KC_WWW_FORWARD = 183
KC_WWW_STOP = 184
KC_WWW_REFRESH = 185
KC_WWW_FAVORITES = 186
KC_MEDIA_FAST_FORWARD = 187
KC_MEDIA_REWIND = 188
KC_BRIGHTNESS_UP = 189
KC_BRIGHTNESS_DOWN = 190

# Function Keys
KC_FN0 = 192
KC_FN1 = 193
KC_FN2 = 194
KC_FN3 = 195
KC_FN4 = 196
KC_FN5 = 197
KC_FN6 = 198
KC_FN7 = 199
KC_FN8 = 200
KC_FN9 = 201
KC_FN10 = 202
KC_FN11 = 203
KC_FN12 = 204
KC_FN13 = 205
KC_FN14 = 206
KC_FN15 = 207
KC_FN16 = 208
KC_FN17 = 209
KC_FN18 = 210
KC_FN19 = 211
KC_FN20 = 212
KC_FN21 = 213
KC_FN22 = 214
KC_FN23 = 215
KC_FN24 = 216
KC_FN25 = 217
KC_FN26 = 218
KC_FN27 = 219
KC_FN28 = 220
KC_FN29 = 221
KC_FN30 = 222
KC_FN31 = 223

# Mouse Buttons
KC_MS_UP = 240
KC_MS_DOWN = 241
KC_MS_LEFT = 242
KC_MS_RIGHT = 243
KC_MS_BTN1 = 244
KC_MS_BTN2 = 245
KC_MS_BTN3 = 246
KC_MS_BTN4 = 247
KC_MS_BTN5 = 248

# Mouse Wheel
KC_MS_WH_UP = 249
KC_MS_WH_DOWN = 250
KC_MS_WH_LEFT = 251
KC_MS_WH_RIGHT = 252

# Acceleration
KC_MS_ACCEL0 = 253
KC_MS_ACCEL1 = 254
KC_MS_ACCEL2 = 255

# Short names for ease of definition of keymap
# Transparent
KC_TRANSPARENT = 1
KC_TRNS = KC_TRANSPARENT

# Punctuation
KC_ENT   = KC_ENTER 
KC_ESC   = KC_ESCAPE 
KC_BSPC  = KC_BSPACE 
KC_SPC   = KC_SPACE 
KC_MINS  = KC_MINUS 
KC_EQL   = KC_EQUAL 
KC_LBRC  = KC_LBRACKET 
KC_RBRC  = KC_RBRACKET 
KC_BSLS  = KC_BSLASH 
KC_NUHS  = KC_NONUS_HASH 
KC_SCLN  = KC_SCOLON 
KC_QUOT  = KC_QUOTE 
KC_GRV   = KC_GRAVE 
KC_COMM  = KC_COMMA 
KC_SLSH  = KC_SLASH 
KC_NUBS  = KC_NONUS_BSLASH 

# Lock Keys
KC_CLCK  = KC_CAPSLOCK 
KC_CAPS  = KC_CAPSLOCK 
KC_SLCK  = KC_SCROLLLOCK 
KC_NLCK  = KC_NUMLOCK 
KC_LCAP  = KC_LOCKING_CAPS 
KC_LNUM  = KC_LOCKING_NUM 
KC_LSCR  = KC_LOCKING_SCROLL 

# Commands
KC_PSCR  = KC_PSCREEN 
KC_PAUS  = KC_PAUSE 
KC_BRK   = KC_PAUSE 
KC_INS   = KC_INSERT 
KC_DEL   = KC_DELETE 
KC_PGDN  = KC_PGDOWN 
KC_RGHT  = KC_RIGHT 
KC_APP   = KC_APPLICATION 
KC_EXEC  = KC_EXECUTE 
KC_SLCT  = KC_SELECT 
KC_AGIN  = KC_AGAIN 
KC_PSTE  = KC_PASTE 
KC_ERAS  = KC_ALT_ERASE 
KC_CLR   = KC_CLEAR 

# Keypad
KC_PSLS  = KC_KP_SLASH 
KC_PAST  = KC_KP_ASTERISK 
KC_PMNS  = KC_KP_MINUS 
KC_PPLS  = KC_KP_PLUS 
KC_PENT  = KC_KP_ENTER 
KC_P1    = KC_KP_1 
KC_P2    = KC_KP_2 
KC_P3    = KC_KP_3 
KC_P4    = KC_KP_4 
KC_P5    = KC_KP_5 
KC_P6    = KC_KP_6 
KC_P7    = KC_KP_7 
KC_P8    = KC_KP_8 
KC_P9    = KC_KP_9 
KC_P0    = KC_KP_0 
KC_PDOT  = KC_KP_DOT 
KC_PEQL  = KC_KP_EQUAL 
KC_PCMM  = KC_KP_COMMA 

# Japanese specific
KC_ZKHK  = KC_GRAVE 
KC_RO    = KC_INT1 
KC_KANA  = KC_INT2 
KC_JYEN  = KC_INT3 
KC_HENK  = KC_INT4 
KC_MHEN  = KC_INT5 

# Korean specific
KC_HAEN  = KC_LANG1 
KC_HANJ  = KC_LANG2 

# Modifiers
KC_LCTL  = KC_LCTRL 
KC_LSFT  = KC_LSHIFT 
KC_LCMD  = KC_LGUI 
KC_LWIN  = KC_LGUI 
KC_RCTL  = KC_RCTRL 
KC_RSFT  = KC_RSHIFT 
KC_ALGR  = KC_RALT 
KC_RCMD  = KC_RGUI 
KC_RWIN  = KC_RGUI 

# Generic Desktop Page (0x01)
KC_PWR   = KC_SYSTEM_POWER 
KC_SLEP  = KC_SYSTEM_SLEEP 
KC_WAKE  = KC_SYSTEM_WAKE 

# Consumer Page (0x0C)
KC_MUTE  = KC_AUDIO_MUTE 
KC_VOLU  = KC_AUDIO_VOL_UP 
KC_VOLD  = KC_AUDIO_VOL_DOWN 
KC_MNXT  = KC_MEDIA_NEXT_TRACK 
KC_MPRV  = KC_MEDIA_PREV_TRACK 
KC_MSTP  = KC_MEDIA_STOP 
KC_MPLY  = KC_MEDIA_PLAY_PAUSE 
KC_MSEL  = KC_MEDIA_SELECT 
KC_EJCT  = KC_MEDIA_EJECT 
KC_MAIL  = KC_MAIL 
KC_CALC  = KC_CALCULATOR 
KC_MYCM  = KC_MY_COMPUTER 
KC_WSCH  = KC_WWW_SEARCH 
KC_WHOM  = KC_WWW_HOME 
KC_WBAK  = KC_WWW_BACK 
KC_WFWD  = KC_WWW_FORWARD 
KC_WSTP  = KC_WWW_STOP 
KC_WREF  = KC_WWW_REFRESH 
KC_WFAV  = KC_WWW_FAVORITES 
KC_MFFD  = KC_MEDIA_FAST_FORWARD 
KC_MRWD  = KC_MEDIA_REWIND 
KC_BRIU  = KC_BRIGHTNESS_UP 
KC_BRID  = KC_BRIGHTNESS_DOWN 

# System Specific
KC_BRMU  = KC_PAUSE 
KC_BRMD  = KC_SCROLLLOCK 

# Mouse Keys
KC_MS_U  = KC_MS_UP 
KC_MS_D  = KC_MS_DOWN 
KC_MS_L  = KC_MS_LEFT 
KC_MS_R  = KC_MS_RIGHT 
KC_BTN1  = KC_MS_BTN1 
KC_BTN2  = KC_MS_BTN2 
KC_BTN3  = KC_MS_BTN3 
KC_BTN4  = KC_MS_BTN4 
KC_BTN5  = KC_MS_BTN5 
KC_WH_U  = KC_MS_WH_UP 
KC_WH_D  = KC_MS_WH_DOWN 
KC_WH_L  = KC_MS_WH_LEFT 
KC_WH_R  = KC_MS_WH_RIGHT 
KC_ACL0  = KC_MS_ACCEL0 
KC_ACL1  = KC_MS_ACCEL1 
KC_ACL2  = KC_MS_ACCEL2 


#
FN_MIN = KC_FN0
FN_MAX = KC_FN31
