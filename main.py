# This file was created by Elliott Barringer

'''

__Dev Goals__

- rework game to be about tag
- addition of power ups
- two player game

__Game Design__

    _Goals_

    - tag the other player
    - game functions like hot potato; try not to be 'it' when the timer runs out

    _Rules_

    - player can run and jump and interact with powerups
    - collide with opposing player to transfer status of 'it'

    _Feedback_

    - timer and labels at the top of the screen
    - express how much time is left and which player is 'it'

    _Freedom_

    - player can run and jump around the map
    - platforms and powerups allow for more mobility and interaction with environment

'''

# import necessary libraries and modules
import pygame as pg
from pygame.sprite import Sprite
from pygame.math import Vector2 as vec
import os
import settings
from sprites import *
from random import randint as r
import math

class Game:

    def __init__(self):

        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("TAG")
        self.clock = pg.time.Clock()
        self.running = True
    
    def new(self):
        # instantiate players with different key bindings 
        playerA = Player(10, 180, 10, 10, 'a', 'd', 'SPACE', self)
        playerB = Player(20, 180, 10, 10, 'LEFT', 'RIGHT', 'UP', self)
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.all_players = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.all_power_ups = pg.sprite.Group()
        self.all_speed = pg.sprite.Group()
        self.all_super_jump = pg.sprite.Group()
        self.all_size_mod = pg.sprite.Group()

        self.all_players.add(playerA)
        self.all_players.add(playerB)
        # list instantiation method
        for p in PLATFORM_LIST:

            plat = Platform(*p)
            self.all_sprites.add(plat)
            self.all_platforms.add(plat)
        # list instantiation method
        for m in POWER_UP_LIST:

            PowerUp = Powerup(*m, game=self)
            self.all_sprites.add(PowerUp)
            self.all_power_ups.add(PowerUp)
        
        self.run()
    # run loop method
    def run(self):

        self.playing = True

        while self.playing:

            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def update(self):
        if self.playing == True:
            self.all_sprites.update()
        # check for interaction with platform
            if playerA.x in self.all_players > 0:

                hits_a = pg.sprite.spritecollide(playerA, self.all_platforms, False)

                if hits_a:

                    playerA.pos.y = hits_a[0].rect.top
                    playerA.vel.y = 0
                    playerA.vel.y = hits_a[0].speed*1.5
        
            if playerB.vel.y > 0:
            # check if player B interacts with platform
                hits_b = pg.sprite.spritecollide(playerB, self.all_platforms, False)

                if hits_b:

                    playerB.pos.y = hits_b[0].rect.top
                    playerB.vel.y = 0
                    playerB.vel.y = hits_b[0].speed*1.5

            if playerA.vel.y < 0:
                # checks for play A interactions with platforms
                hits_a = pg.sprite.spritecollide(playerA, self.all_platforms, False)

                if hits_a:

                    if self.player_a.rect.bottom >= hits_a[0].rect.top - 1:

                        playerA.rect.top = hits_a[0].rect.bottom
                        playerA.acc.y = 5
                        playerA.vel.y = 0
        
            if playerB.vel.y < 0:
            # checks for player B interactions with platforms
                hits_b = pg.sprite.spritecollide(playerB, self.all_platforms, False)

                if hits_b:

                    if playerB.rect.bottom >= hits_a[0].rect.bottom:

                        playerB.rect.top = hits_a[0].rect.bottom
                        playerB.acc.y = 5
                        playerB.vel.y = 0
    
    def events(self):

        for event in pg.event.get():

            if event.type == pg.QUIT:

                if self.playing:

                    self.playing = False
                
                self.running = False
    # draw screen
    def draw(self):

        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        #self.draw_text()
        pg.display.flip()
    
    def draw_text(self, text, size, color, x, y):
        # function to draw text 
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

g = Game()
# run loop
while g.running:

    g.new()

pg.quit()



