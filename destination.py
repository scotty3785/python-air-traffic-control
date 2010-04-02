#   File: destination.py
#   Author: Tom Woolfrey

import pygame;

class Destination:

    DEST_COLOR = (160, 160, 160)

    def __init__(self, x, y, text):
        self.location = (x, y)
        self.text = text
        self.font = pygame.font.Font(None, 20)

    def draw(self, surface):
        pygame.draw.circle(surface, DEST_COLOR, self.location, 2, 0)
        self.font.render(text, True, (DEST_COLOR), None)
        
