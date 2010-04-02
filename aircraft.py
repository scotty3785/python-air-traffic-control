#   File: aircraft.py

import math;
import pygame;

class Aircraft:

	#Constructor!
    def __init__(self, location, speed, destination):
        self.location = location;
		self.speed = 0
		self.waypoints = []
		self.waypoints.append(destination)
		self.image = image.load('data/aircraft.png')

	#Add a new waypoint in the specified index in the list
	def addWaypoint(self, waypoint, index):
		if((len(self.waypoints) - 1) <= Config.MAX_WAYPOINTS):
			self.waypoints.insert(index, waypoint)
	
	#Get the specified waypoint from the list
	def getWaypoint(self, index):
		return self.waypoints[index]

	#Set speed in pixels per frame
	def setSpeed(self, newspeed):
		self.speed = newspeed

	#Draw myself on the screen at my current position and heading
    def draw(self):
        rot_image = pygame.transform.rotate(self.image, -self.heading)
		screen.blit(rot_image, self.location)

	#Location/heading update function
	def update(self):
		if(self.__reachedWaypoint(self.location, self.waypoints[0])):
			self.waypoints.pop()
			self.heading = self.__calculateHeading(self.location, self.waypoints[0])
		else:
			self.location = self.__calcNewLocation(self.location)


	def __calculateHeading(self, location, waypoint):
		x_diff = waypoint[0] - location[0]
		y_diff = waypoint[1] - location[1]
		self.heading = math.degrees(math.atan2(x_diff, y_diff))
		return heading

	def __calculateNewLocation(self, location, heading, speed):
		#TODO - Get from Scott

	def __reachedWaypoint(self, location, waypoint):
		#TODO - Get from Scott
		
