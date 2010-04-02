#   File: aircraft.py
#   Author: Tom Woolfrey

class Aircraft(PointBasedSprite):

    def __init__(self, location):
        self.location = location;

    def setWaypoints(self, waypoints):
        self.waypoints = waypoints;

    def getWaypoints(self):
        return waypoints;

    def draw(self):
        pass
