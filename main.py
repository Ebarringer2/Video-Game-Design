# This file was created by Elliott Barringer

'''
__Feature Goals__

- rework the game into tag game
- two players, one is designated as a tagger and the other is trying to run away
- one player uses WSDA and the other uses arrow keys
- add power ups

__Player Goals__

- game functions like hot potato
- the goal is to try not to be 'it' when the time runs out
- players just to tag each other, transfering who is 'it'

__Rules__

- jump, run around
- players can use platforms
- players can interact with powerups

__Feedback__

- text displays who is 'it'
- timer at the top of the screen
- sound ques for player interaction with powerups or other players

__Freedom__

- players can run and jump around the map
- interact with platforms and powerups

'''


# import necessary libraries and modules

import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint 
import os 
from settings import *
from sprites import *
import math

vec = pg.math.Vector2

# setup folders for images, sounds

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'imgs')
snd_folder = os.path.join(game_folder, 'snds')

class Game:

    def __init__(self):

        # init pygame and create a window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self):

        # create a group for all sprites
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.all_players = pg.sprite.Group()

        # create two players
        self.player_a = Player(self)
        self.player_b = Player(self)

        # add the players to groups
        self.all_sprites.add(self.player_a)
        self.all_sprites.add(self.player_b)
        self.all_players.add(self.player_a)
        self.all_players.add(self.player_b)

        for p in PLATFORM_LIST:
            # instantiation of the Platform class
            plat = Platform(*p)
            self.all_sprites.add(plat)
            self.all_platforms.add(plat)

        self.run()
    
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

        # this is what prevents the player from falling through the platform when falling down...
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
                self.player.vel.x = hits[0].speed*1.5
                    
         # this prevents the player from jumping up through a platform
        elif self.player.vel.y < 0:
            hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
            if hits:
                print("ouch")
                self.score -= 1
                if self.player.rect.bottom >= hits[0].rect.top - 1:
                    self.player.rect.top = hits[0].rect.bottom
                    self.player.acc.y = 5
                    self.player.vel.y = 0

    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
                
    def draw(self):
        ############ Draw ################
        # draw the background screen
        self.screen.fill(BLACK)
        # draw all sprites
        self.all_sprites.draw(self.screen)
        self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH/2, HEIGHT/10)
        # buffer - after drawing everything, flip display
        pg.display.flip()
    
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)
