# main2.py

import os;
import sys;
from pygame import *;
from game import *;

def main():
    pygame.init()
    display.init()
    font.init()
    screen = pygame.display.set_mode((1024,768))
    display.set_caption("Testing...")
    
    game = Game(screen)
    
    exit = False
    while (not exit):
        try:
            exit = bool("yes" == raw_input("Quit? "))
            if (not exit):
                game.start()
        except ValueError:
            print "Invalid input"


if __name__ == '__main__':
    main()
