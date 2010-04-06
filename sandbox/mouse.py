#!/usr/bin/env python
"""
Demonstrate how the mouse events are used in pygame
Create waypoints and link them with a line
"""

#Import Modules
import os, pygame
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'


#functions to create our resources
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class Waypoint(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = load_image('asprite.bmp', -1)
		self.pos = pygame.mouse.get_pos()
		print "New waypoint inserted at:", self.pos
		self.rect.center = self.pos
		self.clicked = False

	def update(self):
		# Must change at least rect or image attribute to cause 
		# sprite to be displayed
		if self.clicked:
			self.pos = pygame.mouse.get_pos()
			self.rect.center = self.pos
			pass

	def click(self):
		self.clicked = True

	def unclick(self):
		self.clicked = False


def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
#Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((468, 468))
    pygame.display.set_caption('Mouse test')
    pygame.mouse.set_cursor(*pygame.cursors.diamond)
    pygame.mouse.set_visible(1)

#Create The Backgound
    background = pygame.Surface(screen.get_size())
    background = background.convert()
	# Set the background colour
    background.fill((0, 100, 0))
    
#Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()
    
#Prepare Game Objects
    clock = pygame.time.Clock()
	# Create a group/container for all the waypoint sprites to be drawn
    waypoints = pygame.sprite.RenderUpdates()

    all_waypoints = []
    
#Main Loop
    while 1:
        clock.tick(60)

    #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == MOUSEBUTTONDOWN:
				# Check if clicked on an existing waypoint
				sprites_clicked = [sprite for sprite in all_waypoints if sprite.rect.collidepoint(pygame.mouse.get_pos())]
				print sprites_clicked
				# If not, then create a new one
				if (not sprites_clicked):
					w = Waypoint()
					waypoints.add(w)
					all_waypoints.append(w)
				else:
					print "sprite already exists"
					sprites_clicked[0].click()
            elif event.type == MOUSEBUTTONUP:
                #fist.unpunch()
				if (sprites_clicked):
					sprites_clicked[0].unclick()
				pass

        waypoints.update()

    #Draw Everything
        screen.blit(background, (0, 0))
        waypoints.draw(screen)
        pygame.display.flip()

#Game Over


#this calls the 'main' function when this script is executed
if __name__ == '__main__': main()
