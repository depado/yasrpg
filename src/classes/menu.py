# -*- coding: utf-8 -*-
# File menu.py

import pygame
from pygame.locals import *
from .cursor import Cursor
from .settings import IMAGES_DIR, DIRECTIONS, FONT, FONT_SIZE

TBK = (255, 255, 255)   # Black color tuple.

class Menu(object):
    """docstring for Menu"""
    def __init__(self, screen, team, bag):
        self.clock = pygame.time.Clock()
        self.team = team
        self.bag = bag
        self.screen = screen
        self.buffer = pygame.Surface(self.screen.get_size())
        self.font = pygame.font.Font(FONT, FONT_SIZE)
        self.menu_items = ['Items', 'Equip', 'Magic', 'Status', 'Save',
                           'Close', 'Quit']
        self.menu_image = pygame.image.load(IMAGES_DIR + 'menu.png').convert_alpha()
        self.ypos = [20, 45, 70, 95, 120, 145, 170]
        self.cursor = Cursor(ypos=self.ypos)
        self.blitable = []


    def open_menu(self):
        old_direction = self.team[0].direction
        self.team[0].direction = DIR_DOWN
        self.reset_animation_team()

        menu = continue_game = True
        pygame.key.set_repeat()
        while menu:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        menu = False
                    if event.key == K_DOWN:
                        self.cursor.move_down()
                    if event.key == K_UP:
                        self.cursor.move_up()
                    if event.key == K_RETURN:
                        if self.cursor.position.y == self.ypos[0]:
                            self.open_items()
                        if self.cursor.position.y == self.ypos[1]:
                            self.open_equipment()
                        if self.cursor.position.y == self.ypos[2]:
                            self.open_magic()
                        if self.cursor.position.y == self.ypos[3]:
                            self.open_status()
                        if self.cursor.position.y == self.ypos[4]:
                            self.save()
                        if self.cursor.position.y == self.ypos[5]:
                            menu = False
                        if self.cursor.position.y == self.ypos[6]:
                            menu = continue_game = False
                        

            self.buffer.blit(self.menu_image, (0,0))
            self.render_menu()
            self.render_team()
            self.render_cursor()
            pygame.transform.scale(self.buffer, self.screen.get_size(),
                                   self.screen)
            pygame.display.flip()
        # Loop end.

        pygame.key.set_repeat(1, 5)
        self.team[0].direction = old_direction
        self.team[0].update_now()

        return continue_game


    def render_menu(self):
        pos = self.ypos[0]
        for item in self.menu_items:
            rend = self.font.render(item, 0, TBK)
            self.buffer.blit(rend, (self.buffer.get_width() - 110, pos))
            pos += 25

    def render_cursor(self, animate=True):
        if animate:
            self.cursor.update()
        self.buffer.blit(self.cursor.image, self.cursor.position)

    def render_team(self, animate=True):
        pos = 1
        for char in self.team:
            self.render_char(char, pos, animate)
            pos += 1

    def reset_animation_team(self):
        for char in self.team:
            char.reset_animation()

    def render_char(self, char, pos, animate=True):
        if pos == 1:
            basey = 15
        if pos == 2:
            basey = 75
        if pos == 3:
            basey = 135
        if pos == 4:
            basey = 195
        if animate:
            char.update()

        sn = str(char.name)
        shp = "HP : " + str(char.stats.hp) + " / " + str(char.stats.maxhp)
        smp = "MP : " + str(char.stats.mp) + " / " + str(char.stats.maxmp)
        slv = "Level : " + str(char.stats.level)
        self.buffer.blit(char.image, pygame.Rect(20, basey, 32, 32))
        self.buffer.blit(self.font.render(sn, 0, TBK), (60, basey))
        self.buffer.blit(self.font.render(shp, 0, TBK), (210, basey))
        self.buffer.blit(self.font.render(smp, 0, TBK), (210, basey + 15))
        self.buffer.blit(self.font.render(slv, 0, TBK), (60, basey + 15))

    def save(self):
        # Save function goes here !
        popup = True
        while popup:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        popup = False

            self.buffer.blit(self.menu_image, (0,0))
            self.render_menu()
            self.render_team(animate=False)
            self.render_cursor(animate=False)
            self.buffer.blit(self.font.render("GAME SAVED", 0, TBK), (100, 500))

            pygame.transform.scale(self.buffer, self.screen.get_size(),
                                   self.screen)
            pygame.display.flip()

    def open_items(self):
        # Open Items
        menu = True
        positions = len(self.bag.useable)
        itemcursor = Cursor(ypos=[25, 85, 145, 205], xpos=[0, 50, 100])
        while menu:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        menu = False
                    if event.key == K_DOWN:
                        itemcursor.move_down()
                    if event.key == K_UP:
                        itemcursor.move_up()
                    if event.key == K_RIGHT:
                        itemcursor.move_right()
                    if event.key == K_LEFT:
                        itemcursor.move_left()

            self.buffer.blit(self.menu_image, (0,0))
            posy = 5
            for item in self.bag.useable:
                if item.quantity > 0:
                    sim = "%s x%s" % (item.name, item.quantity)
                    rend = self.font.render(sim, 0, TBK)
                    self.buffer.blit(rend, (5, posy))
                    posy += 10
            itemcursor.update()
            self.buffer.blit(itemcursor.image, itemcursor.position)
            pygame.transform.scale(self.buffer, self.screen.get_size(),
                                   self.screen)
            pygame.display.flip()
        # Loop end.

    def open_magic(self):
        # MAGIC ! TODO
        popup = True
        while popup:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        popup = False

            self.buffer.blit(self.menu_image, (0,0))
            self.render_menu()
            self.render_team(animate=False)
            self.render_cursor(animate=False)

            smc = "You don't have any magic... Yet..."
            self.buffer.blit(self.font.render(smc, 0, TBK), (100, 500))
            pygame.transform.scale(self.buffer, self.screen.get_size(),
                                   self.screen)
            pygame.display.flip()
        # Loop end.

    def open_equipment(self):
        # EQUIPMENT ! TODO
        popup = True
        while popup:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        popup = False

            self.buffer.blit(self.menu_image, (0,0))
            self.render_menu()
            self.render_team(animate=False)
            self.render_cursor(animate=False)

            seq = "You don't have any equipment..."
            sld = "(Yes I'm a lazy developper...)"
            self.buffer.blit(self.font.render(seq, 0, TBK), (100, 500))
            self.buffer.blit(self.font.render(sld, 0, TBK), (100, 515))
            pygame.transform.scale(self.buffer, self.screen.get_size(),
                                   self.screen)
            pygame.display.flip()
        # Loop end.

    def open_status(self):
        menu = True
        statuscursor = Cursor(ypos=[25, 85, 145, 205], xpos=[0])
        while menu:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        menu = False
                    if event.key == K_DOWN:
                        statuscursor.move_down()
                    if event.key == K_UP:
                        statuscursor.move_up()
                    if event.key == K_RETURN:
                        if statuscursor.position.y == 25:
                            self.status(self.team[0])
                        if statuscursor.position.y == 85:
                            self.status(self.team[1])
                        if statuscursor.position.y == 145:
                            self.status(self.team[2])
                        if statuscursor.position.y == 205:
                            self.status(self.team[3])

            self.buffer.blit(self.menu_image, (0,0))
            self.render_menu()
            self.render_team()
            statuscursor.update()
            self.buffer.blit(statuscursor.image, statuscursor.position)
            pygame.transform.scale(self.buffer, self.screen.get_size(), self.screen)
            pygame.display.flip()
        # Loop end.

    def status(self, char):
        menu = True
        while menu:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        menu = False

            self.buffer.blit(self.menu_image, (0,0))
            self.render_char(char, 1)
            self.buffer.blit(self.font.render("Skills", 0, TBK), (60, 45))
            self.buffer.blit(self.font.render("Stats", 0, TBK), (60, 60))
            self.buffer.blit(self.font.render("Strength : %d" % char.stats.str, 0, TBK), (60, 75))
            self.buffer.blit(self.font.render("Defense : %d" % char.stats.defense, 0, TBK), (300, 75))
            self.buffer.blit(self.font.render("Intelligence : %d" % char.stats.int, 0, TBK), (60, 90))
            self.buffer.blit(self.font.render("Magic Defense : %d" % char.stats.mdefense, 0, TBK), (300, 90))
            self.buffer.blit(self.font.render("Dexterity : %d" % char.stats.dex, 0, TBK), (60, 105))
            pygame.transform.scale(self.buffer, self.screen.get_size(), self.screen)
            pygame.display.flip()
        # Loop end.

        self.reset_animation_team()
        


