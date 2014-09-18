import pygame
from .settings import DIR_DOWN, DIR_LEFT, DIR_RIGHT, DIR_RIGHT, DIR_UP, valid_dir
from .stats import Stats

class Hero(pygame.sprite.Sprite):
    """
    Our Fucking Nice Hero
    """

    def __init__(self, name="Angus", charset="../res/charsets/captain.png"):
        # Non displayable
        self.position = pygame.Rect(500, 500, 32, 32)
        #self.collidebox = pygame.Rect(self.position.x + 3,
        #                              self.position.y + 16, 26, 16)
        self.index = 0
        self.direction = DIR_DOWN
        self.UPDATE_TIME = 10
        self.timer = 0
        # In game Infos
        self.stats = Stats()
        self.name = name
        # Animations
        self.up_anim = []
        self.down_anim = []
        self.right_anim = []
        self.left_anim = []
        self.set_file(charset)
        self.image = self.down_anim[0]

    def reset_animation(self):
        self.index = 0
        self.timer = 0

    def extract_sprite(self, size, file, pos=(0, 0)):
        sheet = pygame.image.load(file).convert_alpha() 
        sheet_rect = sheet.get_rect()
        sheet.set_clip(pygame.Rect(pos[0]*size, pos[1]*size, size, size))
        return sheet.subsurface(sheet.get_clip())

    def set_file(self, newfile):
        """ Change the file for the char"""
        self.file = newfile
        self.down_anim = self.up_anim = self.left_anim = self.right_anim = []
        for x in range(0, 2):
            self.down_anim.append(self.extract_sprite(32, self.file, (x, DIR_DOWN)))
            self.up_anim.append(self.extract_sprite(32, self.file, (x, DIR_UP)))
            self.left_anim.append(self.extract_sprite(32, self.file, (x, DIR_LEFT)))
            self.right_anim.append(self.extract_sprite(32, self.file, (x, DIR_RIGHT)))

    @property
    def collidebox(self):
        if self.direction == DIR_DOWN:  # x+3 by default, here -2.  y+16 by default, here +2.
            return pygame.Rect(self.position.x+3, self.position.y+18, 26, 16)
        if self.direction == DIR_LEFT:
            return pygame.Rect(self.position.x+1, self.position.y+16, 26, 16)
        if self.direction == DIR_RIGHT: # x+3 by default, here +2.
            return pygame.Rect(self.position.x+5, self.position.y+16, 26, 16)
        if self.direction == DIR_UP:    #              y+16 by default, here -2.
            return pygame.Rect(self.position.x+3, self.position.y+14, 26, 16)

    def update(self, direction=None):
        if direction is None:
            direction = self.direction
        elif not valid_dir(direction):
            pass

        if self.direction != direction:
            self.direction = direction
            self.update_now()
        else:
            self.timer += 1
            if self.timer >= self.UPDATE_TIME:
                self.timer = 0
                self.update_now()

    def update_now(self):
        self.index += 1
        if self.index >= 2:
            self.index = 0
        if self.direction == DIR_DOWN:
            self.image = self.down_anim[self.index]
        elif self.direction == DIR_UP:
            self.image = self.up_anim[self.index]
        elif self.direction == DIR_LEFT:
            self.image = self.left_anim[self.index]
        elif self.direction == DIR_RIGHT:
            self.image = self.right_anim[self.index]

    def collidelist(self, collisionlist):
        return self.collidebox.collidelist(collisionlist)

    #def collide_neighbours(self, tiledmap): TODO


    def move(self, direction=None):
        if direction == None:
            direction = self.direction
        elif not valid_dir(direction):
            pass

        if direction == DIR_DOWN:
            self.position.y += 2
        elif direction == DIR_LEFT:
            self.position.x -= 2
        elif direction == DIR_RIGHT:
            self.position.x += 2
        else:
            self.position.y -= 2
