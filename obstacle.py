#	File: obstacle.py

class Obstacle:

	TYPE_WEATHER = 0
	TYPE_NOFLY = 1
	TYPE_MOUNTAIN = 2

	def __init__(self, type, location, size):
		self.location = location
		self.size = size

	def getLocation(self):
		return self.location

	def getSize(self):
		return self.size

	def getType(self):
		return self.type
