from high import *
import pygame
from pygame import *
import os

#hiScore = Highs('score.txt',10)
#hiScore.load()
#myScores = hiScore['default']
#position = myScores.submit(190,"Spiderman",None)
#for e in myScores:   
#	print e.score,e.name
#print "You came in position: " +str(position)
#hiScore.save()

#   File: high.py
#   Description: An instance of the highscores screen

def drawtext(screen,text,font):
    x = 50
    y = 100
    tmp = string.split(text,"\n")
    tmp.reverse()
    for line in tmp:
        img = font.render(line,1,(30,30,30),(200,100,200))
        rect = screen.blit(img (x,y))
        screen.fill(0, (rect.right, rect.top, 0, rect.height))
        y = y - font.get_height()

import pygame
import os
import math
from config import *

RED = (255,0,0)
MAGENTA = (255, 56, 156)
ORANGE = (240, 240, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLU = (83,190,255)
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (127, 127, 127)
LGRAY = (200, 200, 200)
DGRAY = (55, 55, 55)

def texty(name,size):
    Texty = pygame.font.Font(name, size)
    return Texty

class HighScore:

    AERIALPANE_W = 795
    AERIALPANE_H = 768
    STRIPPANE_TOP = 152
    STRIPPANE_H = 44

    def __init__(self, screen):
		#Imagey type stuff
        self.screen = screen
        self.background = pygame.image.load(os.path.join('data', 'backdrop.png'))
        self.font = pygame.font.Font(None, 30)
        #self.font = pygame.font.Font(None, 30)
        self.menuEnd = 0
        self.selection = 0
        self.hiScore = Highs('score.txt',10)
        self.hiScore.load()
        self.myScores = self.hiScore['default']
        self.scoretable = ""
        #Initialisation Stuff Done

    def __handleUserInteraction(self):
        for event in pygame.event.get():
            if(event.type == pygame.MOUSEBUTTONDOWN):
                print "Mouse Click: " + str(event.pos)
                ret = self.__mouseMenuSelection(event.pos)
                if (self.selection == 2):
                    self.menuEnd = 2
                elif (self.selection == 1):
                    self.menuEnd = 1
                elif (self.selection == 0):
                    print "I clicked on start"
                    self.menuEnd = "GO"
                break
            elif(event.type == pygame.MOUSEMOTION):
                a = self.__mouseMenuOver(event.pos)
                if (0 <= a <= 2):
                    self.selection = a
            elif(event.type == pygame.QUIT):
                self.menuEnd = 2
                break
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    self.menuEnd = 2
                    break
                elif(event.key == pygame.K_UP):
					self.selection = (self.selection - 1) % 3
					break
                elif(event.key == pygame.K_DOWN):
                    self.selection = (self.selection + 1) % 3
                    break
                elif(event.key == pygame.K_SPACE):
                    if (self.selection == 2):
                        self.menuEnd = 2
                    elif (self.selection == 1):
                        self.menuEnd = 1
                    elif (self.selection == 0):
                        self.menuEnd = 0
                    break
 
    def start(self):               
        clock = pygame.time.Clock()
  
        while self.menuEnd == 0:
            timepassed = clock.tick(Config.FRAMERATE)
            
            #self.__handleUserInteraction()

            #Draw background
            self.screen.blit(self.background, (0, 0))        
            
            #Draw Highscore Table
            for e in self.myScores:   
            	self.scoretable += "%s       %s\n " % (e.name,e.score)

            print self.scoretable
            
			#Draw Screen
            pygame.display.flip()
        return self.menuEnd

if __name__ == '__main__':
    screen = display.set_mode((1024, 768))

    game_scores = HighScore(screen)
    game_scores.start()














