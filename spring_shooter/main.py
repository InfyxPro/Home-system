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

# Setup 64X47
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
# enemy: slime = 2 ghost = 3 fly = 0 block = 1
waves = [WIDTH * .5,HEIGHT * .6,3,1,1],[WIDTH * 0.5,HEIGHT * 0.8,4,2,1],[WIDTH * 0.6,HEIGHT * 0.5,5,1,1],[WIDTH * 0.5,HEIGHT * 0.3,6,0,1],[WIDTH * 0.6,HEIGHT * 0.7,7,3,1],[WIDTH * 0.8,HEIGHT * 0.8,8,0,1],[WIDTH * 0.5,HEIGHT * 0.5,9,0,1],[WIDTH * 0.5,HEIGHT * 0.2,10,0,1],[WIDTH * 0.5,HEIGHT * 0.2,11,0,1],[WIDTH * 0.5,HEIGHT * 0.2,12,0,1],[WIDTH * 0.5,HEIGHT * 0.2,13,0,1],[WIDTH * 0.5,HEIGHT * 0.2,13,0,1],[WIDTH * 0.5,HEIGHT * 0.2,14,0,1],[WIDTH * 0.5,HEIGHT * 0.2,15,0,1],[WIDTH * 0.5,HEIGHT * 0.2,16,0,1]


game_folder = os.path.dirname(__file__)
location = os.path.join(game_folder, "pic_bmp")

pygame.init()
pygame.joystick.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('"Bang!"')
clock = pygame.time.Clock()
player_1_sprites = pygame.sprite.Group()
player_2_sprites = pygame.sprite.Group()

ghost_sprites = pygame.sprite.Group()
block_sprites = pygame.sprite.Group()
slime_sprites = pygame.sprite.Group()
fly_sprites = pygame.sprite.Group()
enemy_sprites = pygame.sprite.Group()

wall_sprites = pygame.sprite.Group()
water_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()

UI_HP1_sprites = pygame.sprite.Group()
UI_HP2_sprites = pygame.sprite.Group()
UI_AP1_sprites = pygame.sprite.Group()
UI_AP2_sprites = pygame.sprite.Group()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PEACH_1 = (205,175,149)
PEACH_2 = (255,218,185)


# Functions

def UI_function(H1 = None, A1 = None, H2 = None, A2 = None):
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
    for i in range(0,H2):
        V = __UI__(x,y,hp_img,i)
        UI_HP2_sprites.add(V)
        x -= 20

    x = 1000
    y = 21
    for i in range(0,A2):
        V = __UI__(x,y,ammo_img,i)
        UI_AP2_sprites.add(V)
        x -= 20


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
    
    def update(self,x1 = None,y1 = None,x2 = None,y2 = None):
        self.time = time.clock()
        if (pygame.sprite.spritecollideany(self,bullet_sprites)):
            self.health -= 1
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
        dist1 = math.sqrt((x1_dis * x1_dis) + (y1_dis * y1_dis))
        dist2 = math.sqrt((x2_dis * x2_dis) + (y2_dis * y2_dis))
        if (pygame.sprite.spritecollideany(self,water_sprites)): self.MS = self.slowspeed
        elif(self.MS): self.MS = self.constMS
        if (pygame.sprite.spritecollideany(self,wall_sprites)): self.MS = self.slowspeed * 0.7
        elif(self.MS): self.MS = self.constMS
        if (dist1 <= dist2): #player one closer
            rads = math.atan2(y1_dis , (x1_dis))
            x = round(math.cos(rads) * self.MS)
            y = round(math.sin(rads) * self.MS)
        elif (dist1 > dist2): #plyer two closer
            rads = math.atan2(y2_dis , (x2_dis))
            x = round(math.cos(rads) * self.MS)
            y = round(math.sin(rads) * self.MS)
        
        self.rect.y += y
        self.rect.x += x
        
        if (self.rect.bottom >= HEIGHT) or (self.rect.top <= 0):
            self.rect.y -= self.MS * y
        if (self.rect.right > WIDTH) or (self.rect.left < 0):
            self.rect.x -= self.MS * x
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
        if (self.health <= 0): self.kill()
        self.time = time.clock()
        if (self.time_new <= self.time):
            self.time_new = time.clock() + (random.randint(10,40) / 10)
            self.x_dis = random.randint(0,20) / 10
            self.y_dis = random.randint(0,20) / 10
        
        self.rect.x += self.x_dis
        self.rect.y += self.y_dis
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
    
    def update(self,x1 = None,y1 = None,x2 = None,y2 = None):
        self.time = time.clock()
        if (pygame.sprite.spritecollideany(self,bullet_sprites)):
            self.health -= 1
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
        dist1 = math.sqrt((x1_dis * x1_dis) + (y1_dis * y1_dis))
        dist2 = math.sqrt((x2_dis * x2_dis) + (y2_dis * y2_dis))
        
        if (pygame.sprite.spritecollideany(self,water_sprites)): self.MS = self.slowspeed
        elif(self.MS): self.MS = self.constMS
        if (dist1 <= dist2): #player one closer
            rads = math.atan2(y1_dis , (x1_dis))

            x = round(math.cos(rads) * self.MS)
            y = round(math.sin(rads) * self.MS)
        elif (dist1 > dist2): #plyer two closer
            rads = math.atan2(y2_dis , (x2_dis))
            x = round(math.cos(rads) * self.MS)
            y = round(math.sin(rads) * self.MS)
        
        self.rect.y += y
        self.rect.x += x
        if (self.rect.bottom >= HEIGHT) or (self.rect.top <= 0):self.rect.y -= y
        if (self.rect.right > WIDTH) or (self.rect.left < 0):self.rect.x -= x
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
    
    def update(self,x1 = None,y1 = None,x2 = None,y2 = None):
        if (pygame.sprite.spritecollideany(self,bullet_sprites)): self.health -= 1
        if (self.health <= 0): self.kill()
        self.time = time.clock()

        #Turn invis
        if (self.time_new <= self.time):
            self.rand_timer_1 = (random.randint(90,120) / 10)
            self.time_new = self.time + self.rand_timer_1
            self.invis = 1
            self.image = self.image2
            self.MS += 1.5
        elif((self.time_new - self.rand_timer_1 + 2) >= self.time):
            self.invis = 1
            self.image = self.image2
            self.MS += 1.5
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
        dist1 = math.sqrt((x1_dis * x1_dis) + (y1_dis * y1_dis))
        dist2 = math.sqrt((x2_dis * x2_dis) + (y2_dis * y2_dis))
        if (pygame.sprite.spritecollideany(self,water_sprites)): self.MS = self.slowspeed
        else: self.MS = self.constMS
        if (dist1 <= dist2): #player one closer
            rads = math.atan2(y1_dis , (x1_dis))
            x = round(math.cos(rads) * self.MS)
            y = round(math.sin(rads) * self.MS)
        elif (dist1 > dist2): #plyer two closer
            rads = math.atan2(y2_dis , (x2_dis))
            x = round(math.cos(rads) * self.MS)
            y = round(math.sin(rads) * self.MS)
        
        self.rect.y += y
        self.rect.x += x

        #sprite detection
        
        if (self.rect.bottom >= HEIGHT) or (self.rect.top <= 0):
            self.rect.y -= y
        if (self.rect.right > WIDTH) or (self.rect.left < 0):
            self.rect.x -= x
        
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
        
        self.xspeed = math.cos(self.angle) * 21 # speed of bullet
        self.yspeed = math.sin(self.angle) * 21
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
            self.kill()
        if (self.rect.bottom >= HEIGHT + 100) or (self.rect.top <= -100):
                self.kill()
        if (self.rect.right > WIDTH + 100) or (self.rect.left < -100):
                self.kill()
        self.rect.x += self.xspeed
        self.rect.y += self.yspeed


class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,player_img_1,player_img_2,max_health,max_bullets,max_speed, regen_ammo, regen_health):
        pygame.sprite.Sprite.__init__(self)
        self.MB = max_bullets
        self.MH = max_health
        self.MS = max_speed
        self.constMS = max_speed
        self.slowspeed = max_speed * 0.5
        self.health = max_health
        self.bullets = max_bullets
        self.shoot_runonce = 1
        self.regen_ammo = regen_ammo
        self.regen_health = regen_health
        self.time = time.clock()
        self.current_time = 0
        self.damage_time = 0
        
        self.image_D = player_img_2
        self.image_N = player_img_1
        self.image = self.image_N
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.regen_h = 0
        self.regen_a = 0
    
    def get_x(self):
        return self.rect.x
    
    def get_y(self):
        return self.rect.y
    
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
    
    def get_regen_health(self):
        return self.regen_h
    
    def update(self, x , y, shoot_x, shoot_y, shoot):
        self.time = time.clock()
        #Check if alive
        if (self.health <= 0):
            self.kill()
            self.rect.y = -10000 #To make the enemys attack current target
            self.rect.x = -10000
        #for regen
        self.regen_a += self.regen_ammo
        self.regen_h += self.regen_health
        if ((self.regen_a >= 149)):
            if ((self.bullets < self.MB)): self.bullets += 1
            self.regen_a = 0
        if ((self.regen_h >= 149)):
            if((self.health < self.MH)): self.health += 1
            self.regen_h = 0
        if (pygame.sprite.spritecollideany(self,water_sprites)): self.MS = self.slowspeed
        else: self.MS = self.constMS
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
            if(pygame.sprite.spritecollideany(self,fly_sprites)):
                self.health -= 1
            if(pygame.sprite.spritecollideany(self,block_sprites)):
                self.health -= 2
            if(pygame.sprite.spritecollideany(self,ghost_sprites)):
                self.health -= 2
            if(pygame.sprite.spritecollideany(self,slime_sprites)):
                self.health -= 1
            
        elif (self.damage_time > self.time):
            self.image = self.image_D
        else:
            self.image = self.image_N
        
        rads = math.atan2(shoot_y , (shoot_x + 0.00001))
        
        pygame.draw.line(screen,RED, (self.rect.x + 17, self.rect.y + 17), (self.rect.x + 17 + (math.cos(rads) * 27), self.rect.y + 17 + (math.sin(rads) * 27)),2) # makes the line for shooting

        #shooting
        if (shoot and self.shoot_runonce and self.bullets > 0):
            self.shoot_runonce = 0
            self.bullets -= 1
            #shooting bullet
            __bullet__ = Bullet(self.rect.x + 17,self.rect.y + 17,rads,bullet_img,1)
            bullet_sprites.add(__bullet__)
        elif (not shoot):
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

# setup
Start_BackGround = Background(os.path.join(location,'front_screen.bmp'), [0,0])
l1_BackGround = Background(os.path.join(location,'level_1.bmp'), [0,0])
l2_BackGround = Background(os.path.join(location,'level_2.bmp'), [0,0])
#players
p1_img = pygame.image.load(os.path.join(location,'chick.bmp')).convert()
p2_img = pygame.image.load(os.path.join(location,'owl.bmp')).convert()
p1d_img = pygame.image.load(os.path.join(location,'chick_d.bmp')).convert()
p2d_img = pygame.image.load(os.path.join(location,'owl_d.bmp')).convert()
#monsters
m1_img = pygame.image.load(os.path.join(location,'ghost.bmp')).convert()
m1_1_img = pygame.image.load(os.path.join(location,'ghost_d.bmp')).convert()
m2_img = pygame.image.load(os.path.join(location,'slimeBlock.bmp')).convert()
m2_2_img = pygame.image.load(os.path.join(location,'slimeBlockD.bmp')).convert()
m3_img = pygame.image.load(os.path.join(location,'grassBlock.bmp')).convert()
m3_3_img = pygame.image.load(os.path.join(location,'grassBlockD.bmp')).convert()
m4_img = pygame.image.load(os.path.join(location,'fly.bmp')).convert()
#walls
wall_img = pygame.image.load(os.path.join(location,'wall_1.bmp')).convert()
water_img = pygame.image.load(os.path.join(location,'water.bmp')).convert()
#bullets
bullet_img1 = pygame.image.load(os.path.join(location,'bullet.bmp')).convert()
bullet_img2 = pygame.image.load(os.path.join(location,'bullet_1.bmp')).convert()
#UI
ammo_img = pygame.image.load(os.path.join(location,'ammo.bmp')).convert()
hp_img = pygame.image.load(os.path.join(location,'health.bmp')).convert()

pygame.joystick.init()

def make_ghost(x,y,round):
    health = 3 + round
    dum = GHOST(x,y,m1_img,m1_1_img, health)
    ghost_sprites.add(dum)
    enemy_sprites.add(dum)

def make_block(x,y,round):
    health = 5 + round
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

def update_leaderboards():
    global wave_num, points
    message_display_1(20, ("Wave: " + str(wave_num)) ,WIDTH * .5, HEIGHT * .02, WHITE)
    message_display_1(20, ("Points: " + str(points)) ,WIDTH * .5, HEIGHT * .05, WHITE)




#Game_functions
def create_map():
    global MAP, wall_img, player_2, player_1, points
    y = 0
    points = 0
    try:
        UI_function(player_1.get_max_health(), player_1.get_max_bullets(), player_2.get_max_health(), player_2.get_max_bullets())
    except:
        try:
            UI_function(player_1.get_max_health(), player_1.get_max_bullets(), 0, 0)
        except:
            try:
                UI_function(0, 0, 0, 0)
            except:
                print("Error")
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

# (self,x,y,player_img_1,player_img_2,max_health,max_bullets,max_speed, regen_ammo, regen_health):
def start_menu():
    global p1_runonce, p2_runconce,joystick_0, joystick_1
    screen.blit(Start_BackGround.image, Start_BackGround.rect)
    message_display_1(40, "Welcome to the shooting game brah",WIDTH * .5, HEIGHT * .2, WHITE)
    message_display_1(20, "Press start to continue",WIDTH * .5, HEIGHT * .8, WHITE)
    buttons(18, 'Start Game', WIDTH * .5, HEIGHT*.1, 121, 35,PEACH_2,PEACH_1,1,level_place_add)
    try:
        joystick_0 = pygame.joystick.Joystick(0)
    except:
        print("P1 Not init")
    try:
        joystick_1 = pygame.joystick.Joystick(1)
    except:
        print("P2 Not init")
    try:
        joystick_0.init()
        if (joystick_0.get_init):
            message_display_1(20, "Player one connected",WIDTH * .2, HEIGHT * .5, GREEN)
            message_display_1(10, "Stats:",WIDTH * .2, HEIGHT * .55, GREEN)
            message_display_1(10, "Special: Life Steal",WIDTH * .2, HEIGHT * .575, GREEN)
            message_display_1(10, "Health: 6",WIDTH * .2, HEIGHT * .6, GREEN)
            message_display_1(10, "Bullets: 4",WIDTH * .2, HEIGHT * .625, GREEN)
            message_display_1(10, "Speed: 5",WIDTH * .2, HEIGHT * .65, GREEN)
            if (p1_runonce == 1):
                global player_1
                player_1 = Player(WIDTH * .35, HEIGHT * .5, p1_img, p1d_img, 10, 8, 5, 100, 1.4)
                player_1_sprites.add(player_1)
                p1_runonce = 0
            
    except:
        message_display_1(20, "Player one NOT connected",WIDTH * .2, HEIGHT * .5, RED)
    try:
        joystick_1.init()
        if (joystick_1.get_init) :
            message_display_1(20, "Player two connected",WIDTH * .2, HEIGHT * .4, GREEN)
            message_display_1(10, "Stats:",WIDTH * .2, HEIGHT * .25, GREEN)
            message_display_1(10, "Special: Dash",WIDTH * .2, HEIGHT * .275, GREEN)
            message_display_1(10, "Health: 3",WIDTH * .2, HEIGHT * .3, GREEN)
            message_display_1(10, "Bullets: 5",WIDTH * .2, HEIGHT * .325, GREEN)
            message_display_1(10, "Speed: 4",WIDTH * .2, HEIGHT * .35, GREEN)
            if (p2_runconce == 1):
                global player_2
                player_2 = Player(WIDTH * .35, HEIGHT * .4, p2_img, p2d_img, 8, 10, 6, 190, 1)
                player_2_sprites.add(player_2)
                p2_runonce = 0
    except:
        message_display_1(20, "Player two NOT connected",WIDTH * .2, HEIGHT * .4, RED)

def enemy_creater(*list_1):
    global enemy_timer
    #enemy_timer = time.clock()
    if(enemy_timer < (time.clock() - random.randint(5,40)/10)):
        enemy_timer = time.clock()
        x = random.randint(1,3)
        if (x == 1):          make_ghost(random.randint(100,WIDTH),random.randint(100,HEIGHT),round(enemy_timer / 10))

        elif (x == 2):        make_slime(random.randint(100,WIDTH),random.randint(100,HEIGHT),round(enemy_timer / 10))

        elif (x == 3):        make_block(random.randint(100,WIDTH),random.randint(100,HEIGHT),round(enemy_timer / 10))

    """
    for i in range(0,15):
        if ((list_1[0][i][2] < enemy_timer) and list_1[0][i][4]):
            list_1[0][i][4] = 0
            if (list_1[0][i][3] == 0):
                make_fly(list_1[0][i][0],list_1[0][i][1],0)
            elif (list_1[0][i][3] == 1):
                make_block(list_1[0][i][0],list_1[0][i][1],0)
            elif (list_1[0][i][3] == 2):
                make_slime(list_1[0][i][0],list_1[0][i][1],0)
            elif (list_1[0][i][3] == 3):
                make_ghost(list_1[0][i][0],list_1[0][i][1],0)
    """

def level_1():
    global map_runonce, player_2, player_1, joystick_0, joystick_1, waves
    enemy_creater(waves)
    if (map_runonce):
        map_runonce = 0
        create_map()
    screen.blit(l1_BackGround.image, l1_BackGround.rect)
    fire = 0
    try:
        if (joystick_0.get_axis(5) > -0.5):
            fire = 1
        player_1_sprites.update(joystick_0.get_axis(0),joystick_0.get_axis(1),joystick_0.get_axis(2),joystick_0.get_axis(3),fire)
    except:
        print("Player 1 not connected")
    try:
        fire = 0
        if (joystick_1.get_axis(5) > -0.5):
            fire = 1
        player_2_sprites.update(joystick_1.get_axis(0),joystick_1.get_axis(1),joystick_1.get_axis(2),joystick_1.get_axis(3),fire)
    except:
        print("Player 2 Not connected")
    fly_sprites.update()
    
    block_sprites.update(player_1.get_x(), player_1.get_y(), player_2.get_x(), player_2.get_y())
    ghost_sprites.update(player_1.get_x(), player_1.get_y(), player_2.get_x(), player_2.get_y())
    slime_sprites.update(player_1.get_x(), player_1.get_y(), player_2.get_x(), player_2.get_y())
    UI_HP1_sprites.update(player_1.get_health())
    UI_AP1_sprites.update(player_1.get_bullets())
    UI_HP2_sprites.update(player_2.get_health())
    UI_AP2_sprites.update(player_2.get_bullets())
    #Regen
    pygame.draw.rect(screen,RED,pygame.Rect(8,36,150,9),1)
    pygame.draw.rect(screen,PEACH_1,pygame.Rect(8,46,150,9),1)
    pygame.draw.rect(screen,RED,pygame.Rect(9,36,player_1.get_regen_health(),9),0) # 149
    pygame.draw.rect(screen,PEACH_1,pygame.Rect(9,46,player_1.get_regen_bullets(),9),0)

    pygame.draw.rect(screen,RED,pygame.Rect(866,36,150,9),1)
    pygame.draw.rect(screen,PEACH_1,pygame.Rect(866,46,150,9),1)
    pygame.draw.rect(screen,RED,pygame.Rect(866,36,player_2.get_regen_health(),9),0) # 149
    pygame.draw.rect(screen,PEACH_1,pygame.Rect(866,46,player_2.get_regen_bullets(),9),0)
    """
    except ExplicitException:
        try:
            UI_HP1_sprites.update(player_1.get_health())
            UI_AP1_sprites.update(player_1.get_bullets())
            pygame.draw.rect(screen,RED,pygame.Rect(8,36,150,9),1)
            pygame.draw.rect(screen,PEACH_1,pygame.Rect(8,46,150,9),1)
            pygame.draw.rect(screen,RED,pygame.Rect(9,36,player_1.get_regen_health(),9),0) # 149
            pygame.draw.rect(screen,PEACH_1,pygame.Rect(9,46,player_1.get_regen_bullets(),9),0)
            block_sprites.update(player_1.get_x(), player_1.get_y(), -5000, -5000)
            ghost_sprites.update(player_1.get_x(), player_1.get_y(), -5000, -5000)
            slime_sprites.update(player_1.get_x(), player_1.get_y(), -5000, -5000)
        except ExplicitException:
            try:
                pass
                #block_sprites.update(0, 0, 0, 0)
                #ghost_sprites.update(0, 0, 0, 0)
                #slime_sprites.update(0, 0, 0, 0)
            except ExplicitException:
                print("Error")
    """
    bullet_sprites.update() 
    update_leaderboards()

def level_2():
    screen.blit(l2_BackGround.image, l2_BackGround.rect)


location = 0 #Start in menu
p1_runonce = 1
p2_runconce = 1
map_runonce = 1
points = 0
wave_num = 1
enemy_timer = 0

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
        wall_sprites.draw(screen)
        water_sprites.draw(screen)
        bullet_sprites.draw(screen)
        UI_HP1_sprites.draw(screen)
        UI_AP1_sprites.draw(screen)
        UI_HP2_sprites.draw(screen)
        UI_AP2_sprites.draw(screen)
        
        pygame.display.flip()


main(1);























