# byzantium

NB: _The code has not been completely imported yet, and won't work without some extra love_

This project is pretty simple; the idea is to make _a normal keyboard_ dynamically reprogrammable _in real time_, through a web app running on some custom hardware (a couple of Raspberry Pis).

It is fast enough to work for people who have trouble using conventional keyboards; it may be fast enough for you, but YMMV.

## rationale

Unfortunately, programming keyboards is hard. I've got a few keyboards; my current favourite is the Keyboard.io Model 01. While the keyboard is beautiful, and a pleasure to type on, it is a pain for me to go and edit the C++ sources to _just to configure it_. This is not Keyboard.io's fault; actually, it is good because C++ is performant, and they are doing great at the hardware level. What we need is more software.

Most people probably don't think about tweaking their layout. That is because the keyboard is made for the average person. Some of us have a different number of digits; some of us may not even have a hand. There is a great amount of work going in to making Human Interface Devices for differently-abled people. But it is hard work. This project aims, among other goals, to ease the burden of iterative development, and implementation of features for such devices.

## the how

Plug a usb keyboard into a raspberry pi. Capture the keyboard input scancodes from events (currently generated by evdev). Send the events to the 2nd Pi, which is able to replay them to the computer it is plugged into.

If some other board is able to work as a USB device ("gadget mode"), and simultaneously work as a USB host ("host mode"), and given it has enough horsepower, it should be able to act in both roles (1st and 2nd RPi). But for now, I am using 2 RPis as follows.

Hardware:
- Raspberry Pi Model 3 B, after this called "Pi 1"
- Raspberry Pi Zero W, after this called "Pi 2"

Software on Pi 1:
- Raspbian Stretch Full
- packages: redis-client, python-evdev
- run "client.py"
- nodejs app to modify keymaps (coming)
- NB: The code on this end has to capture input, in a similar way to other programs; it doesn't need root level privileges.

Software on Pi 2:
- Raspbian Stretch Lite
- packages: redis-server
- run "server.py"
- NB: The code on this end has to be run as root, as the dynamically-generated device file will be usable by root only on system boot.

At this point many other possibilities exist:
- logging
- changing keymaps _in real time_
- adding custom state machines for accessibility, such as "sticky keys"
- removing/changing repeat rates
- metrics on when work is backspace-d out -- "is it working?"
- adding layers

## future work

Performance:
- tackle low-hanging fruit first (nice levels, redis config)

Features:
- select keyboard by region, type, manufacturer
- editor to allow clicking keys in browser, and tapping keys on keyboard, for ID
- editor to allow clicking keys in browser to reassign keys

## why call it byzantium?

This project is about keyboards; when I look at a keyboard, I see a picture made of tiny squares. Byzantine art was often in the form of mosaics (arrangements of little tiles). Furthermore, to me it carries the idea of translation, as it was connected to the West, and yet was so Eastern in many ways. The name carries that idea of connecting "over here" with "over there" (or if you like, "over there" to "over here").

Of course it also sings in a minor key, because what was connected became disconnected; the name is therefore meant to convey the mourning hope that those who have little meaningful opportunity to access the global conversation with computers will one day enjoy the same kind of connection most of us enjoy today.
