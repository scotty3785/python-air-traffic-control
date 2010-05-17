from high import *
import pygame
from pygame import *
import os
import pygame
import os
import math
import config
from config import *
import sys; sys.path.append("pgu")
from pgu import high, gui

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

#   File: high.py
#   Description: An instance of the highscores screen

def drawtext(screen,text,font):
    x = 200
    y = 200
    tmp = string.split(text,"\n")
    for line in tmp:
        img = font.render(line,1,WHITE,BLACK)
        rect = screen.blit(img,(x,y))
        screen.fill(0, (rect.right, rect.top, 0, rect.height))
        y = y + font.get_height()



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
        self.SCREEN_W = screen.get_size()[0]
        self.SCREEN_H = screen.get_size()[1]
        self.font = pygame.font.Font(None, 30)
        #self.font = pygame.font.Font(None, 30)
        self.highEnd = 0
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
            elif(event.type == pygame.QUIT):
                self.highEnd = GAME_CODE_MENU
                break
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    self.highEnd = Config.GAME_CODE_MENU
                    break
 
    def start(self,score):               
        clock = pygame.time.Clock()

        if (score > 0):
             print "Score Passed"
             app = gui.Desktop()
             app.connect(gui.QUIT,app.quit,None)
             main = gui.Container(width=500, height=400) #, background=(220, 220, 220) )
             main.add(gui.Label("New Highscore!!!", cls="h1"), 20, 20)
             td_style = {'padding_right': 10}
             t = gui.Table()
             t.tr()
             t.td( gui.Label('Type your name:') , style=td_style )
             userName = gui.Input()
             t.tr()
             t.td( userName, style=td_style )
             b = gui.Button("Done")
             b.connect(gui.CLICK,app.quit,None)
             t.td( b, style=td_style )
             main.add(t, 20, 100)
             app.run(main)
             if (userName.value != ""):
                   position = self.myScores.submit(score,userName.value,None)
        else:
             print "No Score Passed"
  
        #Draw background
        pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, self.SCREEN_W, self.SCREEN_H))  
            
        #Draw Highscore Table
        self.scoretable = ""
        for e in self.myScores:   
            self.scoretable += "%s       %s\n" % (e.name,e.score)
            drawtext(self.screen,self.scoretable,self.font)
            
            #Draw Screen
            pygame.display.flip()
        self.hiScore.save()
        while (self.highEnd):
            self.__handleUserInteraction()
            drawtext(self.screen,self.scoretable,self.font)
            #Draw Screen
            pygame.display.flip()
        return self.highEnd

if __name__ == '__main__':
    display.init()
    font.init()
    screen = display.set_mode((1024, 768))

    game_scores = HighScore(screen)
    game_scores.start(200)














