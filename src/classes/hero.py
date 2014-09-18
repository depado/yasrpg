import pygame
from .settings import DIRECTIONS
from .stats import Stats

class Hero(pygame.sprite.Sprite):
    """
    Our Fucking Nice Hero
    """

    def __init__(self, name="Angus", charset="../res/charsets/captain.png"):
        # Non displayable
        self.position = pygame.Rect(500, 500, 32, 32)
        self.collision = pygame.Rect(self.position.x + 3,
                                     self.position.y + 16, 26, 16)
        self.index = 0
        self.direction = DIRECTIONS['down']
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

    def extract_sprite(self, size, file, pos=(0,0)):
        sheet = pygame.image.load(file).convert_alpha() 
        sheet_rect = sheet.get_rect()
        sheet.set_clip(pygame.Rect(pos[0]*size, pos[1]*size, size, size))
        sprite = sheet.subsurface(sheet.get_clip())
        return sprite

    def set_file(self, newfile):
        """ Change the file for the char"""
        self.file = newfile
        for x in range(0,2):
            self.down_anim.append(self.extract_sprite(32, self.file, (x, DIRECTIONS['down'])))
            self.up_anim.append(self.extract_sprite(32, self.file, (x, DIRECTIONS['up'])))
            self.left_anim.append(self.extract_sprite(32, self.file, (x, DIRECTIONS['left'])))
            self.right_anim.append(self.extract_sprite(32, self.file, (x, DIRECTIONS['right'])))

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