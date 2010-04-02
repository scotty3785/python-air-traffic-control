#   File: config.py
#   Author: Tom Woolfrey

class Config:

    GAMETIME = 180;             #Game length in seconds
    NUMBEROFAIRCRAFT = 10;      #Number of aircraft spawning during the game
    NUMBEROFDESTINATIONS = 6;   #Number of destinations spawning during the game
    FRAMERATE = 40              #Framerate of the main game loop

    MAX_WAYPOINTS = 6;
    
    DEST_COLOR = (192, 192, 192)

    #Difficulty HARD
    DH_AIRCRAFT = 20;           #Num aircraft
    DH_DEST = 12;               #Num destinations

    #Difficulty MEDIUM
    DM_AIRCRAFT = 10;           #Num aircraft
    DM_DEST = 8;                #Num destinations

    #Difficulty EASY
    DE_AIRCRAFT = 5;            #Num aircraft
    DE_DEST = 2;                #Num destinations
