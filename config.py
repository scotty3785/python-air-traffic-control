#   File: config.py

import pygame;

class Config:

    GAMETIME = 180000;                  #Game length in milliseconds
    NUMBEROFAIRCRAFT = 80;              #Number of aircraft spawning during the game
    NUMBEROFDESTINATIONS = 6;           #Number of destinations spawning during the game
    FRAMERATE = 40                      #Framerate of the main game loop

    MAX_WAYPOINTS = 6;                  #Max user-selectable waypoints per a/c
    
    SCORE_REACHDEST = 100               #Score for reaching destination
    SCORE_OBS_COLLIDE = -20             #Score for hitting obstacle
    SCORE_AC_COLLIDE = -1000            #Score for hitting aircraft

    AC_SPEED_DEFAULT = 0.5              #Aircraft starting speed
    AC_COLLISION_RADIUS = 20            #Aircraft collision radius (pixels)
    AC_DRAW_COLLISION_RADIUS = False    #Draw collision radius?
    AC_SPEED_SCALEFACTOR = 1000

    GAME_CODE_USER_END = 1
    GAME_CODE_TIME_UP = 2
    GAME_CODE_AC_COLLIDE = 5
    MENU_CODE_START = 3
    MENU_CODE_HIGH_SCORE = 4

    CODE_KILL = -10

    GAME_FULLSCREEN = True
