# -*- coding: utf-8 -*-
# File stats.py

class Stats(object):
	"""docstring for Stats"""
	def __init__(self, classname="Warrior"):
		self.classname = classname
		self.level = 1
		self.maxhp = 20
		self.hp = 20
		self.maxmp = 5
		self.mp = 5
		self.str = 1
		self.int = 1
		self.dex = 1
		self.defense = 1
		self.mdefense = 1
		# create_stats(self.classname)

	def create_stats(self, classname, level):
		pass
		# Parsing XML
		# 
		