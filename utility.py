#   File: utility.py

class Utility:

    # Function: locDist(loc1, loc2)
    # Returns the Euclidean distance between two points in 2D space.
    # Uses Pythagoras theorem to compute. If you do not *need* the
    # result square rooted, it is preferred that you use locDistSq
    # and square the comparator, as it is faster.
    @staticmethod
    def locDist(loc1, loc2):
        return math.sqrt( Utility.locationDistanceSq(loc1, loc2) )

    @staticmethod
    def locDistSq(loc1, loc2):
        dx = loc1[0] - loc2[0]
        dy = loc1[1] - loc2[1]
        return ( (dx ** 2) + (dy ** 2) )
