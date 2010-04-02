#   File: game.py
#   Description: An instance of one game of ATC

import random;

class Game:

    AERIALPANE_W = 850;
    AERIALPANE_H = 768;

    def __init__(self, screen):
        self.screen = screen
        self.ms_elapsed = 0
        self.score = 0
        __generateDestinations()
        __generateAircraftSpawnEvents()

    def start(self):
        clock = pygame.time.clock()

        #The main game loop
        while (self.ms_elapsed / 1000) < Config.GAMETIME:
            timepassed = clock.tick(Config.FPS)
            self.ms_elapsed = self.ms_elapsed + timepassed
            __update()
            __checkUserInteraction()
            
            
    def __update(self):
        #Things to do here:
        #1: Update the positions of all existing aircraft
        #2: Check if any aircraft have collided with an obstacle
        #3: Check if any aircraft have reached a destination
        #4: Spawn new aircraft
        pass

    def __updateAircraftPositions(self):
        for x in self.aircraft:
            #Do some shizzle
            pass

    def __generateAircraftSpawnEvents(self):
        for x in range(0, Config.NUMBEROFAIRCRAFT):
            randtime = random.randint(1, Config.GAMETIME)
            randspawn = __generateRandomSpawnPoint();
            randdest = random.randint(0, Config.NUMBEROFDESTINATIONS)
            spawn = spawn(randtime, randspawn, randdest)
            self.aircraftspawns.append(spawn)

    def __generateDestinations(self):
        for x in range(0, Config.NUMBEROFDESTINATIONS):
            randx = random.gammavariate( AERIALPANE_W/2, AERIALPANE_W/6 )
            randy = random.randint(-AERIALPANE_H/2, AERIALPANE_H/6)
            dest = destination(randx, randy)
            self.destinations.append(dest)

    def __generateRandomSpawnPoint(self):
        side = random.randint(1, 4)
        if side == 1:
            loc = (random.randint(0, AERIALPANE_W), 0)
        elif side == 2:
            loc = (AERIALPANE_W, random.randint(-AERIALPANE_H, 0))
        elif side == 3:
            loc = (random.randint(0, AERIALPANE_W), -AERIALPANE_H)
        elif side == 4:
            loc = (0, random.randint(-AERIALPANE_H, 0))
        return loc
