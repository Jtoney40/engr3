# SPDX-FileCopyrightText: 2020 FoamyGuy for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
This example script shows how to read button state with
debouncing that does not rely on time.sleep().
"""
import time
import board
from digitalio import DigitalInOut, Direction, Pull

btn1 = DigitalInOut(board.D2)
btn1.direction = Direction.INPUT
btn1.pull = Pull.DOWN

prev_state = btn1.value

btn2 = DigitalInOut(board.D3)
btn2.direction = Direction.INPUT
btn2.pull = Pull.DOWN

prev_state = btn2.value

while True:
    if btn1.value:
        print("BTN1 is down")

    if btn2.value:
        print("BTN2  is down")     

    time.sleep(0.1)    
        
         


