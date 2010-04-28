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
        menuEndCode = self.menu.start()
        if (menuEndCode == 1):
    	    gameEndCode = self.game.start()
            print "Game End Code: " + str(gameEndCode)

if __name__ == '__main__':
    game_main = Main()
    game_main.run()
