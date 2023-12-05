# This file was created by: Elliott Barringer
# Content from Chris Bradfield; Kids Can Code
# KidsCanCode - Game Development with Pygame video series
# Video link: https://youtu.be/OmlQ0XCvIn0 

# import necessary modules / libraries
import os
from random import randint as r
import pygame as pg

# setup asset files
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'imgs')

# game settings 
WIDTH = 360
HEIGHT = 480
FPS = 30

# player settings
PLAYER_JUMP = 30
PLAYER_GRAV = 1.5
global PLAYER_FRIC
PLAYER_FRIC = 0.2
PLAYER_SPEED = 5

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# list for platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, "normal"),
                 (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 20,"normal"),
                 (125, HEIGHT - 350, 100, 20, "moving"),
                 (222, 200, 100, 20, "normal"),
                 (175, 100, 50, 20, "normal")]

# list for powerups
# x, y, w, h, kind, game
POWER_UP_LIST = [(r(0, WIDTH), r(0, HEIGHT), 25, 25, r(1, 3)),
                 (r(0, WIDTH), r(0, HEIGHT), 25, 25, r(1, 3)),
                 (r(0, WIDTH), r(0, HEIGHT), 25, 25, r(1, 3)),
                 (r(0, WIDTH), r(0, HEIGHT), 25, 25, r(1, 3)),
                 (r(0, WIDTH), r(0, HEIGHT), 25, 25, r(1, 3))]

# list for players
# x, y, w, h, k_left, k_right, k_jump, game
PLAYER_LIST = [(100, HEIGHT - 40, 15, 15, pg.K_a, pg.K_d, pg.K_SPACE),
               (200, HEIGHT - 40, 15, 15, pg.K_LEFT, pg.K_RIGHT, pg.K_UP)]

# dictionary for random powerups
p_dict = {
    '1': 'speed',
    '2': 'super_jump',
    '3': 'size_mod'
}
