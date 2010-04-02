#   File: main.py
#   Author: Tom Woolfrey

from pygame import *;
from game import *;
import os;

class Main:

    BG_COLOR = (0, 0, 0)

    def __init__(self):
        init()
        screen = display.set_mode((1024, 768))
        display.set_caption('ATC Version 0.1')
        background = image.load(os.path.join('data', 'backdrop.png'))
        screen.blit(background, (0, 0))

        self.game = Game(screen)

    def run(self):
        #Display a menu
        #
        self.game.start()

if __name__ == '__main__':
    game_main = Main()
    game_main.run()
