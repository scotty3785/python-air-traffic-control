#   File: main.py
#   Author: Tom Woolfrey

from pygame import *;
from game import *;
from menu import *;
import os;

class Main:

    BG_COLOR = (0, 0, 0)

    def __init__(self):
        init()
        screen = display.set_mode((1024, 768))
        display.set_caption('ATC Version 0.1')

        self.menu = Menu(screen)
        self.game = Game(screen)

    def run(self):
        #Display a menu
        #
        exit = 0
        while (exit == 0):
            menuEndCode = self.menu.start()
            print "Menu End Code: " + str(menuEndCode)
            if (menuEndCode == "GO"):
                menuEndCode = 0
    	        gameEndCode = self.game.start()
                if (gameEndCode == 1):
                #Time has elapsed to go to make a high score entry
                    print "Make High Score Entry"
                    exit = 1 # For now exit the game if this is selected
                elif (gameEndCode == 2):
                #User has exited game for now exit the game if this is selected
                     exit = 1                
                     print "User Aborted Game"
            elif (menuEndCode == 1):
            #Enter High Score Screen
                print "High Score Screen"
                exit = 1 # For now exit the game if this is selected
            elif (menuEndCode == 2):
                 print "Game Ended from menu"
                 exit = 1           


if __name__ == '__main__':
    game_main = Main()
    game_main.run()
