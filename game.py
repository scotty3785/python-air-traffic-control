#   File: game.py
#   Description: An instance of one game of ATC

import pygame;
import random;
from config import *;
from destination import *;
from aircraft import *;
from obstacle import *;
from aircraftspawnevent import *;
from utility import *;

class Game:

    AERIALPANE_W = 795
    AERIALPANE_H = 768
    STRIPPANE_TOP = 152
    STRIPPANE_H = 44

    def __init__(self, screen):
        #Imagey type stuff
        self.background = pygame.image.load(os.path.join('data', 'backdrop.png'))
        self.font = pygame.font.Font(None, 30)
        self.screen = screen

        #Aircraft/destination state vars
        self.ms_elapsed = 0
        self.score = 0
        self.aircraft = []
        self.obstacles = []
        self.destinations = []
        self.aircraftspawntimes = []
        self.aircraftspawns = []

        #UI vars
        self.ac_selected = None
        self.way_clicked = None

        #Generations functions
        self.__generateDestinations()
        self.__generateObstacles()
        self.__generateAircraftSpawnEvents()

    def start(self):
        clock = pygame.time.Clock()
        gameEnd = 0
        i = 0 
        #The main game loop
        while gameEnd == 0:
            timepassed = clock.tick(Config.FRAMERATE)

            gameEnd = self.__handleUserInteraction()

            for a in self.aircraft:
                a.setSelected(False)
            
            if(self.ac_selected != None):
                self.ac_selected.setSelected(True)
            
            #Draw background
            self.screen.blit(self.background, (0, 0))

            #Draw radar circles
            pygame.draw.circle(self.screen, Config.RADAR_CIRC_COLOR, (Game.AERIALPANE_W / 2, Game.AERIALPANE_H / 2), Config.RADAR_RADIUS * 1/3, 1)
            pygame.draw.circle(self.screen, Config.RADAR_CIRC_COLOR, (Game.AERIALPANE_W / 2, Game.AERIALPANE_H / 2), Config.RADAR_RADIUS * 2/3, 1)
            pygame.draw.circle(self.screen, Config.RADAR_CIRC_COLOR, (Game.AERIALPANE_W / 2, Game.AERIALPANE_H / 2), Config.RADAR_RADIUS, 1)

            #Draw destinations
            for x in self.destinations:
                x.draw(self.screen)
                
            for x in self.obstacles:
                x.draw(self.screen)

            #Move/redraw/collide aircraft
            self.__update()

            #Draw score/time indicators
            sf_score = self.font.render("Score: " + str(self.score), True, Config.COLOR_SCORETIME)
            self.screen.blit(sf_score, (820, 10))

            sf_time = self.font.render("Time: " + str( math.floor((Config.GAMETIME - self.ms_elapsed) / 1000) ), True, Config.COLOR_SCORETIME)
            self.screen.blit(sf_time, (820, 40))
            
            
            #Recalc time and check for game end
            self.ms_elapsed = self.ms_elapsed + timepassed
            if(self.ms_elapsed >= Config.GAMETIME):
                gameEnd = 1
                
            #Flip the framebuffers
            pygame.display.flip()

        return gameEnd
            
    def __update(self):

        #1: Update the positions of all existing aircraft
        #2: Check if any aircraft have collided with an obstacle
        #3: Check if any aircraft have reached a destination
        ac_removal = []

        for n in range(0, len(self.aircraft)):
            a = self.aircraft[n]

            #Update positions and redraw
            reachdest = a.update()
            if(reachdest == True):
                #Schedule aircraft for removal
                ac_removal.append(a)
                self.score += Config.SCORE_REACHDEST
            else:
                a.draw(self.screen, n)

            #Check collisions
            for o in self.obstacles:
            	self.__handleObstacleCollision(a, o)
            for ac_t in self.aircraft:
                if(ac_t != a):
                	self.__handleAircraftCollision(ac_t, a)

        for a in ac_removal:
            if(self.ac_selected == a):
                a.setSelected(False)
                self.ac_selected = None
            self.aircraft.remove(a)

        #4: Spawn new aircraft due for spawning
        if(len(self.aircraftspawntimes) != 0):
            if self.ms_elapsed >= self.aircraftspawntimes[0]:
                sp = self.aircraftspawns[0]
                ac = Aircraft(sp.getSpawnPoint(), Config.AC_SPEED_DEFAULT, sp.getDestination(), "BA" + str(random.randint(1, 100)))
                self.aircraft.append(ac)
                ac.addWaypoint((400, 400), 0)
                self.aircraftspawns.remove(sp)
                self.aircraftspawntimes.remove(self.aircraftspawntimes[0])


    def __generateAircraftSpawnEvents(self):
        for x in range(0, Config.NUMBEROFAIRCRAFT):
            randtime = random.randint(1, Config.GAMETIME)
            randspawn = self.__generateRandomSpawnPoint();
            randdest = random.choice(self.destinations)
            spawnevent = AircraftSpawnEvent(randspawn, randdest)
            self.aircraftspawntimes.append(randtime)
            self.aircraftspawns.append(spawnevent)
        self.aircraftspawntimes.sort()

    def __generateDestinations(self):
        for x in range(0, Config.NUMBEROFDESTINATIONS):
            randx = random.randint( 20, Game.AERIALPANE_W - 20 )
            randy = random.randint( 20, Game.AERIALPANE_H - 20 )
            dest = Destination((randx, randy), "D" + str(x))
            self.destinations.append(dest)

    def __generateObstacles(self):
        pass                    #TODO

    def __generateRandomSpawnPoint(self):
        side = random.randint(1, 4)
        if side == 1:
            loc = (random.randint(0, Game.AERIALPANE_W), 0)
        elif side == 2:
            loc = (Game.AERIALPANE_W, random.randint(0, Game.AERIALPANE_H))
        elif side == 3:
            loc = (random.randint(0, Game.AERIALPANE_W), Game.AERIALPANE_H)
        elif side == 4:
            loc = (0, random.randint(0, Game.AERIALPANE_H))
        return loc

    def __handleUserInteraction(self):
        ret = 0

        for event in pygame.event.get():
            if(event.type == pygame.MOUSEBUTTONDOWN):
                clickedac = self.__getACClickedOn(event.pos)
                if(clickedac != None):
                    #Clicked an aircraft
                    self.ac_selected = clickedac
                else:
                    if(self.ac_selected != None):
                        #Not clicked aircraft, check waypoints for current selected ac
                        wclick = False
                        for x in range(0, len(self.ac_selected.getWaypoints()) - 1):
                            w = self.ac_selected.getWaypoints()[x]
                            if(w.clickedOn(event.pos) == True):
                                self.way_clicked = w
                                wclick = True
                        if wclick == False:
                            self.ac_selected = None
            elif(event.type == pygame.MOUSEBUTTONUP):
                if(self.way_clicked != None):
                    self.way_clicked = None
            elif(event.type == pygame.MOUSEMOTION):
                if(self.way_clicked != None):
                    self.way_clicked.setLocation(event.pos)
            elif(event.type == pygame.QUIT):
                ret = 2
                break
            elif(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    ret = 2
                    break
        return ret

    def __handleObstacleCollision(self, ac, obs):
        if(obs.isPointInside(ac.getLocation()) == True):
            self.score += Config.SCORE_OBS_COLLIDE

    def __handleAircraftCollision(self, ac1, ac2):
        if( Utility.locDistSq(ac1.getLocation(), ac2.getLocation()) < (Config.AC_COLLISION_RADIUS ** 2) ):
            self.score += Config.SCORE_AC_COLLIDE

    def __getACClickedOn(self, clickpos):
        foundac = None
        mindistsq = 100
        for i in range(0, len(self.aircraft)):
            ac = self.aircraft[i]
            distsq = ac.getClickDistanceSq(clickpos)
            if( ac.clickedOnFlightstrip(clickpos, i) ):
                foundac = ac
                break;
            elif( distsq < mindistsq ):
                foundac = ac
                mindistsq = distsq
        return foundac

