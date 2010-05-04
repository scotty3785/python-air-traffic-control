#   File: main.py

from pygame import *;
from game import *;
from menu import *;
from highs import *
import os;

STATE_MENU = 1
STATE_GAME = 2
STATE_HIGH = 3
STATE_KILL = 4

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
        state = STATE_MENU
        exit = 0
        while (exit == 0):
             if (state == STATE_MENU):
                 menuEndCode = None
                 menuEndCode = self.menu.start()
                 if (menuEndCode == Config.GAME_CODE_START):
                     state = STATE_GAME
                 elif (menuEndCode == Config.GAME_CODE_HIGH_SCORE):
                     score = 0
                     state = STATE_HIGH
                 elif (menuEndCode == Config.GAME_CODE_KILL):
                     state = STATE_KILL
             elif (state == STATE_GAME):
                 (gameEndCode, score) = self.game.start()
                 if (gameEndCode == Config.GAME_CODE_TIME_UP):
                     state = STATE_HIGH
                 elif (gameEndCode == Config.GAME_CODE_KILL):
                     state = STATE_KILL
                 elif (gameEndCode == Config.GAME_CODE_USER_END):
                     state = STATE_MENU 
             elif (state == STATE_HIGH):
                 highEndCode = self.high.start(score)
                 state = STATE_MENU
                 score = 0
                 print "Exiting High Score Screen" 
             elif (state == STATE_KILL):
                 exit = 1

if __name__ == '__main__':
    game_main = Main()
    game_main.run()
