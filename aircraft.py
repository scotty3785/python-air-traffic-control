#   File: aircraft.py

import math;
import pygame;
import os;
from config import *;
from waypoint import *;

class Aircraft:

	#Constructor!
    def __init__(self, location, speed, destination):
        self.location = location;
        self.speed = speed
        self.waypoints = []
        self.waypoints.append(destination)
        self.heading = self.__calculateHeading(self.location, self.waypoints[0].getLocation())
        self.image = pygame.image.load(os.path.join('data', 'aircraft.png'))
        self.image.convert_alpha()

	#Add a new waypoint in the specified index in the list
    def addWaypoint(self, waypoint, index):
        if((len(self.waypoints) - 1) <= Config.MAX_WAYPOINTS):
            self.waypoints.insert(index, Waypoint(waypoint))
            self.heading = self.__calculateHeading(self.location, self.waypoints[0].getLocation())
	
	#Get the specified waypoint from the list
	def getWaypoint(self, index):
		return self.waypoints[index]

	#Set speed in pixels per frame
	def setSpeed(self, newspeed):
		self.speed = newspeed

	#Draw myself on the screen at my current position and heading
    def draw(self, surface):
        rot_image = pygame.transform.rotate(self.image, -self.heading)
        rect = rot_image.get_rect()
        rect.center = self.location
        surface.blit(rot_image, rect)

        if(Config.AC_DRAW_COLLISION_RADIUS == True):
            pygame.draw.circle(surface, (255, 255, 0), self.location, Config.AC_COLLISION_RADIUS, 1)

	#Location/heading update function
    def update(self):
        if(self.__reachedWaypoint(self.location, self.waypoints[0].getLocation())):
            #Reached next waypoint, pop it
            self.waypoints.pop(0)
            if( len(self.waypoints) == 0):
                #Reached destination, return True
                return True
            else:
                self.heading = self.__calculateHeading(self.location, self.waypoints[0].getLocation())
		
		#Keep moving towards waypoint
        self.location = self.__calculateNewLocation(self.location, self.heading, self.speed)
        return False

	#Calculate heading based on current position and waypoint
    def __calculateHeading(self, location, waypoint):
        x_diff = waypoint[0] - location[0]
        y_diff = waypoint[1] - location[1]
        heading = math.degrees(math.atan2(y_diff, x_diff) + (math.pi / 2))
        return heading

	#Calculate new location based on current location, heading and speed
    def __calculateNewLocation(self, location, heading, speed):
        x_diff = speed * math.sin(math.radians(heading))
        y_diff = -speed * math.cos(math.radians(heading))
        location = (location[0] + x_diff, location[1] + y_diff)
        return location

	#Check whether I have reached the given waypoint
    def __reachedWaypoint(self, location, waypoint):
        x = (location[0] - waypoint[0])**2
        y = (location[1] - waypoint[1])**2
        distance = math.sqrt(x+y)
        if distance < 2:
            return True
        else:
            return False
