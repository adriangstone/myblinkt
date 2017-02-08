# Inspired by flashing lights on maintenance vehicles

#!/usr/bin/env python

import time

from blinkt import set_clear_on_exit, set_pixel, show


set_clear_on_exit()

def show_all(state):
    for i in range(8):
        val = state * 255
        set_pixel(i, val, val, val)
    show()

def show_bank1(state):
    for i in range(4):
        set_pixel(i, 250, 50, 0) 
    show()

def show_bank2(state):
    for i in range(4):
        set_pixel(i+4, 250, 50, 0)
    show()

def flash_bank1():
    show_bank1(1)
    time.sleep(0.05)
    show_all(0)
    time.sleep(0.05)

def flash_bank2():
    show_bank2(1)
    time.sleep(0.05)
    show_all(0)
    time.sleep(0.05)

def dot():
    show_all(1)
    time.sleep(0.05)
    show_all(0)
    time.sleep(0.2)

def dash():
    show_all(1)
    time.sleep(0.2)
    show_all(0)
    time.sleep(0.2)

def space():
    time.sleep(0.1)

morse = '1111022220'

while True:
    for m in morse:
        if m == '0':
            space()
        elif m == '1':
            flash_bank1()
        elif m == '2':
            flash_bank2()
