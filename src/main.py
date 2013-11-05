# -*- coding: utf-8 -*-
# File main.py

from classes.tiled import TiledRenderer
from classes.hero import Hero
from classes.cursor import Cursor
from classes.menu import Menu
from classes.inventory import Item, Bag
import classes.settings as settings
import sys
import pygame
from pygame.locals import *
import math

CHARSET_DIR = settings.CHARSET_DIR
MAPS_DIR = settings.MAPS_DIR
IMAGES_DIR = settings.IMAGES_DIR
DIRECTIONS = settings.DIRECTIONS
pygame.init()
screen = pygame.display.set_mode((640, 640))
screen_buf = pygame.Surface(screen.get_size())
clock = pygame.time.Clock()
angus = Hero()
hawk = Hero(name="Hawk")
hello = Hero(name="Hello")
world = Hero(name="World")
team = [angus, hawk, hello, world]
bag = Bag()
randobject = Item(name="Random !", quantity=2, effect="None")
bag.useable.append(randobject)

for item in bag.useable:
    print("Name : %s\nQuantity : %s\nEffect : %s" % (item.name, item.quantity, item.effect))

hawk.stats.hp -= 10
hawk.stats.level = 15

hello.stats.hp = 1
hello.stats.level = 2

world.stats.hp = 10
world.stats.maxhp = 2000
world.stats.level = 32

class Game(object):
    """ The main Game Class """
    def __init__(self):
        pygame.font.init()
        pygame.display.set_caption('Yet Another SNES RPG')
        pygame.mouse.set_visible(0)
        pygame.key.set_repeat(1, 5)

    def game(self, filename):
        formosa = TiledRenderer(filename)

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
                        if testrect.collidelist(formosa.boxcollider) == -1:
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
                        if testrect.collidelist(formosa.boxcollider) == -1:
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
                        if testrect.collidelist(formosa.boxcollider) == -1:
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
                        if testrect.collidelist(formosa.boxcollider) == -1:
                            angus.position.y += 2
                            angus.collision.y += 2

                    elif (event.key == K_ESCAPE):
                        menu = Menu(screen, team, bag)
                        menu.open_menu()

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

    def quit(self):
        pygame.quit()

game = Game()
game.game(MAPS_DIR+"map.tmx")
game.quit()