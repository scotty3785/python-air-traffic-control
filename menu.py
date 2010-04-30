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
    Texty = pygame.font.Font(name, size)
    return Texty

class Menu:

    AERIALPANE_W = 795
    AERIALPANE_H = 768
    STRIPPANE_TOP = 152
    STRIPPANE_H = 44

    def __init__(self, screen):
		#Imagey type stuff
        self.background = pygame.image.load(os.path.join('data', 'backdrop.png'))
        self.font = pygame.font.Font(None, 30)
        self.screen = screen
        self.radar_angle = 0
        self.menuEnd = 0
        self.selection = 0
        #Initialisation Stuff Done

    def __mouseMenuOver(self,pos):
            if ((520 < pos[0] < 710) and (360 < pos[1] < 385)):
                return 0
            elif ((520 < pos[0] < 710) and (385 < pos[1] < 420)):
                return 1
            elif ((520 < pos[0] < 710) and (420 < pos[1] < 450)):
                return 2
            else:
                return -1

    def __mouseMenuSelection(self,pos):
            if ((520 < pos[0] < 710) and (360 < pos[1] < 385)):
                return 0
            elif ((520 < pos[0] < 710) and (385 < pos[1] < 420)):
                return 1
            elif ((520 < pos[0] < 710) and (420 < pos[1] < 450)):
                return 2
            else:
                return -1

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
                self.menuEnd = Config.GAME_CODE_KILL
                break
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    self.menuEnd = Config.GAME_CODE_KILL
                    break
                elif(event.key == pygame.K_UP):
					self.selection = (self.selection - 1) % 3
					break
                elif(event.key == pygame.K_DOWN):
                    self.selection = (self.selection + 1) % 3
                    break
                elif(event.key == pygame.K_SPACE):
                    if (self.selection == 2):
                        self.menuEnd = Config.GAME_CODE_KILL
                    elif (self.selection == 1):
                        self.menuEnd = Config.GAME_CODE_HIGH_SCORE
                    elif (self.selection == 0):
                        self.menuEnd = Config.GAME_CODE_START
                    break
 
    def __calcRadarEndPoint(self, angle):
        dx = Config.RADAR_RADIUS * math.sin(math.radians(angle))
        dy = Config.RADAR_RADIUS * math.cos(math.radians(angle))
        return ( (Menu.AERIALPANE_W / 2) + dx, (Menu.AERIALPANE_H / 2) - dy)

    def start(self):
        Texty = texty(None,40)
        Bigtex = texty(None,60) #large text
        selection = 0
        shift0 = 40
        shift1 = 40
        shift2 = 40
        START   = Texty.render("START",0,WHITE)
        OPTIONS = Texty.render("HIGH SCORES",0,WHITE)
        EXIT    = Texty.render("EXIT",0,WHITE)
        
        timer = 0
        boxrect = pygame.Rect((18,48),(185,35))
        erectpos = (0,420)

        clock = pygame.time.Clock()
  
        while self.menuEnd == 0:
            timepassed = clock.tick(Config.FRAMERATE)
            
            self.__handleUserInteraction()

            #Draw background
            self.screen.blit(self.background, (0, 0))        
            
            #Draw + update radar
            #if(self.radar_angle == 0):
            #    self.radar_angle = 359
            #else:
            #    self.radar_angle -= Config.RADAR_SCAN_ANGLE
            #pygame.draw.circle(self.screen, Config.RADAR_CIRC_COLOR, (Menu.AERIALPANE_W / 2, Menu.AERIALPANE_H / 2), Config.RADAR_RADIUS * 1/3, 1)
            #pygame.draw.circle(self.screen, Config.RADAR_CIRC_COLOR, (Menu.AERIALPANE_W / 2, Menu.AERIALPANE_H / 2), Config.RADAR_RADIUS * 2/3, 1)
            #pygame.draw.circle(self.screen, Config.RADAR_CIRC_COLOR, (Menu.AERIALPANE_W / 2, Menu.AERIALPANE_H / 2), Config.RADAR_RADIUS, 1)
            #pygame.draw.line(self.screen, Config.RADAR_LINE_COLOR, (Menu.AERIALPANE_W / 2, Menu.AERIALPANE_H / 2), self.__calcRadarEndPoint(self.radar_angle), 3)

			#Create Menu Items depending on current selection.
            shift0 = 0
            shift1 = 0
            shift2 = 0
            if (self.selection == 0):
                START   = Texty.render("START",0,GREEN)
                OPTIONS = Texty.render("HIGH SCORES",0,WHITE)
                EXIT    = Texty.render("EXIT",0,WHITE)
                shift0=40
            if (self.selection == 1):
                START   = Texty.render("START",0,WHITE)
                OPTIONS = Texty.render("HIGH SCORES",0,GREEN)
                EXIT    = Texty.render("EXIT",0,WHITE)
                shift1=40
            if (self.selection == 2):
                START   = Texty.render("START",0,WHITE)
                OPTIONS = Texty.render("HIGH SCORES",0,WHITE)
                EXIT    = Texty.render("EXIT",0,GREEN)
                shift2=40

			#Draw Menu
            self.screen.blit(START,(shift0+520,360))
            self.screen.blit(OPTIONS,(shift1+520,390))
            self.screen.blit(EXIT,(shift2+520,420))

            #Draw Screen
            pygame.display.flip()
        return self.menuEnd













