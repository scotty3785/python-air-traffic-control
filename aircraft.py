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
        self.image = pygame.image.load(os.path.join('data', 'aircraft.png'))
        self.image.convert_alpha()
        self.recta = self.image.get_rect()

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
    def draw(self, surface):
        rot_image = pygame.transform.rotate(self.image, -self.heading)
        self.recta.center = self.location
        surface.blit(rot_image, self.location)

	#Location/heading update function
	def update(self):
		if(self.__reachedWaypoint(self.location, self.waypoints[0])):
			#Reached next waypoint, pop it
			self.waypoints.pop()
			if( len(self.waypoints) == 0):
				#Reached destination, return True
				return True
			else:
				#Not reached destination, return False
				self.heading = self.__calculateHeading(self.location, self.waypoints[0])
				return False
		
		#Keep moving
		self.location = self.__calcNewLocation(self.location)

	#Calculate heading based on current position and waypoint
	def __calculateHeading(self, location, waypoint):
		x_diff = waypoint[0] - location[0]
		y_diff = waypoint[1] - location[1]
		self.heading = math.degrees(math.atan2(x_diff, y_diff))
		return heading

	#Calculate new location based on current location, heading and speed
	def __calculateNewLocation(self, location, heading, speed):
		x_diff = speed * math.cos(math.radians(heading))
		y_diff = speed * math.sin(math.radians(heading))
		location[0] += x_diff
		location[1] += y_diff

	#Check whether I have reached the given waypoint
	def __reachedWaypoint(self, location, waypoint):
		x = (location[0] - waypoint[0])**2
		y = (location[1] - waypoint[1])**2
		distance = math.sqrt(x+y)
		if distance < 5:
			return True
		else:
			return False
