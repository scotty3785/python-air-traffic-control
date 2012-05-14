#   File: menu.py
#   Description: An instance of one menu

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
    matched = pygame.font.match_font('verdana, arial')
    Texty = pygame.font.Font(matched, size)
    return Texty

class Menu:

    AERIALPANE_W = 795
    AERIALPANE_H = 768
    STRIPPANE_TOP = 152
    STRIPPANE_H = 44

    def __init__(self, screen):
        self.SCREEN_W = screen.get_size()[0]
        self.SCREEN_H = screen.get_size()[1]
		#Imagey type stuff
        self.font = pygame.font.Font(None, 30)
        self.screen = screen
        self.menuEnd = 0
        self.selection = 0
        self.timeWithoutUIEvent = 0
        #Initialisation Stuff Done

    def __mouseMenuOver(self,pos):
            if ((520 < pos[0] < 710) and (360 < pos[1] < 385)):
                return 0
            elif ((520 < pos[0] < 710) and (385 < pos[1] < 420)):
                return 1
            elif ((520 < pos[0] < 710) and (420 < pos[1] < 450)):
                return 2
            elif ((520 < pos[0] < 710) and (450 < pos[1] < 480)):
                return 3
            else:
                return -1

    def __mouseMenuSelection(self,pos):
            if ((520 < pos[0] < 710) and (360 < pos[1] < 385)):
                return 0
            elif ((520 < pos[0] < 710) and (385 < pos[1] < 420)):
                return 1
            elif ((520 < pos[0] < 710) and (420 < pos[1] < 450)):
                return 2
            elif ((520 < pos[0] < 710) and (450 < pos[1] < 480)):
                return 3
            else:
                return -1

    def __handleUserInteraction(self):
        
        for event in pygame.event.get():
            if(event.type == pygame.MOUSEBUTTONDOWN):
                self.timeWithoutUIEvent = 0
                ret = self.__mouseMenuSelection(event.pos)
                if (ret == 3):
                    self.menuEnd = Config.CODE_KILL
                elif (ret == 2):
                    self.menuEnd = Config.MENU_CODE_HIGH_SCORE
                elif (ret == 1):
                    self.menuEnd = Config.MENU_CODE_DEMO
                elif (ret == 0):
                    self.menuEnd = Config.MENU_CODE_START
                break
            elif(event.type == pygame.MOUSEMOTION):
                self.timeWithoutUIEvent = 0
                a = self.__mouseMenuOver(event.pos)
                if (0 <= a <= 3):
                    self.selection = a
            elif(event.type == pygame.QUIT):
                self.menuEnd = Config.CODE_KILL
                break
            elif(event.type == pygame.KEYDOWN):
                self.timeWithoutUIEvent = 0
                if(event.key == pygame.K_ESCAPE):
                    self.menuEnd = Config.CODE_KILL
                    break
                elif(event.key == pygame.K_UP):
                    self.selection = (self.selection - 1) % 4
                    break
                elif(event.key == pygame.K_DOWN):
                    self.selection = (self.selection + 1) % 4
                    break
                elif(event.key == pygame.K_SPACE or event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER):
                    if (self.selection == 3):
                        self.menuEnd = Config.CODE_KILL
                    elif (self.selection == 2):
                        self.menuEnd = Config.MENU_CODE_HIGH_SCORE
                    elif (self.selection == 1):
                        self.menuEnd = Config.MENU_CODE_DEMO
                    elif (self.selection == 0):
                        self.menuEnd = Config.MENU_CODE_START
                    break

 
    def start(self):
        Texty = texty(None,30)
        Bigtex = texty(None,60) #large text
        selection = 0
        shift0 = 40
        shift1 = 40
        shift2 = 40
        START   = Texty.render("START", 0,WHITE)
        DEMO    = Texty.render("DEMO",0,WHITE)
        OPTIONS = Texty.render("HIGH SCORES",0,WHITE)
        EXIT    = Texty.render("EXIT",0,WHITE)
        
        timer = 0
        boxrect = pygame.Rect((18,48),(185,35))
        erectpos = (0,420)

        clock = pygame.time.Clock()
        
        self.menuEnd = 0
  
        while self.menuEnd == 0:
            timepassed = clock.tick(Config.FRAMERATE)
            self.timeWithoutUIEvent += timepassed
            if (self.timeWithoutUIEvent > Config.GAME_DEMOTIMEOUT):
                self.menuEnd = Config.MENU_CODE_DEMO
                self.timeWithoutUIEvent = 0
            
            self.__handleUserInteraction()

            pygame.draw.rect(self.screen, BLACK, pygame.Rect(0, 0, self.SCREEN_W, self.SCREEN_H))
            
            #Create Menu Items depending on current selection.
            shift0 = 0
            shift1 = 0
            shift2 = 0
            shift3 = 0
            if (self.selection == 0):
                START   = Texty.render("START",0,GREEN)
                DEMO    = Texty.render("DEMO",0,WHITE)
                OPTIONS = Texty.render("HIGH SCORES",0,WHITE)
                EXIT    = Texty.render("EXIT",0,WHITE)
                shift0=40
            elif (self.selection == 1):
                START   = Texty.render("START",0,WHITE)
                DEMO    = Texty.render("DEMO",0,GREEN)
                OPTIONS = Texty.render("HIGH SCORES",0,WHITE)
                EXIT    = Texty.render("EXIT",0,WHITE)
                shift1=40
            elif (self.selection == 2):
                START   = Texty.render("START",0,WHITE)
                DEMO    = Texty.render("DEMO",0,WHITE)
                OPTIONS = Texty.render("HIGH SCORES",0,GREEN)
                EXIT    = Texty.render("EXIT",0,WHITE)
                shift2=40
            elif (self.selection == 3):
                START   = Texty.render("START",0,WHITE)
                DEMO    = Texty.render("DEMO",0,WHITE)
                OPTIONS = Texty.render("HIGH SCORES",0,WHITE)
                EXIT    = Texty.render("EXIT",0,GREEN)
                shift3=40

			#Draw Menu
            self.screen.blit(START,(shift0+520,360))
            self.screen.blit(DEMO, (shift1+520,390))
            self.screen.blit(OPTIONS,(shift2+520,420))
            self.screen.blit(EXIT,(shift3+520,450))

            #Draw Screen
            pygame.display.flip()
        return self.menuEnd
