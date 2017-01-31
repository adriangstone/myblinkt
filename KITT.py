# Inspired by the Knight Industries Two Thousand car from Knight Rider

#!/usr/bin/env python

import math
import time

from blinkt import set_clear_on_exit, set_pixel, show, set_brightness


set_clear_on_exit()

#reds = [0, 0, 0, 0, 0, 16, 64, 255, 0, 0, 0, 0, 0, 0, 0]
reds = [0, 0, 0, 0, 0, 0, 8, 255, 8, 0, 0, 0, 0, 0, 0]

start_time = time.time()

while True:
    delta = (time.time() - start_time) * 12

    # Sine wave, spends a little longer at min/max
    #offset = int(round(((math.sin(delta) + 1) / 2) * 7))

    # Triangle wave, a snappy ping-pong effect
    offset = int(abs((delta % 16) - 8))

    for i in range(8):
        set_pixel(i , reds[offset + i], 0, 0)
    show()

    time.sleep(0.1)
