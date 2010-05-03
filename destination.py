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

	# Must override this inherited method because Destination objects have no rect? 
	# When deleting a waypoint I get an error:
	##  File "C:\pyatc\game.py", line 77, in start
	##    self.__handleUserInteraction()
	##  File "C:\pyatc\game.py", line 201, in __handleUserInteraction
	##    if(w.clickedOn(event.pos) == True):
	##  File "C:\pyatc\waypoint.py", line 23, in clickedOn
	##    return (self.way_rect.inflate(15,15).collidepoint(clickpos))
	##  AttributeError: Destination instance has no attribute 'way_rect'
	# Does not fix the problem though... still get the same error
	def clickedOn(self, clickpos):
		return False
