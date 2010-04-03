#   File: destination.py
#   Author: Tom Woolfrey

import pygame;
from config import *;
from waypoint import *;

class Destination(Waypoint):

    def __init__(self, location, text):
        self.location = location
        self.text = text
        
        font = pygame.font.Font(None, 20)
        self.font_img = font.render(text, True, Config.DEST_COLOR)

    def draw(self, surface):
        pygame.draw.circle(surface, Config.DEST_COLOR, self.location, 5, 0)
        surface.blit(self.font_img, (self.location[0] + 8, self.location[1] + 8))

