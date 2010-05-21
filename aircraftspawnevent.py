#	File: aircraftspawnevent.py

from config import *;
import random;

class AircraftSpawnEvent:

    def __init__(self, spawnpoint, destination):
        self.spawnpoint = spawnpoint
        self.destination = destination

    def getSpawnPoint(self):
        return self.spawnpoint

    def getDestination(self):
        return self.destination

    def __str__(self):
        return "<" + str(self.spawnpoint) + ", " + str(self.destination.getLocation()) + ">"
        
    @staticmethod
    def generateGameSpawnEvents(screen_w, screen_h, destinations):
        ret = []
        ret2 = []
        for x in range(0, Config.NUMBEROFAIRCRAFT):
            randtime = random.randint(1, Config.GAMETIME)
            randspawn = AircraftSpawnEvent.__generateRandomSpawnPoint(screen_w, screen_h)
            randdest = random.choice(destinations)
            spawnevent = AircraftSpawnEvent(randspawn, randdest)
            ret.append(randtime)
            ret2.append(spawnevent)
        return (ret, ret2)
    
    @staticmethod
    def __generateRandomSpawnPoint(screen_w, screen_h):
        side = random.randint(1, 4)
        if side == 1:
            loc = (random.randint(0, screen_w), 0)
        elif side == 2:
            loc = (screen_w, random.randint(0, screen_h))
        elif side == 3:
            loc = (random.randint(0, screen_w), screen_h)
        elif side == 4:
            loc = (0, random.randint(0, screen_h))
        return loc
