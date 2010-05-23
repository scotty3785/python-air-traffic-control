#	File: obstacle.py

import pygame;
import os;
import random;
from config import *;

class Obstacle:

    TYPE_WEATHER = 0
    TYPE_MOUNTAIN = 1

    def __init__(self, obs_type, location):
        self.location = location
        self.type = obs_type
        self.colliding = []
        if(self.type == Obstacle.TYPE_WEATHER):
            self.image = pygame.image.load(os.path.join('data', 'obs_weather.png'))
        elif(self.type == Obstacle.TYPE_MOUNTAIN):
            self.image = pygame.image.load(os.path.join('data', 'obs_mountain.png'))
            
        self.mask = pygame.mask.from_surface(self.image)

    def getType(self):
        return self.type

    def draw(self, surface):
        surface.blit(self.image, self.location)
        
    def collideAircraft(self, aircraft):
        newCollides = 0
        for a in aircraft:
            currCollide = self.__isColliding(a)
            if(a in self.colliding):
                prevCollide = True
            else:
                prevCollide = False
            if(currCollide == True and prevCollide == False):
                self.colliding.append(a)
                newCollides += 1
            elif(currCollide == False and prevCollide == True):
                self.colliding.remove(a)
        return newCollides
            
    def __isColliding(self, ac):
        collide = False
        rect = self.image.get_rect()
        rect.topleft = self.location
        #Don't bother with the masky stuff if the ac is outside rect
        if(rect.collidepoint(ac.getLocation()) == True):
            acLocOffsetX = int(ac.getLocation()[0] - rect.left)
            acLocOffsetY = int(ac.getLocation()[1] - rect.top)
            if(self.mask.get_at((acLocOffsetX, acLocOffsetY)) != 0):
                collide = True
        return collide
        
    @staticmethod
    def generateGameObstacles(screen_w, screen_h):
        ret = []
        for x in range(0, Config.NUMBEROFOBSTACLES):
            randx = random.randint( 40, screen_w - 100 )
            randy = random.randint( 40, screen_h - 80 )
            randtype = random.randint(0, 1)
            obstacle = Obstacle(randtype, (randx, randy))
            ret.append(obstacle)
        return ret
