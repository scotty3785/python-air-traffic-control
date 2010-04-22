#   File: flightstrip.py

import pygame;

class Flightstrip:

    def __init__(self, aircraft, index, text):
        self.aircraft = aircraft
        self.text = text
        self.index = index
        self.selected = False

    def setIndex(self, index):
        self.index = index
        self.top = 152 + (self.index * 50)
        self.bottom = 152 + ((self.index + 1) * 50) - 1

    def draw(self, surface):
        pygame.draw.line(surface, (255, 255, 255), (795, self.bottom), (1023, self.bottom), 1)

    def setSelected(self, selected):
        self.selected = selected
        
