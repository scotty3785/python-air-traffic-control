#   File: config.py
#   Author: Tom Woolfrey

class Config:

    GAMETIME = 180000;                  #Game length in milliseconds
    NUMBEROFAIRCRAFT = 20;              #Number of aircraft spawning during the game
    NUMBEROFDESTINATIONS = 6;           #Number of destinations spawning during the game
    FRAMERATE = 25                      #Framerate of the main game loop

    MAX_WAYPOINTS = 6;                  #Max user-selectable waypoints per a/c
    
    COLOR_DEST = (192, 192, 192)        #Destination colour
    COLOR_SCORETIME = (20, 193, 236)    #Score/time counter colour

    RADAR_SCAN_ANGLE = 1                #Degrees per frame radar scan angle
    RADAR_CIRC_COLOR = (0, 0x44, 0)     #Radar circle colour
    RADAR_LINE_COLOR = (0, 0xbb, 0)     #Radar line colour
    RADAR_RADIUS = 360

    SCORE_REACHDEST = 100               #Score for reaching destination
    SCORE_OBS_COLLIDE = -5              #Score for hitting obstacle
    SCORE_AC_COLLIDE = -5               #Score for hitting aircraft

    AC_SPEED_DEFAULT = 0.5              #Aircraft starting speed
    AC_COLLISION_RADIUS = 20            #Aircraft collision radius (pixels)
    AC_DRAW_COLLISION_RADIUS = False    #Draw collision radius?

    FS_FONTSIZE = 18
