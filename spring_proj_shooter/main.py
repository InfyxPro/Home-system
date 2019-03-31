#
#  main.py
#  Created by Dominik Chraca on 3/18/19.
#
# Credit "Kenney.nl" or "www.kenney.nl"

import os
import pygame
import math
import random
import time

# Setup 64X47 1024
WIDTH = 1024
HEIGHT = 750
FPS = 30

#boolean map every 16 pixels apart
MAP = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [2,2,2,2,2,2,2,1,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,0,0,0,0,0,0,0,2,1,1,1,2,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,0,0,0,0,0,0,1,2,2,2,2,2,2,2],\
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,1,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,1,1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,1,1,0,0,0,0,0,0],\
       [0,0,0,0,0,2,1,1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,1,1,2,0,0,0,0,0],\
       [2,2,2,2,2,2,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,2,2,2,2,2,2],\
       [2,2,2,2,2,2,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,2,2,2,2,2,2],\
       [0,0,0,0,0,2,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,2,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,1,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0],\
       [0,0,0,0,0,0,2,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,2,0,0,0,0,0],\
       [0,0,0,0,0,0,2,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,2,0,0,0,0,0],\
       [0,0,0,0,0,0,2,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,2,0,0,0,0,0],\
       [0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,2,1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,1,2,0,0,0,0,0],\
       [2,2,2,2,2,2,1,1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,1,1,2,2,2,2,2,2],\
       [2,2,2,2,2,2,1,1,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,1,1,2,2,2,2,2,2],\
       [0,0,0,0,0,2,1,1,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,1,1,2,0,0,0,0,0],\
       [0,0,0,0,0,0,1,1,0,0,0,0,0,0,2,2,2,2,1,1,1,1,1,1,0,0,0,0,2,2,1,1,1,2,2,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,0,0,0,0,0,0,1,1,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],\
       [2,2,2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0],\
       [0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]\
       ] #not used

# Globals
random.seed(time.time())
global game_folder
# enemy: slime = 2 ghost = 3 fly = 0 block = 1 trump = 4 [x,y,time,enemytype,alive]
waves = \
[[[WIDTH * 0.5, HEIGHT * 0.5,10,4,1] #wave 0 boss
],
[#wave 1
[WIDTH * 0.05, HEIGHT * 0.16,7,0,1],
[WIDTH * 0.95,HEIGHT * 0.16,8,0,1],
[WIDTH * 0.95,HEIGHT * 0.84,9,0,1],
[WIDTH * 0.04,HEIGHT * 0.84,10,0,1],
[WIDTH * 0.15,HEIGHT * 0.21,11,0,1],
[WIDTH * 0.15,HEIGHT * 0.8,11,0,1],
[WIDTH * 0.83,HEIGHT * 0.21,11,0,1],
[WIDTH * 0.83,HEIGHT * 0.8,11,0,1],
[WIDTH * 0.283,HEIGHT * 0.13,15,0,1],
[WIDTH * 0.5,HEIGHT * 0.13,16,0,1],
[WIDTH * 0.283,HEIGHT * 0.13,17,0,1],
[WIDTH * 0.15,HEIGHT * 0.13,18,0,1],
[WIDTH * 0.283,HEIGHT * 0.97,19,0,1],
[WIDTH * 0.69,HEIGHT * 0.97,20,0,1],
[WIDTH * 0.83,HEIGHT * 0.97,21,0,1],
[WIDTH * 0.95,HEIGHT * 0.97,22,0,1]],
[[WIDTH * 0.04, HEIGHT * 0.13,5,0,1], #wave 2
[WIDTH * 0.04,HEIGHT * 0.23,5,0,1],
[WIDTH * 0.04,HEIGHT * 0.375,5,0,1],
[WIDTH * 0.04,HEIGHT * 0.5,5,0,1],
[WIDTH * 0.04,HEIGHT * 0.65,5,0,1],
[WIDTH * 0.04,HEIGHT * 0.83,5,0,1],
 [WIDTH * 0.95,HEIGHT * 0.13,5,0,1],
[WIDTH * 0.95,HEIGHT * 0.23,5,0,1],
[WIDTH * 0.95,HEIGHT * 0.375,5,0,1],
[WIDTH * 0.95,HEIGHT * 0.5,5,0,1],
[WIDTH * 0.95,HEIGHT * 0.65,5,0,1],
[WIDTH * 0.95,HEIGHT * 0.83,5,0,1],
[WIDTH * 0.04,HEIGHT * 0.55,7.5,1,1],
[WIDTH * 0.95,HEIGHT * 0.97,7.5,1,1],
[WIDTH * 0.4,HEIGHT * 0.13,7.5,1,1],
[WIDTH * 0.6,HEIGHT * 0.55,7.5,1,1],
[WIDTH * 0.6,HEIGHT * 0.55,14,0,1],
[WIDTH * 0.6,HEIGHT * 0.55,14,0,1],
[WIDTH * 0.4,HEIGHT * 0.55,14,0,1],
[WIDTH * 0.4,HEIGHT * 0.55,14,0,1],
[WIDTH * 0.4,HEIGHT * 0.55,14,0,1],
[WIDTH * 0.6,HEIGHT * 0.55,14,0,1]],
[[WIDTH * 0.283, HEIGHT * 0.375,7,0,1],#wave 3 #flys
[WIDTH * 0.283, HEIGHT * 0.375,7,0,1],
[WIDTH * 0.283, HEIGHT * 0.375,7,0,1],
[WIDTH * 0.283, HEIGHT * 0.375,7,0,1],
[WIDTH * 0.69,HEIGHT * 0.375,7.5,0,1],
[WIDTH * 0.69,HEIGHT * 0.375,7.5,0,1],
[WIDTH * 0.69,HEIGHT * 0.375,7.5,0,1],
[WIDTH * 0.69,HEIGHT * 0.375,7.5,0,1],
[WIDTH * 0.283,HEIGHT * 0.65,8,0,1],
[WIDTH * 0.283,HEIGHT * 0.65,8,0,1],
[WIDTH * 0.283,HEIGHT * 0.65,8,0,1],
[WIDTH * 0.283,HEIGHT * 0.65,8,0,1],
[WIDTH * 0.69,HEIGHT * 0.65,8.5,0,1],
[WIDTH * 0.69,HEIGHT * 0.65,8.5,0,1],
[WIDTH * 0.69,HEIGHT * 0.65,8.5,0,1],
[WIDTH * 0.69,HEIGHT * 0.65,8.5,0,1],
 #blocks
[WIDTH * 0.15,HEIGHT * 0.96,11,1,1],
[WIDTH * 0.95,HEIGHT * 0.96,12,1,1],
[WIDTH * 0.15,HEIGHT * 0.13,13,1,1],
[WIDTH * 0.95,HEIGHT * 0.13,14,1,1],
[WIDTH * 0.15,HEIGHT * 0.96,25,1,1],
[WIDTH * 0.95,HEIGHT * 0.96,26,1,1],
[WIDTH * 0.15,HEIGHT * 0.13,27,1,1],
[WIDTH * 0.95,HEIGHT * 0.13,28,1,1],
[WIDTH * 0.15,HEIGHT * 0.96,35,1,1],
[WIDTH * 0.95,HEIGHT * 0.96,36,1,1],
[WIDTH * 0.15,HEIGHT * 0.13,37,1,1],
[WIDTH * 0.95,HEIGHT * 0.13,38,1,1],
[WIDTH * 0.5,HEIGHT * 0.7,45,1,1]],
[[WIDTH * 0.5, HEIGHT * 0.6,5,0,1], #wave 4
[WIDTH * 0.5,HEIGHT * 0.5,5,0,1],
[WIDTH * 0.5,HEIGHT * 0.5,5,0,1],
[WIDTH * 0.5,HEIGHT * 0.5,5,0,1],
[WIDTH * 0.5,HEIGHT * 0.5,5,0,1],
[WIDTH * 0.5,HEIGHT * 0.5,5,0,1],
[WIDTH * 0.5,HEIGHT * 0.5,5,0,1],
[WIDTH * 0.5,HEIGHT * 0.5,5,0,1],
[WIDTH * 0.5,HEIGHT * 0.5,5,0,1],
[WIDTH * 0.5,HEIGHT * 0.5,5,0,1],
[WIDTH * 0.5,HEIGHT * 0.5,5,0,1],
[WIDTH * 0.5,HEIGHT * 0.5,5,0,1],
[WIDTH * 0.5,HEIGHT * 0.5,5,0,1],
[WIDTH * 0.5,HEIGHT * 0.5,5,0,1],
[WIDTH * 0.5,HEIGHT * 0.5,5,0,1],
[WIDTH * 0.5,HEIGHT * 0.5,5,0,1],
[WIDTH * 0.5,HEIGHT * 0.5,5,0,1],
[WIDTH * 0.5,HEIGHT * 0.5,5,0,1],
[WIDTH * 0.5,HEIGHT * 0.5,5,0,1],
[WIDTH * 0.15,HEIGHT * 0.96,10,2,1],
[WIDTH * 0.95,HEIGHT * 0.96,10,2,1],
[WIDTH * 0.15,HEIGHT * 0.13,10,2,1],
[WIDTH * 0.95,HEIGHT * 0.13,10,2,1],
[WIDTH * 0.5,HEIGHT * 0.2,22,2,1]],
[[WIDTH * 0.5, HEIGHT * 0.6,7,1,1], #wave 5
[WIDTH * 0.04,HEIGHT * 0.89,7,1,1],
[WIDTH * 0.95,HEIGHT * 0.89,7,1,1],
[WIDTH * 0.15,HEIGHT * 0.89,7,1,1],
[WIDTH * 0.83,HEIGHT * 0.89,7,1,1],
[WIDTH * 0.5,HEIGHT * 0.89,7,1,1],
[WIDTH * 0.3,HEIGHT * 0.89,7,1,1],
[WIDTH * 0.7,HEIGHT * 0.89,7,1,1],
#Slime
[WIDTH * 0.1,HEIGHT * 0.04,12,2,1],
[WIDTH * 0.2,HEIGHT * 0.04,12.2,2,1],
[WIDTH * 0.3,HEIGHT * 0.04,12.4,2,1],
[WIDTH * 0.4,HEIGHT * 0.04,12.6,2,1],
[WIDTH * 0.6,HEIGHT * 0.04,12.8,2,1],
[WIDTH * 0.7,HEIGHT * 0.04,13,2,1],
[WIDTH * 0.8,HEIGHT * 0.04,13.2,2,1],
[WIDTH * 0.9,HEIGHT * 0.04,13.4,2,1]],
[[WIDTH * 0.5, HEIGHT * 0.6,5,0,1], #wave 6 ghost
[WIDTH * 0.95,HEIGHT * 0.16,5.1,0,1],
[WIDTH * 0.95,HEIGHT * 0.84,5.2,0,1],
[WIDTH * 0.04,HEIGHT * 0.84,5.3,0,1],
[WIDTH * 0.15,HEIGHT * 0.21,5.4,0,1],
[WIDTH * 0.15,HEIGHT * 0.8,5.5,0,1],
[WIDTH * 0.83,HEIGHT * 0.21,5.6,0,1],
[WIDTH * 0.83,HEIGHT * 0.8,5.7,0,1],
[WIDTH * 0.283,HEIGHT * 0.13,5.8,0,1],
[WIDTH * 0.5,HEIGHT * 0.13,5.9,0,1],
[WIDTH * 0.283,HEIGHT * 0.13,6,0,1],
[WIDTH * 0.15,HEIGHT * 0.13,6.1,0,1],
[WIDTH * 0.283,HEIGHT * 0.97,6.2,0,1],
[WIDTH * 0.69,HEIGHT * 0.97,6.3,0,1],
[WIDTH * 0.83,HEIGHT * 0.97,6.4,0,1],
[WIDTH * 0.05,HEIGHT * 0.55,7,3,1],
[WIDTH * 0.95,HEIGHT * 0.55,7,3,1],
[WIDTH * 0.5,HEIGHT * 0.55,7,3,1],
[WIDTH * 0.5,HEIGHT * 0.2,10,0,1],
[WIDTH * 0.5,HEIGHT * 0.55,25,3,1],
[WIDTH * 0.5,HEIGHT * 0.55,25.5,3,1],
[WIDTH * 0.5,HEIGHT * 0.55,26,3,1],
[WIDTH * 0.5,HEIGHT * 0.55,26.5,3,1],
[WIDTH * 0.5,HEIGHT * 0.55,27,3,1],
[WIDTH * 0.5,HEIGHT * 0.55,27.5,3,1],
[WIDTH * 0.5,HEIGHT * 0.55,28,3,1],
[WIDTH * 0.5,HEIGHT * 0.55,28.5,3,1]
],
[
[WIDTH * 0.95, HEIGHT * 0.16,5,0,1], #wave 7 all enemy
[WIDTH * 0.95,HEIGHT * 0.16,5.1,0,1],
[WIDTH * 0.95,HEIGHT * 0.84,5.2,0,1],
[WIDTH * 0.04,HEIGHT * 0.84,5.3,0,1],
[WIDTH * 0.15,HEIGHT * 0.21,5.4,0,1],
[WIDTH * 0.15,HEIGHT * 0.8,5.5,0,1],
[WIDTH * 0.83,HEIGHT * 0.21,5.6,0,1],
[WIDTH * 0.83,HEIGHT * 0.8,5.7,0,1],
[WIDTH * 0.283,HEIGHT * 0.13,5.8,0,1],
[WIDTH * 0.5,HEIGHT * 0.13,5.9,0,1],
[WIDTH * 0.283,HEIGHT * 0.13,6,0,1],
[WIDTH * 0.15,HEIGHT * 0.13,6.1,0,1],
[WIDTH * 0.283,HEIGHT * 0.97,6.2,0,1],
[WIDTH * 0.69,HEIGHT * 0.97,6.3,0,1],
[WIDTH * 0.83,HEIGHT * 0.97,6.4,0,1],
 
[WIDTH * 0.5,HEIGHT * 0.55,7,2,1],
[WIDTH * 0.5,HEIGHT * 0.55,8,2,1],
[WIDTH * 0.69,HEIGHT * 0.55,8,1,1],
[WIDTH * 0.5,HEIGHT * 0.55,9,2,1],
[WIDTH * 0.5,HEIGHT * 0.55,10,2,1],
[WIDTH * 0.5,HEIGHT * 0.55,11,2,1],
[WIDTH * 0.283,HEIGHT * 0.55,11,1,1],
[WIDTH * 0.5,HEIGHT * 0.55,12,2,1],
[WIDTH * 0.5,HEIGHT * 0.55,13,2,1],

[WIDTH * 0.04,HEIGHT * 0.89,20,1,1],
[WIDTH * 0.95,HEIGHT * 0.89,21,1,1],
[WIDTH * 0.15,HEIGHT * 0.89,22,1,1],
[WIDTH * 0.83,HEIGHT * 0.89,23,1,1],
[WIDTH * 0.5,HEIGHT * 0.89,24,1,1],
[WIDTH * 0.3,HEIGHT * 0.89,25,1,1],
[WIDTH * 0.7,HEIGHT * 0.89,26,1,1],
 
[WIDTH * 0.283, HEIGHT * 0.375,30,3,1],
[WIDTH * 0.283, HEIGHT * 0.375,31,3,1],
[WIDTH * 0.283, HEIGHT * 0.375,32,3,1],
[WIDTH * 0.69,HEIGHT * 0.375,33,3,1],
[WIDTH * 0.69,HEIGHT * 0.375,33,3,1],
[WIDTH * 0.69,HEIGHT * 0.375,33,3,1],
[WIDTH * 0.69,HEIGHT * 0.375,36,3,1],
[WIDTH * 0.283,HEIGHT * 0.65,37,3,1],
[WIDTH * 0.283,HEIGHT * 0.65,38,3,1],
[WIDTH * 0.283,HEIGHT * 0.65,39,3,1],
[WIDTH * 0.283,HEIGHT * 0.65,40,3,1],
[WIDTH * 0.69,HEIGHT * 0.65,41,3,1],
[WIDTH * 0.69,HEIGHT * 0.65,42,3,1],
[WIDTH * 0.69,HEIGHT * 0.65,43,3,1],
[WIDTH * 0.69,HEIGHT * 0.65,45,3,1],
 
[WIDTH * 0.5,HEIGHT * 0.2,50,0,1],
[WIDTH * 0.5,HEIGHT * 0.2,50,0,1]
 ],
[#wave 8
[WIDTH * 0.5, HEIGHT * 0.375,7,1,1],
[WIDTH * 0.5,HEIGHT * 0.65,8,1,1],
[WIDTH * 0.283,HEIGHT * 0.375,9,1,1],
[WIDTH * 0.283,HEIGHT * 0.65,10,1,1],
[WIDTH * 0.69,HEIGHT * 0.375,11,1,1],
[WIDTH * 0.69,HEIGHT * 0.65,12,1,1],

[WIDTH * 0.05, HEIGHT * 0.16,15,0,1],
[WIDTH * 0.95,HEIGHT * 0.16,15,0,1],
[WIDTH * 0.95,HEIGHT * 0.84,15,0,1],
[WIDTH * 0.04,HEIGHT * 0.84,15,0,1],
[WIDTH * 0.15,HEIGHT * 0.21,15,0,1],
[WIDTH * 0.15,HEIGHT * 0.8,15,0,1],
[WIDTH * 0.83,HEIGHT * 0.21,15,0,1],
[WIDTH * 0.83,HEIGHT * 0.8,15,0,1],
[WIDTH * 0.283,HEIGHT * 0.13,15,0,1],
[WIDTH * 0.5,HEIGHT * 0.13,15,0,1],
[WIDTH * 0.283,HEIGHT * 0.13,15,0,1],
[WIDTH * 0.15,HEIGHT * 0.13,15,0,1],

[WIDTH * 0.69,HEIGHT * 0.65,23,3,1],
[WIDTH * 0.69,HEIGHT * 0.65,23,3,1],
[WIDTH * 0.69,HEIGHT * 0.65,23,3,1],
[WIDTH * 0.61,HEIGHT * 0.65,23,3,1],
 
[WIDTH * 0.15,HEIGHT * 0.96,10,2,1],
[WIDTH * 0.95,HEIGHT * 0.96,10,2,1],
[WIDTH * 0.15,HEIGHT * 0.13,10,2,1],
[WIDTH * 0.95,HEIGHT * 0.13,10,2,1],

 
[WIDTH * 0.5,HEIGHT * 0.2,22,0,1]
 ],
[#wave 9
 [WIDTH * 0.5, HEIGHT * 0.75,7,1,1],
[WIDTH * 0.5, HEIGHT * 0.6,7,0,1],
[WIDTH * 0.5,HEIGHT * 0.8,8,0,1],
[WIDTH * 0.6,HEIGHT * 0.5,9,0,1],
[WIDTH * 0.5,HEIGHT * 0.3,10,0,1],
[WIDTH * 0.6,HEIGHT * 0.7,11,0,1],
[WIDTH * 0.8,HEIGHT * 0.8,12,0,1],
[WIDTH * 0.5,HEIGHT * 0.5,13,0,1],
[WIDTH * 0.5,HEIGHT * 0.2,14,0,1],
[WIDTH * 0.5,HEIGHT * 0.2,15,0,1],
[WIDTH * 0.5,HEIGHT * 0.2,16,0,1],
[WIDTH * 0.5,HEIGHT * 0.2,17,0,1],
[WIDTH * 0.5,HEIGHT * 0.2,18,0,1],
[WIDTH * 0.5,HEIGHT * 0.2,19,0,1],
[WIDTH * 0.5,HEIGHT * 0.2,20,0,1],
[WIDTH * 0.5,HEIGHT * 0.2,21,0,1],
[WIDTH * 0.5,HEIGHT * 0.2,22,0,1]
]]



game_folder = os.path.dirname(__file__)
location = os.path.join(game_folder, "pic_bmp")
sounds = os.path.join(game_folder, "sounds")

pygame.init()
pygame.joystick.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('"Bang!"')
clock = pygame.time.Clock()
player_1_sprites = pygame.sprite.Group()
player_2_sprites = pygame.sprite.Group()
player_3_sprites = pygame.sprite.Group()
player_4_sprites = pygame.sprite.Group()

ghost_sprites = pygame.sprite.Group()
block_sprites = pygame.sprite.Group()
slime_sprites = pygame.sprite.Group()
fly_sprites = pygame.sprite.Group()
trump_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

wall_sprites = pygame.sprite.Group()
water_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()
bulletx2_sprites = pygame.sprite.Group()
enemy_bullet_sprites = pygame.sprite.Group()
enemy_bomb_sprites = pygame.sprite.Group()

UI_HP1_sprites = pygame.sprite.Group()
UI_HP2_sprites = pygame.sprite.Group()
UI_AP1_sprites = pygame.sprite.Group()
UI_AP2_sprites = pygame.sprite.Group()
UI_HP3_sprites = pygame.sprite.Group()
UI_AP3_sprites = pygame.sprite.Group()
UI_HP4_sprites = pygame.sprite.Group()
UI_AP4_sprites = pygame.sprite.Group()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PEACH_1 = (205,175,149)
PEACH_2 = (255,218,185)


# Functions

def UI_function(H1 = None, A1 = None, H2 = None, A2 = None, H3 = None, A3 = None, H4 = None, A4 = None):
    x = 8
    y = 4
    for i in range(0,H1):
        V = __UI__(x,y,hp_img,i)
        UI_HP1_sprites.add(V)
        x += 20

    x = 8
    y = 21
    for i in range(0,A1):
        V = __UI__(x,y,ammo_img,i)
        UI_AP1_sprites.add(V)
        x += 20
    x = 1000
    y = 4
    for i in range(0,H4):
        V = __UI__(x,y,hp_img,i)
        UI_HP4_sprites.add(V)
        x -= 20

    x = 1000
    y = 21
    for i in range(0,A4):
        V = __UI__(x,y,ammo_img,i)
        UI_AP4_sprites.add(V)
        x -= 20

    x = 800
    y = 4
    for i in range(0,H3):
        V = __UI__(x,y,hp_img,i)
        UI_HP3_sprites.add(V)
        x -= 20
    
    x = 800
    y = 21
    for i in range(0,A3):
        V = __UI__(x,y,ammo_img,i)
        UI_AP3_sprites.add(V)
        x -= 20

    x = 208
    y = 4
    for i in range(0,H2):
        V = __UI__(x,y,hp_img,i)
        UI_HP2_sprites.add(V)
        x += 20
    
    x = 208
    y = 21
    for i in range(0,A2):
        V = __UI__(x,y,ammo_img,i)
        UI_AP2_sprites.add(V)
        x += 20


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class wall(pygame.sprite.Sprite):
    def __init__(self,x,y,player_img_1):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img_1
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

class __UI__(pygame.sprite.Sprite):
    def __init__(self,x,y,player_img_1,amount):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img_1
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.amount = amount
        self.x = x
        self.y = y
    
    def update(self, current_atr):
        if (self.amount >= current_atr): #Delete Health or ammo box for UI
            self.rect.y = -100
        else:
            self.rect.y = self.y
            self.rect.x = self.x

class GLITCH_BOSS(pygame.sprite.Sprite):
    def __init__(self ,health, glitch_img, blink_img, img1, img2, map_img):
        global points
        pygame.sprite.Sprite.__init__(self)
        self.x = 500
        self.y = 500
        self.glitch_img = glitch_img
        self.image = self.glitch_img
        self.blink_img = blink_img
        self.img1 = img1
        self.img2 = img2
        self.map_img = map_img

        self.points = points
        
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.MH = health
        self.health = health
        self.half_health = health * 0.5
        self.MS = 2
        self.time = StopWatch()
        self.move_once = 1
        background_horror_sound.play(-1)
        self.spawn_once = 1
        self.quick_shoot_once = 1
        self.bomb_once = 1
        
        self.enter_time = StopWatch()
        
        self.blink_time = StopWatch()
        self.blink_value = (random.randint(10,25)/10)
        self.blink_amount = 0
        
        self.glitch_time = StopWatch()
        self.glitch_value = random.randint(1,7)
        self.glitch_amount = 0
        self.glitch_type = 0
    

    def update(self,x1 = None,y1 = None,x2 = None,y2 = None, x3 = None, y3 = None, x4 = None, y4 = None):
        global points
        points = 666
        #For health
        if (pygame.sprite.spritecollideany(self,bullet_sprites)):
            self.health -= 1
        if (pygame.sprite.spritecollideany(self,bulletx2_sprites)):
            self.health -= 2
        if (self.health <= 0):
            background_horror_sound.stop()
            glitching_out_sound.play()
            points = self.points
            self.kill()
        #Teleports boss when 5 damage is done
        if (self.health % 5 == 0 and self.move_once):
            take_control_player_sound.set_volume(.3)
            take_control_player_sound.play(0,10000)
            self.rect.x = random.randint(0,WIDTH)
            self.rect.y = random.randint(10,HEIGHT)
            self.move_once = 0
            for i in range(0,7):
                rad = (i-1) * 0.7854
                bullet = EBULLETS(self.rect.x + 45,self.rect.y + 45, rad,m4_img,1)
                enemy_bullet_sprites.add(bullet)
                enemy_sprites.add(bullet)
        elif(not self.health % 5 == 0):
            self.move_once = 1
        
        #For blinking
        self.image = self.glitch_img
        if (self.blink_time.elapsed(1) >= self.blink_value):
            self.blink_time = StopWatch()
            self.blink_value = random.randint(20,35) / 10
            self.blink_amount = random.randint(1,5) / 10
        if(self.blink_time.elapsed(1) <= self.blink_amount):
            self.image = self.blink_img
            self.image.set_colorkey(BLACK)
        #For glitching
        if (self.glitch_time.elapsed(1) >= self.glitch_value):
            self.glitch_time = StopWatch()
            self.glitch_value = random.randint(1,7)
            self.glitch_amount = random.randint(1,3) / 10
            self.glitch_type = random.randint(0,2)
        if(self.glitch_time.elapsed(1) <= self.glitch_amount):
            if (self.glitch_type == 0):
                self.image = self.img1
                self.image.set_colorkey(BLACK)
            elif(self.glitch_type == 1):
                self.image = self.img2
                self.image.set_colorkey(BLACK)
        
        
        #Display health
        pygame.draw.rect(screen,RED,pygame.Rect(self.rect.x,self.rect.y- 10,map(self.health,0,self.MH,0,40),10),0)

class BOSS(pygame.sprite.Sprite):
    def __init__(self ,x ,y ,player_img_1, health):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = player_img_1
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.MH = health
        self.health = health
        self.half_health = health * 0.5
        self.MS = 2
        self.time = StopWatch()
        self.talk_once = 1
        trump_enter_sound.play()
        self.spawn_once = 1
        self.quick_shoot_once = 1
        self.bomb_once = 1
        self.bomb_time = StopWatch()
        self.time_1 = time.clock()
        self.time_new = time.clock()
    
        
    def update(self,x1 = None,y1 = None,x2 = None,y2 = None, x3 = None, y3 = None, x4 = None, y4 = None):
        #Make sound when hurt ever 20 damage
        self.time_1 = time.clock()
        if (self.time_new <= self.time_1):
            self.time_new = time.clock() + (random.randint(10,40) / 10)
            self.x_dis = round(random.randint(-20,20) / 13)
            self.y_dis = round(random.randint(-20,20) / 13)
                #Move boss random
        self.rect.x += self.x_dis
        self.rect.y += self.y_dis
        if (self.rect.bottom >= HEIGHT) or (self.rect.top <= 0):
            self.rect.y -=  self.y_dis
        if (self.rect.right > WIDTH) or (self.rect.left < 0):
            self.rect.x -= self.x_dis
        if ((self.talk_once) and ((self.health % 20) == 0)):
            self.talk_once = 0
            x = random.randint(1,3)
            if (x == 1): trump_hurt1_sound.play()
            elif (x == 2): trump_hurt2_sound.play()
            elif (x == 3): trump_hurt3_sound.play()
        elif (not ((self.health % 10) == 0)): self.talk_once = 1
        
        if (pygame.sprite.spritecollideany(self,bullet_sprites)):
            self.health -= 1
        if (pygame.sprite.spritecollideany(self,bulletx2_sprites)):
            self.health -= 2
        if (self.health <= 0):
            trump_dead_sound.play()
            self.kill()
        #Display health
        pygame.draw.rect(screen,RED,pygame.Rect(self.rect.x,self.rect.y- 10,map(self.health,0,self.MH,0,200),10),0)
        
        if((self.health <= self.half_health)):
            self.spawn_once = boss_enemy_creater(self.time.elapsed(), 30,self.spawn_once)
        
        x = 0
        y = 0
        x1_dis = x1 - (self.rect.center[0]) + 17
        y1_dis = y1 - (self.rect.center[1]) + 17
        x2_dis = x2 - self.rect.center[0] + 17
        y2_dis = y2 - self.rect.center[1] + 17
        x3_dis = x3 - self.rect.center[0] + 17
        y3_dis = y3 - self.rect.center[1] + 17
        x4_dis = x4 - self.rect.center[0] + 17
        y4_dis = y4 - self.rect.center[1] + 17
        dist1 = math.sqrt((x1_dis * x1_dis) + (y1_dis * y1_dis))
        dist2 = math.sqrt((x2_dis * x2_dis) + (y2_dis * y2_dis))
        dist3 = math.sqrt((x3_dis * x3_dis) + (y3_dis * y3_dis))
        dist4 = math.sqrt((x4_dis * x4_dis) + (y4_dis * y4_dis))
        rads_4 = math.atan2(y4_dis , (x4_dis))
        rads_3 = math.atan2(y3_dis , (x3_dis))
        rads_2 = math.atan2(y2_dis , (x2_dis))
        rads_1 = math.atan2(y1_dis , (x1_dis))
        p1 = 0
        p2 = 0
        p3 = 0
        p4 = 0
        if (dist1 <= dist2 and dist1 <= dist3 and dist1 <= dist4): #player one closer
            p1 = 1
        elif (dist2 <= dist3 and dist2 <= dist4): #plyer two closer
            p2 = 1
        elif (dist3 < dist4): #plyer three closer
            p3 = 1
        else: #plyer four closer
            p4 = 1

        #Boss shooting
        if ((int(self.time.elapsed()) % 10) == 0):
            if (self.quick_shoot_once):
                self.quick_shoot_once = 0
                trump_shoot_bullets_sound.play(-1,10)
                __bullet__ = EBULLETS(self.rect.x + 100,self.rect.y + 113,rads_1,bullet_img2,1)#player 1
                enemy_bullet_sprites.add(__bullet__)
                enemy_sprites.add(__bullet__)
                __bullet__ = EBULLETS(self.rect.x + 100,self.rect.y + 113,rads_2,bullet_img2,1) #Player 2
                enemy_bullet_sprites.add(__bullet__)
                enemy_sprites.add(__bullet__)
                __bullet__ = EBULLETS(self.rect.x + 100,self.rect.y + 113,rads_3,bullet_img2,1) #Player 3
                enemy_bullet_sprites.add(__bullet__)
                enemy_sprites.add(__bullet__)
                __bullet__ = EBULLETS(self.rect.x + 100,self.rect.y + 113,rads_4,bullet_img2,1) #Player 4
                enemy_bullet_sprites.add(__bullet__)
                enemy_sprites.add(__bullet__)
            elif(self.time.elapsed()*10 % 2 == 0):
                self.quick_shoot_once = 1
                trump_shoot_bullets_sound.stop()
        #Shooting bomb
        if (((int(self.time.elapsed()) % 18) == 0) and self.bomb_once):
            self.bomb_time.start()
            self.bomb_once = 0
            trump_shoot_bomb_sound.play()
            if(p1):
                bom = BOMB(self.rect.center[0],self.rect.center[1],rads_1,bomb_img,dist1,x1,y1)
                enemy_bomb_sprites.add(bom)
                enemy_sprites.add(bom)
            elif(p2):
                bom = BOMB(self.rect.center[0],self.rect.center[1],rads_2,bomb_img,dist2,x2,y2)
                enemy_bomb_sprites.add(bom)
                enemy_sprites.add(bom)
            elif(p3):
                bom = BOMB(self.rect.center[0],self.rect.center[1],rads_3,bomb_img,dist3,x3,y3)
                enemy_bomb_sprites.add(bom)
                enemy_sprites.add(bom)
            elif(p4):
                bom = BOMB(self.rect.center[0],self.rect.center[1],rads_4,bomb_img,dist4,x4,y4)
                enemy_bomb_sprites.add(bom)
                enemy_sprites.add(bom)
        elif (self.bomb_time.elapsed() > 2): self.bomb_once = 1

class BOMB(pygame.sprite.Sprite):
    def __init__(self,x,y, angle, player_img_1,dis,x_loc,y_loc):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.angle = angle
        angle = self.angle * 57.3 #convert to degrees
        self.enemy_locx = x_loc
        self.enemy_locy = y_loc
        
        self.xspeed = math.cos(self.angle) * map(abs(dis),30,WIDTH,1,8) # speed of bullet is related to distance
        self.yspeed = math.sin(self.angle) * map(abs(dis),30,WIDTH,1,8)
        self.image_1 = player_img_1
        self.image = pygame.transform.rotate(self.image_1,-1 * angle)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    def update(self):
        #Out of map
        if (pygame.sprite.spritecollideany(self,player_1_sprites) or pygame.sprite.spritecollideany(self,player_2_sprites)):
            big_bomb_sound.play(0,100)
            self.kill()
        if (self.rect.bottom >= HEIGHT + 100) or (self.rect.top <= -100):
            self.kill()
        if (self.rect.right > WIDTH + 100) or (self.rect.left < -100):
            self.kill()
        self.rect.center = (self.rect.center[0] + self.xspeed, self.rect.center[1] + self.yspeed)
        print((self.rect.center[1] <= self.enemy_locy+50) and (self.rect.center[1] >= self.enemy_locy-50))
        if ((((self.rect.center[0]) <= self.enemy_locx+50) and (self.rect.center[0] >= self.enemy_locx-50)) and ((self.rect.center[1] <= self.enemy_locy+50) and (self.rect.center[1] >= self.enemy_locy-50))):
            big_bomb_sound.play(0,100)
            # create bullets in all directions
            for i in range(0,7):
                rad = (i-1) * 0.7854
                bullet = EBULLETS(self.rect.x + 45,self.rect.y + 45, rad,small_rocks_img,1)
                enemy_bullet_sprites.add(bullet)
                enemy_sprites.add(bullet)
            self.kill()


class EBULLETS(pygame.sprite.Sprite):
    def __init__(self,x,y, angle, player_img_1,damage):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.angle = angle
        self.damage = damage
        angle = self.angle * 57.3 #convert to degrees
        
        self.xspeed = math.cos(self.angle) * 19 # speed of bullet
        self.yspeed = math.sin(self.angle) * 19
        self.image_1 = player_img_1
        self.image = pygame.transform.rotate(self.image_1,-1 * angle)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        if (pygame.sprite.spritecollideany(self,player_1_sprites) or pygame.sprite.spritecollideany(self,player_2_sprites)):
            dead_sound.play()
            self.kill()
        if (self.rect.bottom >= HEIGHT + 100) or (self.rect.top <= -100):
            self.kill()
        if (self.rect.right > WIDTH + 100) or (self.rect.left < -100):
            self.kill()
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed

class SLIME(pygame.sprite.Sprite):
    def __init__(self ,x ,y ,player_img_1, player_img_2, health):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = player_img_1
        self.imageD = player_img_2
        self.imageN = self.image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.health = health
        self.time = time.clock()
        self.time_new = time.clock()
        self.x_dis = 0
        self.y_dis = 0
        self.MS = 3.5
        self.slowspeed  = self.MS * .7
        self.constMS = self.MS
    
    def update(self,x1 = None,y1 = None,x2 = None,y2 = None, x3 = None, y3 = None, x4 = None, y4 = None):
        self.time = time.clock()
        if (pygame.sprite.spritecollideany(self,bullet_sprites)):
            self.health -= 1
            self.time_new = self.time + 0.5
        if (pygame.sprite.spritecollideany(self,bulletx2_sprites)):
            self.health -= 2
            self.time_new = self.time + 0.5
                
        if (self.health <= 0): self.kill()
        
        if (self.time_new >= self.time):
            self.MS = 0
            self.image = self.imageD
        else:
            self.MS = self.constMS
            self.image = self.imageN
        
        #Following players
        #Find farthest distance
        x = 0
        y = 0
        x1_dis = x1 - self.rect.x
        y1_dis = y1 - self.rect.y
        x2_dis = x2 - self.rect.x
        y2_dis = y2 - self.rect.y
        x3_dis = x3 - self.rect.x
        y3_dis = y3 - self.rect.y
        x4_dis = x4 - self.rect.x
        y4_dis = y4 - self.rect.y
        dist1 = math.sqrt((x1_dis * x1_dis) + (y1_dis * y1_dis))
        dist2 = math.sqrt((x2_dis * x2_dis) + (y2_dis * y2_dis))
        dist3 = math.sqrt((x3_dis * x3_dis) + (y3_dis * y3_dis))
        dist4 = math.sqrt((x4_dis * x4_dis) + (y4_dis * y4_dis))
        if (pygame.sprite.spritecollideany(self,water_sprites)): self.MS = self.slowspeed
        elif(self.MS): self.MS = self.constMS
        if (pygame.sprite.spritecollideany(self,wall_sprites)): self.MS = self.slowspeed * 0.5
        elif(self.MS): self.MS = self.constMS
        
        if (dist1 <= dist2 and dist1 <= dist3 and dist1 <= dist4): #player one closer
            rads = math.atan2(y1_dis , (x1_dis))
            x = round(math.cos(rads) * self.MS)
            y = round(math.sin(rads) * self.MS)
        elif (dist2 <= dist3 and dist2 <= dist4): #plyer two closer
            rads = math.atan2(y2_dis , (x2_dis))
            x = round(math.cos(rads) * self.MS)
            y = round(math.sin(rads) * self.MS)
        elif (dist3 < dist4): #plyer three closer
            rads = math.atan2(y3_dis , (x3_dis))
            x = round(math.cos(rads) * self.MS)
            y = round(math.sin(rads) * self.MS)
        else: #plyer four closer
            rads = math.atan2(y4_dis , (x4_dis))
            x = round(math.cos(rads) * self.MS)
            y = round(math.sin(rads) * self.MS)

        self.rect.y += y
        self.rect.x += x

        #sprite detection


class FLY(pygame.sprite.Sprite):
    def __init__(self ,x ,y ,player_img_1, health):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = player_img_1
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.health = health
        self.time = time.clock()
        self.time_new = time.clock()
        self.x_dis = 0
        self.y_dis = 0

    def update(self):
        if (pygame.sprite.spritecollideany(self,bullet_sprites)): self.health -= 1
        if (pygame.sprite.spritecollideany(self,bulletx2_sprites)): self.health -= 2
        if (self.health <= 0): self.kill()
        self.time = time.clock()
        if (self.time_new <= self.time):
            self.time_new = time.clock() + (random.randint(10,40) / 10)
            self.x_dis = round(random.randint(-20,20) / 10)
            self.y_dis = round(random.randint(-20,20) / 10)
        
        self.rect.x += round(self.x_dis)
        self.rect.y += round(self.y_dis)
        if (self.rect.bottom >= HEIGHT) or (self.rect.top <= 0):
            self.rect.y -=  self.y_dis
        if (self.rect.right > WIDTH) or (self.rect.left < 0):
            self.rect.x -= self.x_dis
        #sprite detection
        if (pygame.sprite.spritecollideany(self,wall_sprites)):
            bool_y = 0
            bool_x = 0
            #Checking y
            self.rect.x -= (self.x_dis)
            if (pygame.sprite.spritecollideany(self,wall_sprites)): bool_y = 1
            self.rect.y -= (self.y_dis)
            self.rect.x += (self.x_dis)
            if (pygame.sprite.spritecollideany(self,wall_sprites)):bool_x = 1
            self.rect.y += (self.y_dis)
            if (bool_x):self.rect.x -= (self.x_dis)
            if (bool_y):self.rect.y -= (self.y_dis)

class BLOCK(pygame.sprite.Sprite):
    def __init__(self ,x ,y ,player_img_1, player_img_2, health):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = player_img_1
        self.imageD = player_img_2
        self.imageN = self.image
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.health = health
        self.time = time.clock()
        self.time_new = time.clock()
        self.x_dis = 0
        self.y_dis = 0
        self.MS = 2
        self.slowspeed  = (self.MS * .8)
        self.constMS = self.MS
    
    def update(self,x1 = None,y1 = None,x2 = None,y2 = None, x3 = None, y3 = None, x4 = None, y4 = None):
        self.time = time.clock()
        if (pygame.sprite.spritecollideany(self,bullet_sprites)):
            self.health -= 1
            self.time_new = self.time + 0.5
        if (pygame.sprite.spritecollideany(self,bulletx2_sprites)):
            self.health -= 2
            self.time_new = self.time + 0.5
                
        if (self.health <= 0): self.kill()
        
        if (self.time_new >= self.time):
            self.MS = 0
            self.image = self.imageD
        else:
            self.MS = self.constMS
            self.image = self.imageN
        
        #Following players
        #Find farthest distance
        x = 0
        y = 0
        x1_dis = x1 - self.rect.x
        y1_dis = y1 - self.rect.y
        x2_dis = x2 - self.rect.x
        y2_dis = y2 - self.rect.y
        x3_dis = x3 - self.rect.x
        y3_dis = y3 - self.rect.y
        x4_dis = x4 - self.rect.x
        y4_dis = y4 - self.rect.y
        dist1 = math.sqrt((x1_dis * x1_dis) + (y1_dis * y1_dis))
        dist2 = math.sqrt((x2_dis * x2_dis) + (y2_dis * y2_dis))
        dist3 = math.sqrt((x3_dis * x3_dis) + (y3_dis * y3_dis))
        dist4 = math.sqrt((x4_dis * x4_dis) + (y4_dis * y4_dis))
        
        if (pygame.sprite.spritecollideany(self,water_sprites)): self.MS = self.slowspeed
        elif(self.MS): self.MS = self.constMS
        
        if (dist1 <= dist2 and dist1 <= dist3 and dist1 <= dist4): #player one closer
            rads = math.atan2(y1_dis , (x1_dis))
            x = round(math.cos(rads) * self.MS)
            y = round(math.sin(rads) * self.MS)
        elif (dist2 <= dist3 and dist2 <= dist4): #plyer two closer
            rads = math.atan2(y2_dis , (x2_dis))
            x = round(math.cos(rads) * self.MS)
            y = round(math.sin(rads) * self.MS)
        elif (dist3 < dist4): #plyer three closer
            rads = math.atan2(y3_dis , (x3_dis))
            x = round(math.cos(rads) * self.MS)
            y = round(math.sin(rads) * self.MS)
        else: #plyer four closer
            rads = math.atan2(y4_dis , (x4_dis))
            x = round(math.cos(rads) * self.MS)
            y = round(math.sin(rads) * self.MS)
        
        self.rect.y += y
        self.rect.x += x
            #sprite detection
        if (pygame.sprite.spritecollideany(self,wall_sprites)):
            bool_y = 0
            bool_x = 0
            #Checking y
            self.rect.x -= (x)
            if (pygame.sprite.spritecollideany(self,wall_sprites)): bool_y = 1
            self.rect.y -= (y)
            self.rect.x += (x)
            if (pygame.sprite.spritecollideany(self,wall_sprites)):bool_x = 1
            self.rect.y += (y)
            if (bool_x):
                self.rect.x -= (x)
                if (0):
                    self.rect.y += (y / abs(y))
            if (bool_y):
                self.rect.y -= (y)
                if (0):
                    self.rect.x += (x / abs(x))

class GHOST(pygame.sprite.Sprite):
    def __init__(self ,x ,y ,player_img_1, player_img_2, health):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image1 = player_img_1
        self.image2 = player_img_2
        self.image = self.image1
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.health = health
        self.time = time.clock()
        self.time_new = 0
        self.x_dis = 0
        self.y_dis = 0
        self.MS = 3.25
        self.slowspeed  = self.MS *.7
        self.constMS = self.MS
        self.invis = 0
        self.rand_timer_1 = 0
    
    def update(self,x1 = None,y1 = None,x2 = None,y2 = None, x3 = None, y3 = None, x4 = None, y4 = None):
        if (pygame.sprite.spritecollideany(self,bullet_sprites)): self.health -= 1
        if (pygame.sprite.spritecollideany(self,bulletx2_sprites)): self.health -= 2
        if (self.health <= 0): self.kill()
        self.time = time.clock()

        #Turn invis
        if (self.time_new <= self.time):
            self.rand_timer_1 = (random.randint(90,120) / 10)
            self.time_new = self.time + self.rand_timer_1
            self.invis = 1
            self.image = self.image2
            self.MS += 0.07
        elif((self.time_new - self.rand_timer_1 + 2) >= self.time):
            self.invis = 1
            self.image = self.image2
            self.MS += 0.07
        else:
            self.MS = self.constMS
            self.invis = 0
            self.image = self.image1
        
        #Following players
        #Find farthest distance
        x = 0
        y = 0
        x1_dis = x1 - self.rect.x
        y1_dis = y1 - self.rect.y
        x2_dis = x2 - self.rect.x
        y2_dis = y2 - self.rect.y
        x3_dis = x3 - self.rect.x
        y3_dis = y3 - self.rect.y
        x4_dis = x4 - self.rect.x
        y4_dis = y4 - self.rect.y
        dist1 = math.sqrt((x1_dis * x1_dis) + (y1_dis * y1_dis))
        dist2 = math.sqrt((x2_dis * x2_dis) + (y2_dis * y2_dis))
        dist3 = math.sqrt((x3_dis * x3_dis) + (y3_dis * y3_dis))
        dist4 = math.sqrt((x4_dis * x4_dis) + (y4_dis * y4_dis))
        if (pygame.sprite.spritecollideany(self,water_sprites)): self.MS = self.slowspeed
        if (dist1 <= dist2 and dist1 <= dist3 and dist1 <= dist4): #player one closer
            rads = math.atan2(y1_dis , (x1_dis))
            x = round(math.cos(rads) * self.MS)
            y = round(math.sin(rads) * self.MS)
        elif (dist2 <= dist3 and dist2 <= dist4): #plyer two closer
            rads = math.atan2(y2_dis , (x2_dis))
            x = round(math.cos(rads) * self.MS)
            y = round(math.sin(rads) * self.MS)
        elif (dist3 < dist4): #plyer three closer
            rads = math.atan2(y3_dis , (x3_dis))
            x = round(math.cos(rads) * self.MS)
            y = round(math.sin(rads) * self.MS)
        else: #plyer four closer
            rads = math.atan2(y4_dis , (x4_dis))
            x = round(math.cos(rads) * self.MS)
            y = round(math.sin(rads) * self.MS)
        
        self.rect.y += y
        self.rect.x += x

        #sprite detection
        
        if (pygame.sprite.spritecollideany(self,wall_sprites) and not self.invis):
            bool_y = 0
            bool_x = 0
            #Checking y
            self.rect.x -= (x)
            if (pygame.sprite.spritecollideany(self,wall_sprites)): bool_y = 1
            self.rect.y -= (y)
            self.rect.x += (x)
            if (pygame.sprite.spritecollideany(self,wall_sprites)):bool_x = 1
            self.rect.y += (y)
            if (bool_x):
                self.rect.x -= (x)
                if (0):
                    self.rect.y += (y / abs(y))
            if (bool_y):
                self.rect.y -= (y)
                if (0):
                    self.rect.x += (x / abs(x))

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y, angle, player_img_1,damage):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.angle = angle
        self.damage = damage
        angle = self.angle * 57.3 #convert to degrees
        speedofbullet = 23
        if (damage == 5): speedofbullet = 60#For special
        if (damage == 4): speedofbullet = 55#For special
        self.xspeed = math.cos(self.angle) * speedofbullet # speed of bullet
        self.yspeed = math.sin(self.angle) * speedofbullet
        self.image_1 = player_img_1
        self.image = pygame.transform.rotate(self.image_1,-1 * angle)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        global points
        if (pygame.sprite.spritecollideany(self,wall_sprites)):
            self.kill()
        if (pygame.sprite.spritecollideany(self,enemy_sprites)):
            points += 1
            dead_sound.play()
            self.kill()
        if (self.rect.bottom >= HEIGHT + 100) or (self.rect.top <= -100):
                self.kill()
        if (self.rect.right > WIDTH + 100) or (self.rect.left < -100):
                self.kill()
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed

class SWORD(pygame.sprite.Sprite):
    def __init__(self,x,y, angle, player_img_1,xspeed,yspeed):
        pygame.sprite.Sprite.__init__(self)
        self.angle = angle * -57.3 #convert to degrees
        self.xspeed = round(math.cos(angle) * 10) + xspeed
        self.yspeed = round(math.sin(angle) * 10) + yspeed
        self.x = x
        self.y = y
        self.image_1 = player_img_1
        self.image = pygame.transform.rotate(self.image_1,self.angle)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.angle_speed = StopWatch()
        self.hit = 0
    
    def update(self):
        global points
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed
        self.angle += 25
        self.image = pygame.transform.rotate(self.image_1,self.angle)
        self.image.set_colorkey(BLACK)
        if (self.angle_speed.elapsed() >= 0.4): self.kill()
        if (pygame.sprite.spritecollideany(self,enemy_sprites)):
            points += 1
            hit_sword_sound.play()
            if(self.hit):
                self.kill()
            self.hit+=1

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,player_img_1,player_img_2,player_img_3,max_health,max_bullets,max_speed, regen_ammo, regen_health, ability):
        pygame.sprite.Sprite.__init__(self)
        self.ability = ability
        self.MB = max_bullets
        self.constMB = self.MB
        self.MH = max_health
        self.MS = max_speed
        self.constMS = max_speed
        self.slowspeed = max_speed * 0.5
        self.health = max_health
        self.bullets = max_bullets
        self.shoot_runonce = 1
        self.regen_ammo = regen_ammo
        self.const_regen_ammo = self.regen_ammo
        self.regen_health = regen_health
        self.time = time.clock()
        self.current_time = 0
        self.damage_time = 0
        self.ammo_accel = 0
        self.sound_1 = 1
        
        self.image_A = player_img_3
        self.image_D = player_img_2
        self.image_N = player_img_1
        self.image = self.image_N
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.regen_h = 0
        self.regen_a = 0
        self.dead = 0
        self.dash_timer = StopWatch()
        self.ability_timer = StopWatch()
        self.dash_time = 7
    
    
    def get_x(self):
        value = self.rect.x
        if (self.dash_time == 0.5): value = -5000 #for mele
        return value
    
    def get_y(self):
        value = self.rect.y
        if (self.dash_time == 0.5): value = -5000 #for mele
        return value
    
    def get_health(self):
        return self.health
    
    def get_bullets(self):
        return self.bullets
    
    def get_max_health(self):
        return self.MH
    
    def get_max_bullets(self):
        return self.MB
    
    def get_regen_bullets(self):
        return self.regen_a
    
    def set_dead(self, var):
        self.dead = var
    
    def get_regen_health(self):
        return self.regen_h
    
    def update(self, x , y, shoot_x, shoot_y, shoot, dash, ability):
        self.time = time.clock()
        #Check if alive
        if (self.health <= 0):
            self.health = self.MH
            self.kill()
            self.rect.y = -10000 #To make the enemys attack current target
            self.rect.x = -10000
            self.dead = 1
        #for regen
        if (self.rect.y == -10000 and not self.dead):
            self.rect.y = HEIGHT * 0.5
            self.rect.x = WIDTH * 0.45
        
        self.ammo_accel += 0.055
        self.regen_a += self.regen_ammo + self.ammo_accel
        self.regen_h += self.regen_health
        if ((self.regen_a >= 149)):
            if ((self.bullets < self.MB)): self.bullets += 1
            self.regen_a = 0
        if ((self.regen_h >= 149)):
            if((self.health < self.MH)): self.health += 1
            self.regen_h = 0
        if (self.bullets == self.MB and self.sound_1):
            self.sound_1 = 0
            reload_sound.play()
        if (pygame.sprite.spritecollideany(self,water_sprites)): self.MS = self.slowspeed
        else: self.MS = self.constMS
        
        if (self.dash_timer.elapsed() > self.dash_time): #Dash and button pressed
            self.image = self.image_A
            if(dash):
                self.dash_timer.start()
                dash_sound.play()
        else:
            self.image = self.image_N
        if (self.dash_timer.elapsed() <= 0.18):
            self.MS = 39
        
        x = round(self.MS * x)
        y = round(self.MS * y)
        self.rect.x += x
        self.rect.y += y
        if (self.rect.bottom >= HEIGHT) or (self.rect.top <= 0):
            self.rect.y -= y
        if (self.rect.right > WIDTH) or (self.rect.left < 0):
            self.rect.x -= x
        #sprite detection
        if (pygame.sprite.spritecollideany(self,wall_sprites)):
            bool_y = 0
            bool_x = 0
            #Checking y
            self.rect.x -= (x)
            if (pygame.sprite.spritecollideany(self,wall_sprites)): bool_y = 1
            self.rect.y -= (y)
            self.rect.x += (x)
            if (pygame.sprite.spritecollideany(self,wall_sprites)):bool_x = 1
            self.rect.y += (y)
            if (bool_x):self.rect.x -= (x)
            if (bool_y):self.rect.y -= (y)
        #For enemy sprites
        if(pygame.sprite.spritecollideany(self,enemy_sprites) and (self.damage_time < self.time)):
            self.image = self.image_D
            self.damage_time = self.time + 1.25
            hurt_sound.play()
            if(pygame.sprite.spritecollideany(self,fly_sprites)):
                self.health -= 1
            elif(pygame.sprite.spritecollideany(self,block_sprites)):
                self.health -= 2
            elif(pygame.sprite.spritecollideany(self,ghost_sprites)):
                self.health -= 2
            elif(pygame.sprite.spritecollideany(self,slime_sprites)):
                self.health -= 1
            elif(pygame.sprite.spritecollideany(self,enemy_bullet_sprites)):
                self.health -= 2
            elif (pygame.sprite.spritecollideany(self,enemy_bomb_sprites)):
                self.health -= 3
            elif (pygame.sprite.spritecollideany(self,trump_sprites)):
                self.health -= 2

        elif (self.damage_time > self.time):
            self.image = self.image_D
        rads = math.atan2(shoot_y , (shoot_x + 0.00001))
        pygame.draw.line(screen,RED, (self.rect.x + 17, self.rect.y + 17), (self.rect.x + 17 + (math.cos(rads) * 27), self.rect.y + 17 + (math.sin(rads) * 27)),2) # makes the line for shooting
        #Using ability
        global rounds
        ability_extra_shot = 0
        if (self.ability == 1): #shooter
            self.MB = self.constMB + rounds
            if (self.ability_timer.elapsed() > 30): #ability
                pygame.draw.rect(screen,BLACK,pygame.Rect(self.rect.x,self.rect.y-3,34,3),0)
                if(ability):
                    self.bullets = self.MB
                    self.ability_timer.start()
                    fire_power_sound.play()
            else:
                if (self.ability_timer.elapsed() <= 4):
                    ability_extra_shot = 1
            #shooting
            if (shoot and self.shoot_runonce and self.bullets > 0):
                self.shoot_runonce = 0
                self.bullets -= 1
                self.sound_1 = 1
                shoot_sound.play()
                #shooting bullet
                if (ability_extra_shot):
                    __bullet__ = Bullet(self.rect.x + 17,self.rect.y + 17,rads,bullet_img1,4)
                    bulletx2_sprites.add(__bullet__)
                
                else:
                    __bullet__ = Bullet(self.rect.x + 17,self.rect.y + 17,rads,bullet_img1,1)
                    bullet_sprites.add(__bullet__)
                self.ammo_accel = 0
            elif (not shoot):
                self.shoot_runonce = 1
        elif (self.ability == 2): #sword
            self.ammo_accel = 0
            self.regen_a = self.const_regen_ammo + rounds * 0.25
            self.dash_time = 4 # 5 seconds per dash
            if (self.ability_timer.elapsed() > 50): #ability
                pygame.draw.rect(screen,BLUE,pygame.Rect(self.rect.x,self.rect.y-3,34,3),0)
                if(ability):
                    self.bullets = self.MB
                    self.bullets += 12
                    self.ability_timer.start()
                    taunt_sound.play()
            else:
                if (self.ability_timer.elapsed() <= 5):
                    self.image = self.image_D
                    self.dash_time = 0.5
                    self.health = self.MH

           
            if (shoot and self.shoot_runonce and self.bullets > 0):
                self.shoot_runonce = 0
                self.bullets -= 1
                self.sound_1 = 1
                swing_sword_sound.play()
                #shooting bullet
                __bullet__ = SWORD(self.rect.x + 17,self.rect.y + 17,rads,yellow_sword_img,x,y)
                bullet_sprites.add(__bullet__)

            elif ((not shoot)):
                self.shoot_runonce = 1



def message_display(s,text,x,y): #freesansbold.ttf
    largeText = pygame.font.Font('freesansbold.ttf',s)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    screen.blit(TextSurf, TextRect)

def message_display_1(s,text,x,y,c):
    largeText = pygame.font.Font('freesansbold.ttf',s)
    TextSurf, TextRect = text_objects_1(text, largeText, c)
    TextRect.center = (x,y)
    screen.blit(TextSurf, TextRect)

def text_objects_1(text, font,c):
    textSurface = font.render(text, True, c)
    return textSurface, textSurface.get_rect()

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def buttons(s,msg,x,y,w,h,ic,ac,number_1,action = None):
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if action != None and click[0] == 1:
            action(number_1)
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",s)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def make_glitch(round):
    health = 50 + (round*20)
    dum = GLITCH_BOSS(health,glitch_ghost_img,glitch_ghost_blink_img,glitch_ghost1_img,glitch_ghost2_img,glitch_map_img)
    trump_sprites.add(dum)
    enemy_sprites.add(dum)

def make_ghost(x,y,round):
    health = 3 + round
    dum = GHOST(x,y,m1_img,m1_1_img, health)
    ghost_sprites.add(dum)
    enemy_sprites.add(dum)

def make_block(x,y,round):
    health = 4 + round
    dum = BLOCK(x,y,m3_img,m3_3_img, health)
    block_sprites.add(dum)
    enemy_sprites.add(dum)

def make_slime(x,y,round):
    health = 2 + round
    dum = SLIME(x,y,m2_img,m2_2_img, health)
    slime_sprites.add(dum)
    enemy_sprites.add(dum)

def make_fly(x,y,round):
    health = 1 + round
    dum = FLY(x,y,m4_img, health)
    fly_sprites.add(dum)
    enemy_sprites.add(dum)

def make_trump(x,y,round):
    health = 135 + ((round-1) * 50)
    dum = BOSS(x,y,trump_boss_img, health)
    trump_sprites.add(dum)
    enemy_sprites.add(dum)

def update_leaderboards():
    global wave_num, points, rounds
    message_display_1(20, (" Wave: " + str(rounds) + "." + str(wave_num)) ,WIDTH * .5, HEIGHT * .02, WHITE)
    message_display_1(20, ("Points: " + str(points)) ,WIDTH * .5, HEIGHT * .05, WHITE)

def check_controller():
    global controller_count,joystick_0,joystick_1, joystick_2, joystick_3
    message_display_1(30, "Controller disconnected" ,WIDTH * .5, HEIGHT * .5, RED)
    pygame.display.flip()
    pygame.joystick.quit()
    pygame.joystick.init()
    if ((controller_count == pygame.joystick.get_count())):
        if (controller_count == 1):
            joystick_0 = pygame.joystick.Joystick(0)
            joystick_0.init()
        elif (controller_count == 2):
            joystick_0 = pygame.joystick.Joystick(0)
            joystick_0.init()
            joystick_1 = pygame.joystick.Joystick(1)
            joystick_1.init()
        elif (controller_count == 3):
            joystick_0 = pygame.joystick.Joystick(0)
            joystick_0.init()
            joystick_1 = pygame.joystick.Joystick(1)
            joystick_1.init()
            joystick_2 = pygame.joystick.Joystick(2)
            joystick_2.init()
        elif (controller_count == 4):
            joystick_0 = pygame.joystick.Joystick(0)
            joystick_0.init()
            joystick_1 = pygame.joystick.Joystick(1)
            joystick_1.init()
            joystick_3 = pygame.joystick.Joystick(3)
            joystick_3.init()
    if(controller_count == 4 and joystick_0.get_init() and joystick_1.get_init() and joystick_2.get_init() and joystick_3.get_init()):return
    elif(controller_count == 3 and joystick_0.get_init() and joystick_1.get_init() and joystick_2.get_init()): return
    elif(controller_count == 2 and joystick_0.get_init() and joystick_1.get_init()): return
    elif(controller_count == 1 and joystick_0.get_init()): return
    check_controller()

class StopWatch:
    def __init__(self):
        self.start()
    def start(self):
        self._startTime = time.time()
    def getStartTime(self):
        return self._startTime
    def elapsed(self, prec=2):
        prec = 1
        diff= time.time() - self._startTime
        return round(diff + 0.1, prec)
def round(n, p=0):
    m = 10 ** p
    return math.floor(n * m + 0.5) / m

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;


#Game_functions
def create_map():
    global MAP, wall_img, player_2, player_1, points, enemy_timer, player_3, player_4
    enemy_timer.start()
    #make_glitch(0)
    y = 0
    points = 0
    try:
        UI_function(player_1.get_max_health(), player_1.get_max_bullets(), player_2.get_max_health(), player_2.get_max_bullets(),player_3.get_max_health(), player_3.get_max_bullets(),player_4.get_max_health(), player_4.get_max_bullets())
    except:
        try:
            UI_function(player_1.get_max_health(), player_1.get_max_bullets(),player_2.get_max_health(), player_2.get_max_bullets(), player_3.get_max_health(), player_3.get_max_bullets(), 0, 0)
        except:
            try:
                UI_function(player_1.get_max_health(), player_1.get_max_bullets(),player_2.get_max_health(), player_2.get_max_bullets(), 0, 0, 0, 0)
            except:
                try:
                    UI_function(player_1.get_max_health(), player_1.get_max_bullets(),0, 0, 0, 0, 0, 0)
                except:
                    try:
                        UI_function(0, 0, 0, 0, 0, 0, 0, 0)
                    except:
                        print("UI Error")
    #Both rect are for regen HP and Ammo
    for column in MAP:
        x = -8
        y += 16
        for row in column:
            x +=16
            if (row == 1):
                temp_wall = wall(x,y,wall_img)
                wall_sprites.add(temp_wall)
            if (row == 2):
                temp_wall = wall(x,y,water_img)
                water_sprites.add(temp_wall)

def level_place_add(value):
    global location
    location += 1

def start_menu():
    global p1_runonce, p2_runonce,p3_runonce,p4_runonce,joystick_0, joystick_1, controller_count, joystick_2, joystick_3
    screen.blit(Start_BackGround.image, Start_BackGround.rect)
    message_display_1(40, "Welcome to the shooting game brah",WIDTH * .5, HEIGHT * .2, WHITE)
    message_display_1(20, "Press start to continue",WIDTH * .5, HEIGHT * .8, WHITE)
    buttons(18, 'Start Game', WIDTH * .7, HEIGHT*.1, 121, 35,PEACH_2,PEACH_1,1,level_place_add)
    if(round(time.time(),2)*10 % 10 == 0):
        pygame.joystick.quit()
        pygame.joystick.init()
    try:
        joystick_0 = pygame.joystick.Joystick(0)
    except:
        print("P1 Not init")
    try:
        joystick_1 = pygame.joystick.Joystick(1)
    except:
        print("P2 Not init")
    try:
        joystick_2 = pygame.joystick.Joystick(2)
    except:
        print("P3 Not init")
    try:
        joystick_3 = pygame.joystick.Joystick(3)
    except:
        print("P4 Not init")
    try:
        joystick_0.init()
        if (joystick_0.get_init()):
            if (joystick_0.get_button(1)): level_place_add(1)#start game
            message_display_1(20, "Player one connected",WIDTH * .2, HEIGHT * .5, GREEN)
            message_display_1(12, "Stats:",WIDTH * .2, HEIGHT * .55, GREEN)
            message_display_1(12, "Special: Life Steal",WIDTH * .2, HEIGHT * .575, GREEN)
            message_display_1(12, "Health: 6",WIDTH * .2, HEIGHT * .6, GREEN)
            message_display_1(12, "Bullets: 4",WIDTH * .2, HEIGHT * .625, GREEN)
            message_display_1(12, "Speed: 5",WIDTH * .2, HEIGHT * .65, GREEN)
            if (p1_runonce == 1):# (self,x,y,player_img_1,player_img_2,max_health,max_bullets,max_speed, regen_ammo, regen_health,ability):
                global player_1
                controller_count+=1
                player_1 = Player(WIDTH * .35, HEIGHT * .5, p1_img, p1d_img,p1a_img, 6, 6, 4.5, 0.7, 0.2,1)
    
                player_1_sprites.add(player_1)
                p1_runonce = 0
            
    except:
        pygame.joystick.init()
        message_display_1(20, "Player one NOT connected",WIDTH * .2, HEIGHT * .5, RED)
    try:
        joystick_1.init()
        if (joystick_1.get_init()) :
            if (joystick_1.get_button(1)): level_place_add(1)#start game
            message_display_1(20, "Player two connected",WIDTH * .2, HEIGHT * .4, GREEN)
            message_display_1(12, "Stats:",WIDTH * .2, HEIGHT * .25, GREEN)
            message_display_1(12, "Special: Dash",WIDTH * .2, HEIGHT * .275, GREEN)
            message_display_1(12, "Health: 3",WIDTH * .2, HEIGHT * .3, GREEN)
            message_display_1(12, "Bullets: 5",WIDTH * .2, HEIGHT * .325, GREEN)
            message_display_1(12, "Speed: 4",WIDTH * .2, HEIGHT * .35, GREEN)
            if (p2_runonce == 1):
                global player_2
                controller_count+=1
                player_2 = Player(WIDTH * .35, HEIGHT * .4, p2_img, p2d_img,p2a_img, 4, 4, 5.5, 3, 0.35,2)
                player_2_sprites.add(player_2)
                p2_runonce = 0
    except:
        pygame.joystick.init()
        message_display_1(20, "Player two NOT connected",WIDTH * .2, HEIGHT * .4, RED)
    try:
        joystick_2.init()
        if (joystick_2.get_init()) :# (self,x,y,player_img_1,player_img_2,max_health,max_bullets,max_speed, regen_ammo, regen_health,ability):
            if (joystick_2.get_button(1)): level_place_add(1)#start game
            message_display_1(20, "Player three connected",WIDTH * .6, HEIGHT * .4, GREEN)
            message_display_1(12, "Stats:",WIDTH * .6, HEIGHT * .25, GREEN)
            message_display_1(12, "Special: Dash",WIDTH * .6, HEIGHT * .275, GREEN)
            message_display_1(12, "Health: 3",WIDTH * .6, HEIGHT * .3, GREEN)
            message_display_1(12, "Bullets: 5",WIDTH * .6, HEIGHT * .325, GREEN)
            message_display_1(12, "Speed: 4",WIDTH * .6, HEIGHT * .35, GREEN)
            if (p3_runonce == 1):
                global player_3
                controller_count+=1
                player_3 = Player(WIDTH * .35, HEIGHT * .5, p1_img, p1d_img,p1a_img, 6, 6, 6, 0.7, 0.2,1)
                player_3_sprites.add(player_3)
                p3_runonce = 0
    except:
        pygame.joystick.init()
        message_display_1(20, "Player three NOT connected",WIDTH * .6, HEIGHT * .4, RED)
    try:
        joystick_3.init()
        if (joystick_3.get_init()) :
            if (joystick_3.get_button(1)): level_place_add(1)#start game
            message_display_1(20, "Player three connected",WIDTH * .6, HEIGHT * .5, GREEN)
            message_display_1(12, "Stats:",WIDTH * .6, HEIGHT * .55, GREEN)
            message_display_1(12, "Special: Dash",WIDTH * .6, HEIGHT * .575, GREEN)
            message_display_1(12, "Health: 3",WIDTH * .6, HEIGHT * .6, GREEN)
            message_display_1(12, "Bullets: 5",WIDTH * .6, HEIGHT * .625, GREEN)
            message_display_1(12, "Speed: 4",WIDTH * .6, HEIGHT * .65, GREEN)
            if (p4_runonce == 1):
                global player_4, HARD_MODE
                HARD_MODE = 1
                controller_count+=1
                player_4 = Player(WIDTH * .35, HEIGHT * .4, p2_img, p2d_img,p2a_img, 4, 4, 6, 3, 0.35,2)
                player_4_sprites.add(player_4)
                p4_runonce = 0
    except:
        pygame.joystick.init()
        message_display_1(20, "Player four NOT connected",WIDTH * .6, HEIGHT * .5, RED)

def random_enemy_creater():
    global enemy_timer
    if(enemy_timer < (time.clock() - random.randint(30,90)/10)):
        enemy_timer = time.clock()
        x = random.randint(1,4)
        if (x == 1):          make_ghost(random.randint(100,WIDTH),random.randint(100,HEIGHT),round(enemy_timer / 50))

        elif (x == 2):        make_slime(random.randint(100,WIDTH),random.randint(100,HEIGHT),round(enemy_timer / 50))

        elif (x == 3):        make_block(random.randint(100,WIDTH),random.randint(100,HEIGHT),round(enemy_timer / 50))
    
        elif (x == 4):        make_fly(random.randint(100,WIDTH),random.randint(100,HEIGHT),round(enemy_timer / 50))

def boss_enemy_creater(time, frequency,do_once):
    if((round(time) % frequency) == 0):
        global rounds, HARD_MODE
        trump_call_enemys_sound.play()
        x = random.randint(1,2)
        if (x == 1 and do_once):
            make_ghost(random.randint(0,WIDTH),0,rounds -1 + HARD_MODE)
            make_ghost(0,random.randint(0,HEIGHT),rounds - 1 + HARD_MODE)
            make_ghost(WIDTH,random.randint(0,HEIGHT),rounds -1 + HARD_MODE)
            make_ghost(random.randint(0,WIDTH),HEIGHT,rounds - 1 + HARD_MODE)
        elif (x == 2 and do_once):
            make_slime(random.randint(0,WIDTH),0,rounds - 1 + HARD_MODE)
            make_slime(0,random.randint(0,HEIGHT),rounds - 1 + HARD_MODE)
            make_slime(WIDTH,random.randint(0,HEIGHT),rounds - 1 + HARD_MODE)
            make_slime(random.randint(0,WIDTH),HEIGHT,rounds - 1 + HARD_MODE)
        return 0
    else:
        return 1


def enemy_creater(list_1):
    global enemy_timer, wave_num, max_time, rounds, player_1, player_2, HARD_MODE
    if (not(len(enemy_sprites)) and (enemy_timer.elapsed() > list_1[wave_num][len(list_1[wave_num]) - 1][2])):
        wave_num += 1
        if (wave_num == 10):
            wave_num = 0
            rounds += 1
            for n in range(0,9):
                for i in range(0,len(list_1[n])):
                    list_1[n][i][4] = 1
        try:
            if (not len(player_1_sprites)):
                player_1_sprites.add(player_1)
                player_1.set_dead(0)
            if (not len(player_2_sprites)):
                player_2_sprites.add(player_2)
                player_2.set_dead(0)
        except:pass
            
        enemy_timer.start()
        next_wave_sound.play()
        print("New round")
    for i in range(0,len(list_1[wave_num])):
        if (((list_1[wave_num][i][2]) < enemy_timer.elapsed() + 5) and list_1[wave_num][i][4]):
            list_1[wave_num][i][4] = 0
            if (list_1[wave_num][i][3] == 0):
                make_fly(list_1[wave_num][i][0],list_1[wave_num][i][1],rounds + HARD_MODE)
            elif (list_1[wave_num][i][3] == 1):
                make_block(list_1[wave_num][i][0],list_1[wave_num][i][1],rounds + HARD_MODE)
            elif (list_1[wave_num][i][3] == 2):
                make_slime(list_1[wave_num][i][0],list_1[wave_num][i][1],rounds + HARD_MODE)
            elif (list_1[wave_num][i][3] == 3):
                make_ghost(list_1[wave_num][i][0],list_1[wave_num][i][1],rounds + HARD_MODE)
            elif (list_1[wave_num][i][3] == 4):
                make_trump(list_1[wave_num][i][0],list_1[wave_num][i][1],rounds+ HARD_MODE)


def level_1():
    global map_runonce, player_4 ,player_3,player_2, player_1, joystick_0, joystick_1, waves, joystick_2, joystick_3
    if (map_runonce):
        next_wave_sound.play()
        map_runonce = 0
        create_map()
    enemy_creater(waves)
    screen.blit(l1_BackGround.image, l1_BackGround.rect)
    """ For raspbrry pi
try:
    if (joystick_0.get_axis(0) == -1 and joystick_0.get_axis(1) == -1 and joystick_0.get_axis(2) == -1 and joystick_0.get_axis(5) == -1):check_controller() #check controller  #
    dash = 0
        fire = 0
        special = joystick_0.get_button(1)
        if (joystick_0.get_axis(4) > 0):
            fire = 1
    if (joystick_0.get_axis(3) > 0):
        dash = 1
        player_1_sprites.update(joystick_0.get_axis(0),joystick_0.get_axis(1),joystick_0.get_axis(2),joystick_0.get_axis(5),fire,dash,special)

except:
    print("Player 1 not connected")
    """
    try:
        if (joystick_0.get_axis(0) == -1 and joystick_0.get_axis(1) == -1 and joystick_0.get_axis(2) == -1 and joystick_0.get_axis(3) == -1):check_controller() #check controller  #
        dash = 0
        fire = 0
        special = joystick_0.get_button(1)
        if (joystick_0.get_axis(5) > 0):
            fire = 1
        if (joystick_0.get_axis(4) > 0):
            dash = 1
        player_1_sprites.update(joystick_0.get_axis(0),joystick_0.get_axis(1),joystick_0.get_axis(2),joystick_0.get_axis(3),fire,dash,special)
    
    except:
        print("Player 1 not connected")

    try:
        if (joystick_1.get_axis(0) == -1 and joystick_1.get_axis(1) == -1 and joystick_1.get_axis(2) == -1 and joystick_1.get_axis(3) == -1):check_controller() #check controller
        fire = 0
        dash = 0
        special = joystick_1.get_button(1)
        if (joystick_1.get_axis(5) > 0):
            fire = 1
        if (joystick_1.get_axis(4) > 0):
            dash = 1
        player_2_sprites.update(joystick_1.get_axis(0),joystick_1.get_axis(1),joystick_1.get_axis(2),joystick_1.get_axis(3),fire,dash,special)
    except:
        print("Player 2 Not connected")

    try:
        if (joystick_2.get_axis(0) == -1 and joystick_2.get_axis(1) == -1 and joystick_2.get_axis(2) == -1 and joystick_2.get_axis(3) == -1):check_controller() #check controller
        fire = 0
        dash = 0
        special = joystick_2.get_button(1)
        if (joystick_2.get_axis(5) > 0):
            fire = 1
        if (joystick_2.get_axis(4) > 0):
            dash = 1
        player_3_sprites.update(joystick_2.get_axis(0),joystick_2.get_axis(1),joystick_2.get_axis(2),joystick_2.get_axis(3),fire,dash,special)
    except:
        print("Player 3 Not connected")

    try:
        if (joystick_3.get_axis(0) == -1 and joystick_3.get_axis(1) == -1 and joystick_3.get_axis(2) == -1 and joystick_3.get_axis(3) == -1):check_controller() #check controller
        fire = 0
        dash = 0
        special = joystick_3.get_button(1)
        if (joystick_3.get_axis(5) > 0):
            fire = 1
        if (joystick_3.get_axis(4) > 0):
            dash = 1
        player_4_sprites.update(joystick_3.get_axis(0),joystick_3.get_axis(1),joystick_3.get_axis(2),joystick_3.get_axis(3),fire,dash,special)
    except:
            print("Player 4 Not connected")

    fly_sprites.update()
    try:
        trump_sprites.update(player_1.get_x(),player_1.get_y(),player_2.get_x(),player_2.get_y(),player_3.get_x(),player_3.get_y(),player_4.get_x(),player_4.get_y())
        block_sprites.update(player_1.get_x(), player_1.get_y(), player_2.get_x(), player_2.get_y(),player_3.get_x(),player_3.get_y(),player_4.get_x(),player_4.get_y())
        ghost_sprites.update(player_1.get_x(), player_1.get_y(), player_2.get_x(), player_2.get_y(),player_3.get_x(),player_3.get_y(),player_4.get_x(),player_4.get_y())
        slime_sprites.update(player_1.get_x(), player_1.get_y(), player_2.get_x(), player_2.get_y(),player_3.get_x(),player_3.get_y(),player_4.get_x(),player_4.get_y())
        UI_HP1_sprites.update(player_1.get_health())
        UI_AP1_sprites.update(player_1.get_bullets())
        UI_HP2_sprites.update(player_2.get_health())
        UI_AP2_sprites.update(player_2.get_bullets())
        UI_HP3_sprites.update(player_3.get_health())
        UI_AP3_sprites.update(player_3.get_bullets())
        UI_HP4_sprites.update(player_4.get_health())
        UI_AP4_sprites.update(player_4.get_bullets())
        #Regen
        pygame.draw.rect(screen,RED,pygame.Rect(8,36,150,9),1)
        pygame.draw.rect(screen,PEACH_1,pygame.Rect(8,46,150,9),1)
        pygame.draw.rect(screen,RED,pygame.Rect(9,36,player_1.get_regen_health(),9),0) # 149
        pygame.draw.rect(screen,PEACH_1,pygame.Rect(9,46,player_1.get_regen_bullets(),9),0)

        pygame.draw.rect(screen,RED,pygame.Rect(866,36,150,9),1)
        pygame.draw.rect(screen,PEACH_1,pygame.Rect(866,46,150,9),1)
        pygame.draw.rect(screen,RED,pygame.Rect(866,36,player_4.get_regen_health(),9),0) # 149
        pygame.draw.rect(screen,PEACH_1,pygame.Rect(866,46,player_4.get_regen_bullets(),9),0)
        
        pygame.draw.rect(screen,RED,pygame.Rect(666,36,150,9),1)
        pygame.draw.rect(screen,PEACH_1,pygame.Rect(666,46,150,9),1)
        pygame.draw.rect(screen,RED,pygame.Rect(666,36,player_3.get_regen_health(),9),0) # 149
        pygame.draw.rect(screen,PEACH_1,pygame.Rect(666,46,player_3.get_regen_bullets(),9),0)
        
        pygame.draw.rect(screen,RED,pygame.Rect(208,36,150,9),1)
        pygame.draw.rect(screen,PEACH_1,pygame.Rect(208,46,150,9),1)
        pygame.draw.rect(screen,RED,pygame.Rect(208,36,player_2.get_regen_health(),9),0) # 149
        pygame.draw.rect(screen,PEACH_1,pygame.Rect(208,46,player_2.get_regen_bullets(),9),0)


    except:
        try:
            trump_sprites.update(player_1.get_x(),player_1.get_y(),player_2.get_x(),player_2.get_y(),player_3.get_x(),player_3.get_y(),-10000,-10000)
            block_sprites.update(player_1.get_x(), player_1.get_y(), player_2.get_x(), player_2.get_y(),player_3.get_x(),player_3.get_y(),-10000,-10000)
            ghost_sprites.update(player_1.get_x(), player_1.get_y(), player_2.get_x(), player_2.get_y(),player_3.get_x(),player_3.get_y(),-10000,-10000)
            slime_sprites.update(player_1.get_x(), player_1.get_y(), player_2.get_x(), player_2.get_y(),player_3.get_x(),player_3.get_y(),-10000,-10000)
            UI_HP1_sprites.update(player_1.get_health())
            UI_AP1_sprites.update(player_1.get_bullets())
            UI_HP2_sprites.update(player_2.get_health())
            UI_AP2_sprites.update(player_2.get_bullets())
            UI_HP3_sprites.update(player_3.get_health())
            UI_AP3_sprites.update(player_3.get_bullets())
            #Regen
            pygame.draw.rect(screen,RED,pygame.Rect(8,36,150,9),1)
            pygame.draw.rect(screen,PEACH_1,pygame.Rect(8,46,150,9),1)
            pygame.draw.rect(screen,RED,pygame.Rect(9,36,player_1.get_regen_health(),9),0) # 149
            pygame.draw.rect(screen,PEACH_1,pygame.Rect(9,46,player_1.get_regen_bullets(),9),0)

            pygame.draw.rect(screen,RED,pygame.Rect(666,36,150,9),1)
            pygame.draw.rect(screen,PEACH_1,pygame.Rect(666,46,150,9),1)
            pygame.draw.rect(screen,RED,pygame.Rect(666,36,player_3.get_regen_health(),9),0) # 149
            pygame.draw.rect(screen,PEACH_1,pygame.Rect(666,46,player_3.get_regen_bullets(),9),0)
        
            pygame.draw.rect(screen,RED,pygame.Rect(208,36,150,9),1)
            pygame.draw.rect(screen,PEACH_1,pygame.Rect(208,46,150,9),1)
            pygame.draw.rect(screen,RED,pygame.Rect(208,36,player_2.get_regen_health(),9),0) # 149
            pygame.draw.rect(screen,PEACH_1,pygame.Rect(208,46,player_2.get_regen_bullets(),9),0)
        except:
            try:
                trump_sprites.update(player_1.get_x(),player_1.get_y(),player_2.get_x(),player_2.get_y(),-10000,-10000,-10000,-10000)
                block_sprites.update(player_1.get_x(), player_1.get_y(), player_2.get_x(), player_2.get_y(),-10000,-10000,-10000,-10000)
                ghost_sprites.update(player_1.get_x(), player_1.get_y(), player_2.get_x(), player_2.get_y(),-10000,-10000,-10000,-10000)
                slime_sprites.update(player_1.get_x(), player_1.get_y(), player_2.get_x(), player_2.get_y(),-10000,-10000,-10000,-10000)
                UI_HP1_sprites.update(player_1.get_health())
                UI_AP1_sprites.update(player_1.get_bullets())
                UI_HP2_sprites.update(player_2.get_health())
                UI_AP2_sprites.update(player_2.get_bullets())
                #Regen
                pygame.draw.rect(screen,RED,pygame.Rect(8,36,150,9),1)
                pygame.draw.rect(screen,PEACH_1,pygame.Rect(8,46,150,9),1)
                pygame.draw.rect(screen,RED,pygame.Rect(9,36,player_1.get_regen_health(),9),0) # 149
                pygame.draw.rect(screen,PEACH_1,pygame.Rect(9,46,player_1.get_regen_bullets(),9),0)

                pygame.draw.rect(screen,RED,pygame.Rect(208,36,150,9),1)
                pygame.draw.rect(screen,PEACH_1,pygame.Rect(208,46,150,9),1)
                pygame.draw.rect(screen,RED,pygame.Rect(208,36,player_2.get_regen_health(),9),0) # 149
                pygame.draw.rect(screen,PEACH_1,pygame.Rect(208,46,player_2.get_regen_bullets(),9),0)
            except:
                try:
                    print("here")
                    trump_sprites.update(player_1.get_x(),player_1.get_y(),-10000,-10000,-10000,-10000,-10000,-10000)
                    block_sprites.update(player_1.get_x(), player_1.get_y(), -10000, -10000,-10000,-10000,-10000,-10000)
                    ghost_sprites.update(player_1.get_x(), player_1.get_y(), -10000, -10000,-10000,-10000,-10000,-10000)
                    slime_sprites.update(player_1.get_x(), player_1.get_y(), -10000, -10000,-10000,-10000,-10000,-10000)
                    UI_HP1_sprites.update(player_1.get_health())
                    UI_AP1_sprites.update(player_1.get_bullets())
                    #Regen
                    print(player_1.get_regen_health())
                    pygame.draw.rect(screen,RED,pygame.Rect(8,36,150,9),1)
                    pygame.draw.rect(screen,PEACH_1,pygame.Rect(8,46,150,9),1)
                    pygame.draw.rect(screen,RED,pygame.Rect(9,36,player_1.get_regen_health(),9),0) # 149
                    pygame.draw.rect(screen,PEACH_1,pygame.Rect(9,46,player_1.get_regen_bullets(),9),0)
                except:
                    print("No players playing")
                        #trump_sprites.update(player_1.get_x(),player_1.get_y(),-10000,-10000,-10000,-10000,-10000,-10000)

    enemy_bomb_sprites.update()
    bullet_sprites.update()
    bulletx2_sprites.update()
    enemy_bullet_sprites.update()
    update_leaderboards()

def level_2():
    screen.blit(l2_BackGround.image, l2_BackGround.rect)


# setup
Start_BackGround = Background(os.path.join(location,'front_screen.bmp'), [0,0])
l1_BackGround = Background(os.path.join(location,'level_1.bmp'), [0,0])
l2_BackGround = Background(os.path.join(location,'level_2.bmp'), [0,0])
#players
p1_img = pygame.image.load(os.path.join(location,'chick.bmp')).convert()
p2_img = pygame.image.load(os.path.join(location,'owl.bmp')).convert()
p1d_img = pygame.image.load(os.path.join(location,'chick_d.bmp')).convert()
p2d_img = pygame.image.load(os.path.join(location,'owl_d.bmp')).convert()
p1a_img = pygame.image.load(os.path.join(location,'owl_A.bmp')).convert()
p2a_img = pygame.image.load(os.path.join(location,'chick_A.bmp')).convert()
p3_img = pygame.image.load(os.path.join(location,'frog.bmp')).convert()
p3d_img = pygame.image.load(os.path.join(location,'frog_d.bmp')).convert()
p3a_img = pygame.image.load(os.path.join(location,'frog_A.bmp')).convert()
p4_img = pygame.image.load(os.path.join(location,'parrot.bmp')).convert()
p4d_img = pygame.image.load(os.path.join(location,'parrot_d.bmp')).convert()
p4a_img = pygame.image.load(os.path.join(location,'parrot_A.bmp')).convert()

#monsters
m1_img = pygame.image.load(os.path.join(location,'ghost.bmp')).convert()
m1_1_img = pygame.image.load(os.path.join(location,'ghost_d.bmp')).convert()
m2_img = pygame.image.load(os.path.join(location,'slimeBlock.bmp')).convert()
m2_2_img = pygame.image.load(os.path.join(location,'slimeBlockD.bmp')).convert()
m3_img = pygame.image.load(os.path.join(location,'grassBlock.bmp')).convert()
m3_3_img = pygame.image.load(os.path.join(location,'grassBlockD.bmp')).convert()
m4_img = pygame.image.load(os.path.join(location,'fly.bmp')).convert()
trump_boss_img = pygame.image.load(os.path.join(location,'trump_face.bmp')).convert()
#walls
wall_img = pygame.image.load(os.path.join(location,'wall_1.bmp')).convert()
water_img = pygame.image.load(os.path.join(location,'water.bmp')).convert()
#weapons
yellow_sword_img = pygame.image.load(os.path.join(location,'yellow_sword.bmp')).convert()
#bullets
bullet_img1 = pygame.image.load(os.path.join(location,'bullet.bmp')).convert()
bullet_img2 = pygame.image.load(os.path.join(location,'bullet_1.bmp')).convert()
small_rocks_img = pygame.image.load(os.path.join(location,'small_rock.bmp')).convert()
bomb_img = pygame.image.load(os.path.join(location,'trump_bomb.bmp')).convert()
#UI
ammo_img = pygame.image.load(os.path.join(location,'ammo.bmp')).convert()
hp_img = pygame.image.load(os.path.join(location,'health.bmp')).convert()
#Sounds
hit_sword_sound = pygame.mixer.Sound(os.path.join(sounds,'hit_sword.wav'))
swing_sword_sound = pygame.mixer.Sound(os.path.join(sounds,'swing_sword.wav'))
taunt_sound = pygame.mixer.Sound(os.path.join(sounds,'taunt_enemy.wav'))
shoot_sound = pygame.mixer.Sound(os.path.join(sounds,'shoot.wav'))
next_wave_sound = pygame.mixer.Sound(os.path.join(sounds,'nextwave.wav'))
dead_sound = pygame.mixer.Sound(os.path.join(sounds,'dead.wav'))
hurt_sound = pygame.mixer.Sound(os.path.join(sounds,'hurt.wav'))
reload_sound = pygame.mixer.Sound(os.path.join(sounds,'reload.wav'))
dash_sound = pygame.mixer.Sound(os.path.join(sounds,'dash.wav'))
ability_ready_sound = pygame.mixer.Sound(os.path.join(sounds,'ability_ready.wav')) # Thi is actually for dash ready
fire_power_sound = pygame.mixer.Sound(os.path.join(sounds,'ability_ready.wav'))
#Trump sounds
big_bomb_sound = pygame.mixer.Sound(os.path.join(sounds,'audio_hero_ExplosionSmall_DIGIJ02_24_351.wav'))
trump_enter_sound = pygame.mixer.Sound(os.path.join(sounds,'i_want_to_make_our_country_great_again.wav'))
trump_dead_sound = pygame.mixer.Sound(os.path.join(sounds,'whats_going_on.wav'))
trump_hurt1_sound = pygame.mixer.Sound(os.path.join(sounds,'china.wav'))
trump_hurt2_sound = pygame.mixer.Sound(os.path.join(sounds,'i_actually_enjoy_that.wav'))
trump_hurt3_sound = pygame.mixer.Sound(os.path.join(sounds,'im_enjoying_it.wav'))
trump_call_enemys_sound = pygame.mixer.Sound(os.path.join(sounds,'terrorists_coming_from_the_middle_east.wav'))
trump_shoot_bomb_sound = pygame.mixer.Sound(os.path.join(sounds,'we_have_to_unleash_it.wav'))
trump_shoot_bullets_sound = pygame.mixer.Sound(os.path.join(sounds,"audio_hero_ExplosionSmall_DIGIJ02_24_351.wav"))
#Boss ghost img
glitch_ghost_img = pygame.image.load(os.path.join(location,'glitch_ghost.bmp')).convert()
glitch_ghost_blink_img = pygame.image.load(os.path.join(location,'glitch_ghost_blink.bmp')).convert()
glitch_ghost1_img = pygame.image.load(os.path.join(location,'glitch_ghost_colored.bmp')).convert()
glitch_ghost2_img = pygame.image.load(os.path.join(location,'glitch_ghost_side.bmp')).convert()
glitch_map_img = pygame.image.load(os.path.join(location,'glitch_level_1.bmp')).convert()

#Boss ghost sounds
background_horror_sound = pygame.mixer.Sound(os.path.join(sounds,'background_horror.wav'))
take_control_player_sound = pygame.mixer.Sound(os.path.join(sounds,'take_control_player10s.wav'))
glitching_out_sound = pygame.mixer.Sound(os.path.join(sounds,'glitchingout.wav'))
change_map_sound = pygame.mixer.Sound(os.path.join(sounds,'changemap5.9s.wav'))
tele_behind_sound = pygame.mixer.Sound(os.path.join(sounds,'tele_behind.wav'))

location = 0 #Start in menu
p1_runonce = 1
p2_runonce = 1
p3_runonce = 1
p4_runonce = 1
map_runonce = 1
points = 0
wave_num = 1
rounds = 0
HARD_MODE = 0
enemy_timer = StopWatch()
max_time = 30
controller_count = 0
def main(running):
    # Process input (events)
    # Update
    # Render (draw)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = 0
        clock.tick(FPS)
        if (location == 0) : start_menu()
        if (location == 1) : level_1()
        if (location == 2) : level_2()
        
        enemy_sprites.draw(screen)
        player_1_sprites.draw(screen)
        player_2_sprites.draw(screen)
        player_3_sprites.draw(screen)
        player_4_sprites.draw(screen)
        wall_sprites.draw(screen)
        water_sprites.draw(screen)
        bullet_sprites.draw(screen)
        bulletx2_sprites.draw(screen)
        enemy_bomb_sprites.draw(screen)
        enemy_bullet_sprites.draw(screen)
        UI_HP1_sprites.draw(screen)
        UI_AP1_sprites.draw(screen)
        UI_HP2_sprites.draw(screen)
        UI_AP2_sprites.draw(screen)
        UI_HP3_sprites.draw(screen)
        UI_AP3_sprites.draw(screen)
        UI_HP4_sprites.draw(screen)
        UI_AP4_sprites.draw(screen)
        
        pygame.display.flip()


main(1);























