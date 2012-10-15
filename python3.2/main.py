#   File: main.py

from pygame import *
from game import *
import main_menu
from highs import *
import os
import info_logger
import ages_menu

STATE_MENU = 1
STATE_GAME = 2
STATE_DEMO = 3
STATE_HIGH = 4
STATE_KILL = 5
STATE_AGES = 6

class Main:

    BG_COLOR = (0, 0, 0)

    def __init__(self):
        #Init the modules we need
        display.init()
        pygame.mixer.init()
        font.init()
        
        if(Config.GAME_FULLSCREEN == True):
            self.screen = display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = display.set_mode((1024, 768))
            
        display.set_caption('ATC Version 0.1')

        self.menu = main_menu.main_menu(self.screen)
        self.ages = ages_menu.ages_menu(self.screen)
        self.high = HighScore(self.screen)
        self.infologger = info_logger.info_logger("config.ini")
        #Current visitor number
        self.id = 0

    def run(self):
        state = STATE_MENU
        exit = 0
        score = 0

        while (exit == 0):
            if (state == STATE_MENU):
                menuEndCode = None
                menuEndCode = self.menu.main_loop()
                self.infologger.writeout()
                if (menuEndCode == Config.MENU_CODE_START):
                    state = STATE_AGES
                    self.id += 1
                    self.infologger.add_value(self.id,'id',self.id)
                elif (menuEndCode == Config.MENU_CODE_DEMO):
                    state = STATE_DEMO
                elif (menuEndCode == Config.MENU_CODE_HIGH_SCORE):
                    state = STATE_HIGH
                elif (menuEndCode == Config.CODE_KILL):
                    state = STATE_KILL
            elif (state == STATE_GAME):
                game = Game(self.screen, False)
                (gameEndCode, score) = game.start()
                self.infologger.add_value(self.id,'score',score)
                if (gameEndCode == Config.GAME_CODE_TIME_UP):
                    state = STATE_HIGH
                elif (gameEndCode == Config.CODE_KILL):
                    state = STATE_KILL
                elif (gameEndCode == Config.GAME_CODE_USER_END):
                    state = STATE_MENU
                elif (gameEndCode == Config.GAME_CODE_AC_COLLIDE):
                    state = STATE_HIGH
            elif (state == STATE_DEMO):
               game = Game(self.screen, True)
               (gameEndCode, score) = game.start()
               state = STATE_MENU
            elif (state == STATE_HIGH):
                highEndCode = self.high.start(score)
                state = STATE_MENU
                score = 0
            elif (state == STATE_KILL):
                exit = 1
            elif (state == STATE_AGES):
                print(state)
                self.infologger.add_value(self.id,'agegroup',self.ages.main_loop())
                state = STATE_GAME
            game = None

if __name__ == '__main__':
    game_main = Main()
    game_main.run()
