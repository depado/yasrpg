# -*- coding: utf-8 -*-

from pytmx import tmxloader
import sys
import pygame
from pygame.locals import *
import math

# Calque 0 : Terrain, toujours en dessous, sans collision
# Calque 1 : Terrain, toujours en dessous, avec collision
# Calque 2 : Objets collisionant en dessous du héro
# Calque 3 : Au dessus du terrain sans colision
# Calque 4 : Objets au dessus du héro

class TiledRenderer(object):
    """
    Super simple way to render a tiled map
    """

    def __init__(self, filename):
        self.tiledmap = tmxloader.load_pygame(filename, pixelalpha=True)
        self.boxcolider = []

    def terrain_render(self, surface):
        tw = self.tiledmap.tilewidth
        th = self.tiledmap.tileheight
        gt = self.tiledmap.getTileImage

        for l in xrange(0, 1):
            for y in xrange(0, self.tiledmap.height):
                for x in xrange(0, self.tiledmap.width):
                    tile = gt(x, y, l)
                    if tile: surface.blit(tile, (x*tw, y*th))

    def over_terrain_render(self, surface):
        tw = self.tiledmap.tilewidth
        th = self.tiledmap.tileheight
        gt = self.tiledmap.getTileImage

        for l in xrange(1, 2):
            for y in xrange(0, self.tiledmap.height):
                for x in xrange(0, self.tiledmap.width):
                    tile = gt(x, y, l)
                    if tile: surface.blit(tile, (x*tw, y*th))

    def under_char_render(self, surface):
        tw = self.tiledmap.tilewidth
        th = self.tiledmap.tileheight
        gt = self.tiledmap.getTileImage

        for l in xrange(2, 3):
            for y in xrange(0, self.tiledmap.height):
                for x in xrange(0, self.tiledmap.width):
                    tile = gt(x, y, l)
                    if tile: 
                        surface.blit(tile, (x*tw, y*th))
                        self.boxcolider.append(pygame.Rect(x*tw, y*th, tw, th))

    def over_char_render(self, surface):
        tw = self.tiledmap.tilewidth
        th = self.tiledmap.tileheight
        gt = self.tiledmap.getTileImage

        for l in xrange(3, 4):
            for y in xrange(0, self.tiledmap.height):
                for x in xrange(0, self.tiledmap.width):
                    tile = gt(x, y, l)
                    if tile: surface.blit(tile, (x*tw, y*th))

CHARSET = '../res/charsets/'
MAPS = '../maps/'
DIRECTIONS = {'down':0, 'left':1, 'right':2, 'up':3}

def extract_sprite(size,file,pos=(0,0)):
    sheet = pygame.image.load(file).convert_alpha() 
    sheet_rect = sheet.get_rect()
    sheet.set_clip(pygame.Rect(pos[0]*size, pos[1]*size, size, size))
    sprite = sheet.subsurface(sheet.get_clip())
    return sprite

class Hero(pygame.sprite.Sprite):
    """
    Our Fucking Nice Hero
    """

    def __init__(self, name="Angus"):
        # Non displayable
        self.position = pygame.Rect(5, 5, 32, 32)
        self.collision = pygame.Rect(self.position.x+3, self.position.y+16, 26, 16)
        self.index = 0
        self.direction = DIRECTIONS['down']
        self.UPDATE_TIME = 10
        self.timer = 0
        # In game Infos
        self.name = name
        self.level = 1
        # Animations
        self.up_anim = []
        self.down_anim = []
        self.right_anim = []
        self.left_anim = []
        self.set_file(CHARSET+"captain.png")
        self.image = self.down_anim[0]

    def set_file(self, newfile):
        """ Change the file for the """
        self.file = newfile
        for x in xrange(0,2):
            self.down_anim.append(extract_sprite(32, self.file, (x, DIRECTIONS['down'])))
            self.up_anim.append(extract_sprite(32, self.file, (x, DIRECTIONS['up'])))
            self.left_anim.append(extract_sprite(32, self.file, (x, DIRECTIONS['left'])))
            self.right_anim.append(extract_sprite(32, self.file, (x, DIRECTIONS['right'])))

    def update(self):
        self.timer += 1
        if self.timer >= self.UPDATE_TIME:
            self.index += 1
            self.timer = 0
            if self.index >= 2:
                self.index = 0
            if self.direction == DIRECTIONS['down']:
                self.image = self.down_anim[self.index]
            elif self.direction == DIRECTIONS['up']:
                self.image = self.up_anim[self.index]
            elif self.direction == DIRECTIONS['left']:
                self.image = self.left_anim[self.index]
            elif self.direction == DIRECTIONS['right']:
                self.image = self.right_anim[self.index]

    def update_now(self):
        self.index += 1
        if self.index >= 2:
            self.index = 0
        if self.direction == DIRECTIONS['down']:
            self.image = self.down_anim[self.index]
        elif self.direction == DIRECTIONS['up']:
            self.image = self.up_anim[self.index]
        elif self.direction == DIRECTIONS['left']:
            self.image = self.left_anim[self.index]
        elif self.direction == DIRECTIONS['right']:
            self.image = self.right_anim[self.index]

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((640, 640))
pygame.display.set_caption('Yet Another SNES RPG')
pygame.key.set_repeat(1, 5)
clock = pygame.time.Clock()


def simpleTest(filename):
    screen_buf = pygame.Surface(screen.get_size())
    screen_buf.fill((0,128,255))
    formosa = TiledRenderer(filename)

    angus = Hero()

    # print "Objects in map:"
    # for o in formosa.tiledmap.getObjects():
    #     print o
    #     for k, v in o.__dict__.items():
    #         print "  ", k, v

    # print "GID (tile) properties:"
    # for k, v in formosa.tiledmap.tile_properties.items():
    #     print "  ", k, v

    run = True
    while run:
        key=pygame.key.get_pressed() 
        try:
            event = pygame.event.wait()
            if event.type == KEYDOWN:
                if (event.key == K_LEFT):
                    if angus.direction != DIRECTIONS['left']:
                        angus.direction = DIRECTIONS['left']
                        angus.update_now()
                    else:
                        angus.update()
                    testrect = pygame.Rect(angus.collision.x-2, angus.collision.y, 26, 16 )
                    if testrect.collidelist(formosa.boxcolider) == -1:
                        angus.position.x -= 2
                        angus.collision.x -= 2

                # KEY RIGHT
                elif (event.key == K_RIGHT):
                    if angus.direction != DIRECTIONS['right']:
                        angus.direction = DIRECTIONS['right']
                        angus.update_now()
                    else:
                        angus.update()
                    testrect = pygame.Rect(angus.collision.x+2, angus.collision.y, 26, 16 )
                    if testrect.collidelist(formosa.boxcolider) == -1:
                        angus.position.x += 2
                        angus.collision.x += 2

                # KEY UP
                elif (event.key == K_UP):
                    if angus.direction != DIRECTIONS['up']:
                        angus.direction = DIRECTIONS['up']
                        angus.update_now()
                    else:
                        angus.update()
                    testrect = pygame.Rect(angus.collision.x, angus.collision.y-2, 26, 16 )
                    if testrect.collidelist(formosa.boxcolider) == -1:
                        angus.position.y -= 2
                        angus.collision.y -= 2

                # KEY DOWN        
                elif (event.key == K_DOWN):
                    if angus.direction != DIRECTIONS['down']:
                        angus.direction = DIRECTIONS['down']
                        angus.update_now()
                    else:
                        angus.update()
                    testrect = pygame.Rect(angus.collision.x, angus.collision.y+2, 26, 16 )
                    if testrect.collidelist(formosa.boxcolider) == -1:
                        angus.position.y += 2
                        angus.collision.y += 2

            if event.type == QUIT: run = False 

        except KeyboardInterrupt:
            run = False

        formosa.terrain_render(screen_buf)
        formosa.over_terrain_render(screen_buf)
        formosa.under_char_render(screen_buf)
        screen_buf.blit(angus.image,angus.position)
        formosa.over_char_render(screen_buf)
        pygame.transform.scale(screen_buf, screen.get_size(), screen)
        pygame.display.flip()
        clock.tick(60)


simpleTest(MAPS+"map.tmx")

pygame.quit()