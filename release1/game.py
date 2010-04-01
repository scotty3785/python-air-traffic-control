#   File: game.py
#   Author: Tom Woolfrey

import random;

class Game:

    AERIALPANE_W = 850;
    AERIALPANE_H = 768;

    def __init__(self, screen):
        self.screen = screen
        __generateDestinations()
        __generateAircraftSpawnEvents()

    def start(self):
        clock = pygame.time.clock()
        while True:
            timepassed = clock.tick(50)
            update()
            
    def update(self):
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
