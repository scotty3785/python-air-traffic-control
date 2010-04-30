#   File: destination.py
#   Author: Tom Woolfrey

import pygame;
from config import *;
from waypoint import *;

class Destination(Waypoint):

    COLOR_DEST = (192, 192, 192)

    def __init__(self, location, text):
        self.location = location
        self.text = text
        font = pygame.font.Font(None, 20)
        self.font_img = font.render(text, True, Destination.COLOR_DEST)

    def draw(self, surface):
        pygame.draw.circle(surface, Destination.COLOR_DEST, self.location, 5, 0)
        surface.blit(self.font_img, (self.location[0] + 8, self.location[1] + 8))
