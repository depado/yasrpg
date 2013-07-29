# -*- coding: utf-8 -*-

from classes.tiled import TiledRenderer
from classes.hero import Hero
import classes.settings as settings
import sys
import pygame
from pygame.locals import *
import math

CHARSET_DIR = settings.CHARSET_DIR
MAPS_DIR = settings.MAPS_DIR
FONT = settings.FONT
FONT_SIZE = settings.FONT_SIZE
DIRECTIONS = settings.DIRECTIONS
pygame.init()
screen = pygame.display.set_mode((640, 640))
screen_buf = pygame.Surface(screen.get_size())
font = pygame.font.Font(FONT, FONT_SIZE)
clock = pygame.time.Clock()
angus = Hero()

class Menu(object):
    """docstring for Menu"""
    def __init__(self):
        self.menu_items = ['Items','Equip','Magic','Status','Save','Close','Quit']
        
    def open_menu(self):
        menu = True
        pygame.key.set_repeat()
        while menu:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        menu = False

            self.render_char(angus)
            self.render_menu()
            pygame.transform.scale(screen_buf, screen.get_size(), screen)
            pygame.display.flip()
            clock.tick(60)
        pygame.key.set_repeat(1,5)

    def render_menu(self):
        pos = 5
        for item in self.menu_items:
            screen_buf.blit(font.render(item, 4, (255,255,255)), (screen_buf.get_width()-100,pos))
            pos += 15


    def render_char(self, char):
        char.update()
        screen_buf.blit(char.image, pygame.Rect(5,5,32,32))
        screen_buf.blit(font.render(str(char.name), 4,(255,255,255)), (50, 5))
        screen_buf.blit(font.render("Level : "+str(char.level), 4,(255,255,255)), (50, 20))


menu = Menu()
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