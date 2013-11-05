# -*- coding: utf-8 -*-
# File inventory.py

class Item(object):
	""" 
	The Item class
	"""
	def __init__(self, name="Potion", quantity=1, effect="Effect"):
		self.name = name
		self.quantity = quantity
		self.effect = effect

	def use(self):
		self.quantity -= 1
		print(self.effect)

	def add(self):
		self.quantity += 1

	def throw(self):
		self.quantity -= 1
		print("You thrown a %s item" % self.name)
		

class Bag(object):
	""" 
	A bag containing several objects.
	These objects are sorted in 3 categories
	"""
	def __init__(self):
		self.useable = [Item()]
		self.important = []
		self.notes = []
		self.equipment = []