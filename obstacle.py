#	File: obstacle.py

import pygame;

class Obstacle:

    TYPE_WEATHER = 0
    TYPE_NOFLY = 1
    TYPE_MOUNTAIN = 2
    TYPE_ASHCLOUD = 3

    def __init__(self, obs_type, bounds):
        self.bounds = bounds
        self.type = obs_type

    def getBounds(self):
        return self.bounds

    def getType(self):
        return self.type

    def draw(self, surface):
        pygame.draw.aalines(surface, (255, 0, 0), True, self.bounds)
        
    def isPointInside(self, point):
        return False
