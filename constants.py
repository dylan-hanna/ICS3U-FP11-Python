#!/usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Nov 2019
# This program contains constants for circuitpython 10 tutorial

# Circuitpython screen size is 160x120 and sprites are 16x16
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 16
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
FPS = 60
TOTAL_NUMBER_OF_ALIENS = 3
TOTAL_NUMBER_OF_LASERS = 30
SHIP_SPEED = 2
ALIEN_SPEED = 1
OFF_SCREEN_X = -100
OFF_SCREEN_Y = -100
LASER_SPEED = 2
OFF_TOP_SCREEN = -1 *SPRITE_SIZE
ALIEN_SPEED = 1

NEW_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'
    b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')

# Using for button state
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released"
}