#   File: aircraft.py

import math;
import pygame;
import os;
import string;
from config import *;
from waypoint import *;
from game import *;
from utility import *;

class Aircraft:

    AC_IMAGE_NORMAL = pygame.image.load(os.path.join('data', 'aircraft.png'))
    AC_IMAGE_SELECTED = pygame.image.load(os.path.join('data', 'aircraft_sel.png'))

    FS_IMAGE_SPEED_UP = pygame.image.load(os.path.join('data', 'arrow_up.png'))
    FS_IMAGE_SPEED_DOWN = pygame.image.load(os.path.join('data', 'arrow_down.png'))

    FS_FONTSIZE = 18
    FS_FONT_COLOR_NORMAL = (255, 255, 255)
    FS_FONT_COLOR_SELECTED = (50, 255, 50)
    FS_BG_COLOR_NORMAL = (60, 60, 60)
    FS_BG_COLOR_SELECTED = (60, 40, 255)

	#Constructor!
    def __init__(self, location, speed, destination, ident):

        #Game state vars
        self.location = location;
        self.speed = speed
        self.altitude = 24000 # hardwired for now; measured in ft
        self.waypoints = []
        self.waypoints.append(destination)
        self.ident = ident
        self.selected = False
        self.heading = self.__calculateHeading(self.location, self.waypoints[0].getLocation())

        Aircraft.AC_IMAGE_NORMAL.convert_alpha()
        Aircraft.AC_IMAGE_SELECTED.convert_alpha()
        Aircraft.FS_IMAGE_SPEED_UP.convert_alpha()
        Aircraft.FS_IMAGE_SPEED_DOWN.convert_alpha()

        #Image/font vars
        self.image = Aircraft.AC_IMAGE_NORMAL
        self.font = pygame.font.Font(None, Aircraft.FS_FONTSIZE)
        self.fs_bg_color = Aircraft.FS_BG_COLOR_NORMAL
        self.fs_font_color = Aircraft.FS_FONT_COLOR_NORMAL

	#Add a new waypoint in the specified index in the list
    def addWaypoint(self, waypoint, index=0):
        if((len(self.waypoints) - 1) <= Config.MAX_WAYPOINTS):
            self.waypoints.insert(index, Waypoint(waypoint))
            self.heading = self.__calculateHeading(self.location, self.waypoints[0].getLocation())
	
	#Get the specified waypoint from the list
	def getWaypoint(self, index):
		return self.waypoints[index]

    def getWaypoints(self):
        return self.waypoints

    #Return current location
    def getLocation(self):
        return self.location

    #Return current heading
    def getHeading(self):
        return self.heading

	#Set speed in pixels per frame
	def setSpeed(self, newspeed):
		self.speed = newspeed

    #Set whether I am the selected aircraft or not
    def setSelected(self, selected):
        self.selected = selected
        if(selected == True):
            self.image = Aircraft.AC_IMAGE_SELECTED
            self.fs_font_color = Aircraft.FS_FONT_COLOR_SELECTED
            self.fs_bg_color = Aircraft.FS_BG_COLOR_SELECTED
        else:
            self.image = Aircraft.AC_IMAGE_NORMAL
            self.fs_font_color = Aircraft.FS_FONT_COLOR_NORMAL
            self.fs_bg_color = Aircraft.FS_BG_COLOR_NORMAL

	#Draw myself on the screen at my current position and heading
    def draw(self, surface, index):
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
                self.waypoints[x].draw(surface)
            point_list.append(self.waypoints[-1].getLocation())
            pygame.draw.aalines(surface, (0, 0, 255), False, point_list)


		# Draw the ident string next to the aircraft?
        x = self.location[0] + 20
        y = self.location[1] + 20
        #list = string.split(self.ident,"\n")
        list = [self.ident, "FL" + str(self.altitude/100), str(self.speed * Config.AC_SPEED_SCALEFACTOR) + "kts"]
        list.reverse()
        for line in list:
			id = self.font.render(line, False, self.fs_font_color)
			r = surface.blit(id, (x,y))
			y = y - self.font.get_height()

        #Draw flightstrip
        self.__drawFlightstrip(surface, index)

	#Location/heading update function
    def update(self):
        if(self.__reachedWaypoint(self.location, self.waypoints[0].getLocation())):
            #Reached next waypoint, pop it
            self.waypoints.pop(0)
            if( len(self.waypoints) == 0):
                #Reached destination, return True
                return True
		
		#Keep moving towards waypoint
        self.heading = self.__calculateHeading(self.location, self.waypoints[0].getLocation())
        self.location = self.__calculateNewLocation(self.location, self.heading, self.speed)

    def getClickDistanceSq(self, clickpos):
        return Utility.locDistSq(clickpos, self.location)

    def clickedOnFlightstrip(self, clickpos, index):
        top = 152 + (index * 50)
        bottom = 152 + ((index + 1) * 50) - 1
        if (clickpos[0] >= 798) and (top <= clickpos[1] <= bottom):
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
        if Utility.locDistSq(location, waypoint) < (self.speed ** 2):
            return True
        else:
            return False

    #Draw my flight strip at the given list index position
    def __drawFlightstrip(self, surface, index):
        #Calc bounds
        left = 798
        top = 152 + (index * 50)
        bottom = 152 + ((index + 1) * 50) - 1

        #Draw bottom line
        pygame.draw.line(surface, (255, 255, 255), (left, bottom), (1023, bottom), 1)

        #Draw background
        pygame.draw.rect(surface, self.fs_bg_color, pygame.Rect(left, top, 226, 49), 0)

        #Draw ident
        srf_ident = self.font.render(self.ident, False, self.fs_font_color)
        surface.blit(srf_ident, (left + 5, top + 4))

        #Draw speed
        srf_speed = self.font.render(str(self.speed * Config.AC_SPEED_SCALEFACTOR) + "kts", False, self.fs_font_color)
        surface.blit(srf_speed, (left + 5, top + 26))
