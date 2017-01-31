#!/usr/bin/env python

import time

from blinkt import set_clear_on_exit, set_pixel, show


set_clear_on_exit()

def show_all(state):
    for i in range(8):
        val = state * 255
        set_pixel(i, val, val, val)
    show()

def show_red(state):
    for i in range(4):
        val = 255
        set_pixel(i, val, 0, 0) 
        set_pixel(i+4, 0, 0, 0)
    show()

def show_blue(state):
    for i in range(4):
        val = 255
        set_pixel(i+4, 0, 0, val)
        set_pixel(i, 0, 0, 0)
    show()

def flash_red():
    show_red(1)
    time.sleep(0.05)
    show_all(0)
    time.sleep(0.05)

def flash_blue():
    show_blue(1)
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

#0 is a space, 1 is a dot and 2 is a dash
morse = '1111022220'

while True:
    for m in morse:
        if m == '0':
            space()
        elif m == '1':
            flash_red()
        elif m == '2':
            flash_blue()
