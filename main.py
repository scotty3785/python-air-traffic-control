#   File: main.py

from pygame import *;
from game import *;
from menu import *;
from highs import *
import os;

class Main:

    BG_COLOR = (0, 0, 0)

    def __init__(self):
        #Init the modules we need
        display.init()
        font.init()
        
        if(Config.GAME_FULLSCREEN == True):
            screen = display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            screen = display.set_mode((1024, 768))
            
        display.set_caption('ATC Version 0.1')

        self.menu = Menu(screen)
        self.game = Game(screen)
        self.high = HighScore(screen)

    def run(self):
        #Display a menu
        #
        exit = 0
        while (exit == 0):
            menuEndCode = self.menu.start()
            print "Menu End Code: " + str(menuEndCode)
            if (menuEndCode == Config.GAME_CODE_START):
                menuEndCode = 0
    	        (gameEndCode, score) = self.game.start()
                if (gameEndCode == Config.GAME_CODE_TIME_UP):
                #Time has elapsed to go to make a high score entry
                    print "Make High Score Entry"
                    exit = 1 # For now exit the game if this is selected
                elif (gameEndCode == Config.GAME_CODE_KILL):
                #User has exited game for now exit the game if this is selected
                     exit = 1                
                     print "User Aborted Game"
            elif (menuEndCode == Config.GAME_CODE_HIGH_SCORE):
            #Enter High Score Screen
                print "High Score Screen"
                menuEndCode = self.high.start("")
                exit = 1 # For now exit the game if this is selected
            elif (menuEndCode == Config.GAME_CODE_KILL):
                 print "Game Ended from menu"
                 exit = 1           


if __name__ == '__main__':
    game_main = Main()
    game_main.run()
