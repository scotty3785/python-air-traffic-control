#   File: main.py
#   Author: Tom Woolfrey

from pygame import *;
import game;

class Main:

    BG_COLOR = (0, 0, 0)

    def __init__(self):
        init()
        screen = display.set_mode((400, 400))
        display.set_caption('ATC Version 0.1')
        background = image.load('data/backdrop.png')
        screen.blit(background, (0, 0))

        self.game = game.Game(screen)

    def run(self):
        #Display a menu
        #
        self.game.start()
        pass

if __name__ == '__main__':
    game_main = Main()
    game_main.run()
