import pygame

class Cursor(object):
	""" A cursor object used in menus """
	def __init__(self, image="../res/images/hand.png", ypos=[500], xpos=[500]):
		# Cursor positionning
		self.ypos = ypos
		self.yposindex = 0
		self.xpos = xpos
		self.xposindex = 0
		self.position = pygame.Rect(self.xpos[self.xposindex], self.ypos[self.yposindex], 16, 16)
		# Animation
		self.index = 0
		self.update_time = 5
		self.timer = 0
		self.image = pygame.image.load(image).convert()


	def update(self):
		self.timer += 1
		self.position.y = self.ypos[self.yposindex]
		if self.timer > self.update_time:
			self.timer = 0
			if self.index in xrange(0,2):
				self.position.x += 1
			elif self.index in xrange(3,5):
				self.position.x -= 1
			self.index += 1
			if self.index == 10: self.index = 0

	def move_up(self):
		if self.yposindex > 0:
			self.yposindex -= 1
		else:
			self.yposindex = len(self.ypos)-1

	def move_down(self):
		if self.yposindex+1 < len(self.ypos):
			self.yposindex += 1
		else:
			self.yposindex = 0

