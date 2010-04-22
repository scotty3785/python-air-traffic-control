#   File: utility.py

class Utility:

    @staticmethod
    def locDist(loc1, loc2):
        return math.sqrt( Utility.locationDistanceSq(loc1, loc2) )

    @staticmethod
    def locDistSq(loc1, loc2):
        dx = loc1[0] - loc2[0]
        dy = loc1[1] - loc2[1]
        return ( (dx ** 2) + (dy ** 2) )
