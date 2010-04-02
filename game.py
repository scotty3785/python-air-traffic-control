#   File: game.py
#   Description: An instance of one game of ATC

import random;
from config import *;
from destination import *;

class Game:

    AERIALPANE_W = 850;
    AERIALPANE_H = 768;

    def __init__(self, screen):
        self.screen = screen
        self.ms_elapsed = 0
        self.score = 0
		self.aircraft = []

        self.__generateDestinations()
        self.__generateAircraftSpawnEvents()

    def start(self):
        clock = pygame.time.clock()
		gameEnd = 0

        #The main game loop
        while gameEnd == 0:
            timepassed = clock.tick(Config.FPS)
            self.ms_elapsed = self.ms_elapsed + timepassed

            self.__update()
            self.__checkForUserInteraction()

			if((self.ms_elapsed / 1000) >= Config.GAMETIME):
				gameEnd = 1
            
            
    def __update(self):
        #Things to do here:
        #1: Update the positions of all existing aircraft
        #2: Check if any aircraft have collided with an obstacle
        #3: Check if any aircraft have reached a destination
        #4: Spawn new aircraft
        for a in self.aircraft:
			x.update()
			x.draw()
			for o in self.obstacles:
				self.__checkCollision(a, o)

    def __updateAircraftPositions(self):
        for x in self.aircraft:
            #Do some shizzle
            pass

    def __generateAircraftSpawnEvents(self):
        for x in range(0, Config.NUMBEROFAIRCRAFT):
            randtime = random.randint(1, Config.GAMETIME)
            randspawn = __generateRandomSpawnPoint();
            randdest = random.randint(0, Config.NUMBEROFDESTINATIONS)
            spawnevent = AircraftSpawnEvent(randtime, randspawn, randdest)
            self.aircraftspawns.append(spawn)

    def __generateDestinations(self):
        for x in range(0, Config.NUMBEROFDESTINATIONS):
            randx = random.gammavariate( Game.AERIALPANE_W/2, Game.AERIALPANE_W/6 )
            randy = random.randint(-Game.AERIALPANE_H/2, Game.AERIALPANE_H/6)
            dest = Destination(randx, randy)
            self.destinations.append(dest)

    def __generateRandomSpawnPoint(self):
        side = random.randint(1, 4)
        if side == 1:
            loc = (random.randint(0, Game.AERIALPANE_W), 0)
        elif side == 2:
            loc = (Game.AERIALPANE_W, random.randint(-Game.AERIALPANE_H, 0))
        elif side == 3:
            loc = (random.randint(0, Game.AERIALPANE_W), -Game.AERIALPANE_H)
        elif side == 4:
            loc = (0, random.randint(-Game.AERIALPANE_H, 0))
        return loc

	def __checkCollision(self, ac, obs):
		if( 

