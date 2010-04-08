#   File: aircraft.py

import math;
import pygame;
import os;
from config import *;
from waypoint import *;
from game import *;

class Aircraft:

	#Constructor!
    def __init__(self, location, speed, destination):
        self.location = location;
        self.speed = speed
        self.waypoints = []
        self.waypoints.append(destination)
        self.selected = False
        self.heading = self.__calculateHeading(self.location, self.waypoints[0].getLocation())
        self.image_normal = pygame.image.load(os.path.join('data', 'aircraft.png'))
        self.image_normal.convert_alpha()
        self.image_sel = pygame.image.load(os.path.join('data', 'aircraft_sel.png'))
        self.image_sel.convert_alpha()
        self.image = self.image_normal

	#Add a new waypoint in the specified index in the list
    def addWaypoint(self, waypoint, index=0):
        if((len(self.waypoints) - 1) <= Config.MAX_WAYPOINTS):
            self.waypoints.insert(index, Waypoint(waypoint))
            self.heading = self.__calculateHeading(self.location, self.waypoints[0].getLocation())
	
	#Get the specified waypoint from the list
	def getWaypoint(self, index):
		return self.waypoints[index]

	#Set speed in pixels per frame
	def setSpeed(self, newspeed):
		self.speed = newspeed

    def setSelected(self, selected):
        self.selected = selected
        if(selected == True):
            self.image = self.image_sel
        else:
            self.image = self.image_normal

    def getLocation(self):
        return self.location

	#Draw myself on the screen at my current position and heading
    def draw(self, surface):
        rot_image = pygame.transform.rotate(self.image, -self.heading)
        rect = rot_image.get_rect()
        rect.center = self.location
        surface.blit(rot_image, rect)

        if(Config.AC_DRAW_COLLISION_RADIUS == True):
            pygame.draw.circle(surface, (255, 255, 0), self.location, Config.AC_COLLISION_RADIUS, 1)

        #Draw lines and waypoints if selected
        if(self.selected == True):
            point_list = []
            point_list.append(self.location)
            for x in range(0, len(self.waypoints)-1):
                point_list.append(self.waypoints[x].getLocation())
                way_rect = pygame.Rect(self.waypoints[x].getLocation()[0], self.waypoints[x].getLocation()[1], 7, 7)
                way_rect.center = self.waypoints[x].getLocation()
                pygame.draw.rect(surface, (0, 0, 255), way_rect, 0)
            point_list.append(self.waypoints[-1].getLocation())
            pygame.draw.aalines(surface, (0, 0, 255), False, point_list)

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
        #if(self.location[0] < 0 or self.location[0] > Game.AERIALPANE_W or self.location[1] < 0 or self.location[1] > Game.AERIALPANE_H):
        #    return True
        #else:
        #    return False

    def clickedOn(self, click):
        x_sq = (click[0] - self.location[0]) ** 2
        y_sq = (click[1] - self.location[1]) ** 2
        if math.sqrt( x_sq + y_sq ) < 10:
            return True
        else:
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
