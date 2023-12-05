# This file was created by Elliott Barringer

# import necessary libs and modules
import pygame as pg
from pygame.sprite import Sprite
from pygame.math import Vector2 as vec
import os
from settings import *
from threading import Timer
from random import randint as r

# set up for asset folders

game_folder = os.path.dirname(__file__)
img_folder = game_folder

# Set up for Player using WASD
class Player(Sprite):

    def __init__(self, x, y, w, h, k_left, k_right, k_jump, game, color):

        Sprite.__init__(self)

        self.image = pg.Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos = vec(x, y)
        self.game = game
        self.k_left = k_left
        self.k_right = k_right
        self.k_jump = k_jump
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.speed = PLAYER_SPEED
        self.hop = PLAYER_JUMP

        '''self.image = pg.Surface((20, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.game = game
        # self.image = pg.Surface((20, 20))
        # self.image.fill(WHITE)
        # self.rect = self.image.get_rect()
        # self.rect.center = (0, 0)
        self.rect.x
        self.pos = vec(x, y)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.speed = PLAYER_SPEED
        self.hop = PLAYER_JUMP
        print("Spawned")'''

    def controls(self):

        keys = pg.key.get_pressed()

        if keys[self.k_left]:

            self.acc.x = -self.speed
        
        if keys[self.k_right]:

            self.acc.x = self.speed
        
        if keys[self.k_jump]:

            self.jump()
    
    def jump(self):

        p_hits = pg.sprite.spritecollide(self, self.game.all_platforms, False)

        if p_hits:

            self.vel.y = - PLAYER_JUMP

    def update(self):

        self.acc = vec(0, PLAYER_GRAV)
        self.controls()

        self.acc.x += self.vel.x * -PLAYER_FRIC

        # motion eqs

        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

        # check for interaction with powerups

        speed = pg.sprite.spritecollide(self, self.game.all_speed, True)
        super_jump = pg.sprite.spritecollide(self, self.game.all_super_jump, True)
        size_mod = pg.sprite.spritecollide(self, self.game.all_size_mod, True)

        t = Timer(self.reset(), 5)

        self.check_powerup(speed, super_jump, size_mod, t)

    def check_powerup(self, cond1, cond2, cond3, timer):

        if cond1:

            self.speed += 5
            timer.start()
        
        elif cond2:

            self.hop += 30
            timer.start()
        
        elif cond3:

            self.image = pg.Surface((50, 50))
            timer.start()
        
        else:

            pass

    def reset(self):

        self.speed = PLAYER_SPEED
        self.hop = PLAYER_JUMP
        self.image = pg.Surface((20, 20))   

    def display(self):
        self.draw(self.game.screen)     

# class for player using arrow keys
'''class PlayerB(Sprite):

    def __init__(self, game):

        Sprite.__init__(self)
        
        self.game = game
        self.image = pg.Surface((20, 20))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        #self.rect.center = (0, 0)
        self.pos = vec(WIDTH/2 + 80, HEIGHT/2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.speed = PLAYER_SPEED
        self.hop = PLAYER_JUMP

    def controls(self):
# check for plau controls 
        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:

            self.acc.x = -self.speed
        
        if keys[pg.K_RIGHT]:

            self.acc.x = self.speed
        
        if keys[pg.K_UP]:

            self.jump()
    
    def jump(self):

        p_hits = pg.sprite.spritecollide(self, self.game.all_platforms, False)

        if p_hits:

            self.vel.y = - PLAYER_JUMP

    def update(self):

        self.acc = vec(0, PLAYER_GRAV)
        self.controls()

        self.acc.x += self.vel.x * -PLAYER_FRIC

        # motion eqs

        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

        # check for interaction with powerups

        speed = pg.sprite.spritecollide(self, self.game.all_speed, True)
        super_jump = pg.sprite.spritecollide(self, self.game.all_super_jump, True)
        size_mod = pg.sprite.spritecollide(self, self.game.all_size_mod, True)

        t = Timer(self.reset(), 5)

        self.check_powerup(speed, super_jump, size_mod, t)

    def check_powerup(self, cond1, cond2, cond3, timer):

        if cond1:

            self.speed += 5
            timer.start()
        
        elif cond2:

            self.hop += 30
            timer.start()
        
        elif cond3:

            self.image = pg.Surface((50, 50))
            timer.start()
        
        else:

            pass

    def reset(self):

        self.speed = PLAYER_SPEED
        self.hop = PLAYER_JUMP
        self.image = pg.Surface((20, 20))      
'''
# class for powerups
class Powerup(Sprite):

    def __init__(self, x, y, w, h, kind, game):

        Sprite.__init__(self)

        self.image = pg.Surface((w, h))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.pos = vec(x, y)
        self.kind = p_dict[str(kind)]
        self.game = game

        # sort powerups into sprite groups
        all_super_jump = pg.sprite.Group()
        all_super_speed = pg.sprite.Group()
        all_size_mod = pg.sprite.Group()

        if self.kind == "speed":
            
            all_super_speed.add(self)
        
        elif self.kind == "super_jump":

            all_super_jump.add(self)
        
        elif self.kind == "size_mod":

            all_size_mod.add(self)
    
    def update(self):
        
        c = pg.sprite.spritecollide(self, self.game.all_players, True)

        t = Timer(self.reset(), 15)

        if c:
            # 'hide' the image by moving it off the screen
            self.pos = vec(2 * WIDTH, 2 * HEIGHT)
            t.start()
    
    def reset(self):

        self.pos = vec(self.rect.x, self.rect.y)

# class for platforms
class Platform(Sprite):

    def __init__(self, x, y, w, h, category):

        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.category = category
        self.speed = 0

        if self.category == "moving":

            self.speed = 5
    
    def update(self):

        if self.category == "moving":

            self.rect.x += self.speed

            if self.rect.x + self.rect.w > WIDTH or self.rect.x < 0:

                self.speed = -self.speed
