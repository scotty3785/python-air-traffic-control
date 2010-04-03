#   File: game.py
#   Description: An instance of one game of ATC

import pygame;
import random;
from config import *;
from destination import *;
from aircraft import *;
from aircraftspawnevent import *;

class Game:

    AERIALPANE_W = 850;
    AERIALPANE_H = 768;

    def __init__(self, screen):
        self.background = pygame.image.load(os.path.join('data', 'backdrop.png'))
        self.screen = screen
        self.ms_elapsed = 0
        self.score = 0
        self.aircraft = []
        self.obstacles = []
        self.destinations = []
        self.aircraftspawns = []
        self.__generateDestinations()
        self.__generateAircraftSpawnEvents()

    def start(self):
        clock = pygame.time.Clock()
        gameEnd = 0
        i = 0 
        #The main game loop
        while gameEnd == 0:
            timepassed = clock.tick(Config.FRAMERATE)

            self.screen.blit(self.background, (0, 0))


            for x in self.destinations:
                x.draw(self.screen)

            self.__update()
            #self.__checkForUserInteraction()
            
            #Recalc time
            self.ms_elapsed = self.ms_elapsed + timepassed
            if(self.ms_elapsed >= Config.GAMETIME):
                gameEnd = 1
                
            #Flip the framebuffers
            pygame.display.flip()
            
    def __update(self):
        #Things to do here:
        #1: Update the positions of all existing aircraft
        #2: Check if any aircraft have collided with an obstacle
        #3: Check if any aircraft have reached a destination
        #4: Spawn new aircraft
        for a in self.aircraft:
			#Update positions and redraw
			a.update()
			a.draw(self.screen)
			#Check collisions
			#for o in self.obstacles:
			#	self.__handleCollision(a, o)
			#for a in self.aircraft:
			#	self.__handleCollision(a, a)

        for sp in self.aircraftspawns:
            if self.ms_elapsed >= sp.getTime():
                print("Time = " + str(self.ms_elapsed))
                print(sp.getSpawnPoint())
                ac = Aircraft(sp.getSpawnPoint(), 0.2, sp.getDestination())
                self.aircraft.append(ac)
                self.aircraftspawns.remove(sp)


    def __generateAircraftSpawnEvents(self):
        for x in range(0, Config.NUMBEROFAIRCRAFT):
            randtime = random.randint(1, Config.GAMETIME)
            randspawn = self.__generateRandomSpawnPoint();
            randdest = random.choice(self.destinations)
            spawnevent = AircraftSpawnEvent(randtime, randspawn, randdest)
            self.aircraftspawns.append(spawnevent)
            print(str(spawnevent))

    def __generateDestinations(self):
        for x in range(0, Config.NUMBEROFDESTINATIONS):
            randx = random.randint( 20, Game.AERIALPANE_W - 20 )
            randy = random.randint( 20, Game.AERIALPANE_H - 20 )
            dest = Destination((randx, randy), "D" + str(x))
            self.destinations.append(dest)

    def __generateRandomSpawnPoint(self):
        side = random.randint(1, 4)
        if side == 1:
            loc = (random.randint(0, Game.AERIALPANE_W), 0)
        elif side == 2:
            loc = (Game.AERIALPANE_W, random.randint(0, Game.AERIALPANE_H))
        elif side == 3:
            loc = (random.randint(0, Game.AERIALPANE_W), Game.AERIALPANE_H)
        elif side == 4:
            loc = (0, random.randint(0, Game.AERIALPANE_H))
        return loc

	def __handleCollision(self, ac, obs):
		pass
