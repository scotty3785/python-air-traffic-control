#   File: main.py
#   Author: Tom Woolfrey

from pygame import *;

class main:

    BG_COLOR = (0, 0, 0)

    def __init__(self):
        init()
        screen = display.set_mode(1024, 768)
        display.set_caption('ATC Version 0.1')
        background = image.load('data/backdrop.png')

        game = game(screen)
        game.start()
        

    def run(self):

        

if __name__ == '__main__':
    game_main = main()
    game_main.run()
