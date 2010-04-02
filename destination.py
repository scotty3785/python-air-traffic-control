#   File: destination.py
#   Author: Tom Woolfrey

import pygame;
from config import *;

class Destination:

    def __init__(self, x, y, text):
        self.location = (x, y)
        self.text = text
        
        font = pygame.font.Font(None, 20)
        self.font_img = font.render(text, True, Config.DEST_COLOR)

    def draw(self, surface):
        pygame.draw.circle(surface, Config.DEST_COLOR, self.location, 2, 0)
        surface.blit(self.font_img, (self.location[0] + 8, self.location[1] + 8))
        
