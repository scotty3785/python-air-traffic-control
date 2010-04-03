#	File: aircraftspawnevent.py

class AircraftSpawnEvent:

    def __init__(self, time, spawnpoint, destination):
        self.time = time
        self.spawnpoint = spawnpoint
        self.destination = destination

    def getTime(self):
        return self.time

    def getSpawnPoint(self):
        return self.spawnpoint

    def getDestination(self):
        return self.destination

    def __str__(self):
        return "<" + str(self.time) + ", " + str(self.spawnpoint) + ", " + str(self.destination.getLocation()) + ">"
