#	File: obstacle.py

import pygame;
import os;

class Obstacle:

    TYPE_WEATHER = 0
    TYPE_NOFLY = 1
    TYPE_MOUNTAIN = 2

    def __init__(self, obs_type, location):
        self.location = location
        self.type = obs_type
        self.colliding = []
        if(self.type == Obstacle.TYPE_WEATHER):
            self.image = pygame.image.load(os.path.join('data', 'obs_weather.png'))
        elif(self.type == Obstacle.TYPE_NOFLY):
            self.image = pygame.image.load(os.path.join('data', 'obs_nofly.png'))
        elif(self.type == Obstacle.TYPE_MOUNTAIN):
            self.image = pygame.image.load(os.path.join('data', 'obs_mountain.png'))
            
        self.image_mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

    def getType(self):
        return self.type

    def draw(self, surface):
        surface.blit(self.image, self.location)
        
    def collideAircraft(self, aircraft):
        newCollides = 0
        for a in aircraft:
            currCollide = self.__isColliding(a)
            prevCollide = (a in self.colliding)
            if(currCollide == True and prevCollide == False):
                self.colliding.append(a)
                newCollides += 1
            elif(currCollide == False and prevCollide == True):
                self.colliding.remove(a)
        return newCollides
            
    def __isColliding(self, ac):
        collide = False
        #Don't bother with the masky stuff if the ac is outside rect
        if(self.rect.collidepoint(ac.getLocation()) == True):
            #AC is within rect
            acLocOffsetX = ac.getLocation()[0] - self.rect.left
            acLocOffsetY = ac.getLocation()[1] - self.rect.top
            if(self.mask.get_at((acLocOffsetX, acLocOffsetY)) != 0):
                collide = True
        return collide
