# -*- coding: utf-8 -*-
# File menu.py

import pygame
from pygame.locals import *
from cursor import Cursor
from settings import IMAGES_DIR, DIRECTIONS, FONT, FONT_SIZE

class Menu(object):
    """docstring for Menu"""
    def __init__(self, screen, team, bag):
        self.clock = pygame.time.Clock()
        self.team = team
        self.bag = bag
        self.screen = screen
        self.buffer = pygame.Surface(self.screen.get_size())
        self.font = pygame.font.Font(FONT, FONT_SIZE)
        self.menu_items = ['Items','Equip','Magic','Status','Save','Close','Quit']
        self.menu_image = pygame.image.load(IMAGES_DIR+'menu.png').convert_alpha()
        self.cursor = Cursor(ypos=[5,30,55,80,105,130,155])
        self.blitable = []

        
    def open_menu(self):
        old_direction = self.team[0].direction
        self.team[0].direction = DIRECTIONS['down']
        self.reset_animation_team()
        menu = continue_game = True
        pygame.key.set_repeat()
        while menu:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        menu = False
                    if event.key == K_DOWN:
                        self.cursor.move_down()
                    if event.key == K_UP:
                        self.cursor.move_up()
                    if event.key == K_RETURN:
                        if self.cursor.position.y == 5:
                            self.open_items()
                        if self.cursor.position.y == 30:
                            self.open_equipment()
                        if self.cursor.position.y == 55:
                            self.open_magic()
                        if self.cursor.position.y == 80:
                            self.open_status()
                        if self.cursor.position.y == 105:
                            self.save()
                        if self.cursor.position.y == 130:
                            menu = False
                        if self.cursor.position.y == 155:
                            menu = continue_game = False

            self.buffer.blit(self.menu_image, (0,0))
            self.render_menu()
            self.render_team()
            self.render_cursor()
            pygame.transform.scale(self.buffer, self.screen.get_size(), self.screen)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.key.set_repeat(1,5)
        self.team[0].direction = old_direction
        self.team[0].update_now()

        return continue_game


    def render_menu(self):
        pos = 5
        for item in self.menu_items:
            self.buffer.blit(self.font.render(item, 0, (255,255,255)), (self.buffer.get_width()-110,pos))
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
        self.buffer.blit(char.image, pygame.Rect(20, basey, 32, 32))
        self.buffer.blit(self.font.render(str(char.name), 0,(255,255,255)), (60, basey))
        self.buffer.blit(self.font.render("HP : "+str(char.stats.hp)+" / "+str(char.stats.maxhp), 0,(255,255,255)), (210, basey))
        self.buffer.blit(self.font.render("MP : "+str(char.stats.mp)+" / "+str(char.stats.maxmp), 0,(255,255,255)), (210, basey+15))
        self.buffer.blit(self.font.render("Level : "+str(char.stats.level), 0,(255,255,255)), (60, basey+15))

    def save(self):
        # Save function goes here !
        popup = True
        while popup:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        popup = False

            self.buffer.blit(self.menu_image, (0,0))
            self.render_menu()
            self.render_team(animate=False)
            self.render_cursor(animate=False)
            self.buffer.blit(self.font.render("GAME SAVED", 0,(255,255,255)), (100, 500))
            pygame.transform.scale(self.buffer, self.screen.get_size(), self.screen)
            pygame.display.flip()
            self.clock.tick(60)

    def open_items(self):
        # Open Items
        menu = True
        positions = len(self.bag.useable)
        itemcursor = Cursor(ypos=[25, 85, 145, 205], xpos=[0, 50, 100])
        while menu:
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
                    self.buffer.blit(self.font.render("%s x%s" % (item.name, item.quantity), 0,(255,255,255)), (5, posy))
                    posy += 10
            itemcursor.update()
            self.buffer.blit(itemcursor.image, itemcursor.position)
            pygame.transform.scale(self.buffer, self.screen.get_size(), self.screen)
            pygame.display.flip()
            self.clock.tick(60)


    def open_magic(self):
        # MAGIC ! TODO
        popup = True
        while popup:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        popup = False

            self.buffer.blit(self.menu_image, (0,0))
            self.render_menu()
            self.render_team(animate=False)
            self.render_cursor(animate=False)
            self.buffer.blit(self.font.render("You don't have any magic... Yet...", 0,(255,255,255)), (100, 500))
            pygame.transform.scale(self.buffer, self.screen.get_size(), self.screen)
            pygame.display.flip()
            self.clock.tick(60)

    def open_equipment(self):
        # EQUIPMENT ! TODO
        popup = True
        while popup:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        popup = False

            self.buffer.blit(self.menu_image, (0,0))
            self.render_menu()
            self.render_team(animate=False)
            self.render_cursor(animate=False)
            self.buffer.blit(self.font.render("You don't have any equipment...", 0,(255,255,255)), (100, 500))
            self.buffer.blit(self.font.render("(Yes I'm a lazy developper...)", 0,(255,255,255)), (100, 515))
            pygame.transform.scale(self.buffer, self.screen.get_size(), self.screen)
            pygame.display.flip()
            self.clock.tick(60)

    def open_status(self):
        menu = True
        statuscursor = Cursor(ypos=[25, 85, 145, 205], xpos=[0])
        while menu:
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
            self.clock.tick(60)

    def status(self, char):
        menu = True
        while menu:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        menu = False

            self.buffer.blit(self.menu_image, (0,0))
            self.render_char(char, 1)
            self.buffer.blit(self.font.render("Skills", 0,(255,255,255)), (60, 45))
            self.buffer.blit(self.font.render("Stats", 0,(255,255,255)), (60, 60))
            self.buffer.blit(self.font.render("Strength : %d" % char.stats.str, 0,(255,255,255)), (60, 75))
            self.buffer.blit(self.font.render("Defense : %d" % char.stats.defense, 0,(255,255,255)), (300, 75))
            self.buffer.blit(self.font.render("Intelligence : %d" % char.stats.int, 0,(255,255,255)), (60, 90))
            self.buffer.blit(self.font.render("Magic Defense : %d" % char.stats.mdefense, 0,(255,255,255)), (300, 90))
            self.buffer.blit(self.font.render("Dexterity : %d" % char.stats.dex, 0,(255,255,255)), (60, 105))
            pygame.transform.scale(self.buffer, self.screen.get_size(), self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        self.reset_animation_team()
        


