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

    SCREEN_W = 0                #Width of the screen
    SCREEN_H = 0                #Height of the screen

    AERIALPANE_W = 0            #Width of the aerial pane
    AERIALPANE_H = 0            #Height of the aerial pane

    FSPANE_LEFT = 0             #LHS of the flight strip pane (AERIALPANE_W + 3)
    FSPANE_TOP = 200            #Top of the flight strip pane

    FS_W = 0
    FS_H = 0

    RADAR_CIRC_COLOR = (0, 0x44, 0)
    RADAR_RADIUS = 0

    COLOR_SCORETIME = (20, 193, 236)    #Score/time counter colour
    
    def __init__(self, screen):
        #Screen vars
        Game.SCREEN_W = screen.get_size()[0]
        Game.SCREEN_H = screen.get_size()[1]
        Game.AERIALPANE_W = Game.SCREEN_H
        Game.AERIALPANE_H = Game.SCREEN_H
        Game.FSPANE_LEFT = Game.AERIALPANE_W + 3
        Game.FS_W = Game.SCREEN_W - Game.FSPANE_LEFT
        Game.FS_H = 60
        Game.RADAR_RADIUS = (Game.AERIALPANE_H - 50) / 2

        #Imagey type stuff
        self.font = pygame.font.Font(None, 30)
        self.screen = screen
        
        #Aircraft/destination state vars
        self.gameEndCode = 0
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

        #The main game loop
        while self.gameEndCode == 0:
            timepassed = clock.tick(Config.FRAMERATE)

            #Handle any UI stuff
            gameEnd = self.__handleUserInteraction()

            for a in self.aircraft:
                a.setSelected(False)
            
            if(self.ac_selected != None):
                self.ac_selected.setSelected(True)
            
            #Draw background
            #self.screen.blit(self.background, (0, 0))
            pygame.draw.rect(self.screen, (0, 0, 0), self.screen.get_rect())
            pygame.draw.line(self.screen, (255, 255, 255), (Game.AERIALPANE_W + 1, 0), (Game.AERIALPANE_W + 1, Game.SCREEN_H), 3)
            pygame.draw.line(self.screen, (255, 255, 255), (Game.FSPANE_LEFT, Game.FSPANE_TOP - 2), (Game.SCREEN_W, Game.FSPANE_TOP - 2), 3)

            #Draw radar circles
            pygame.draw.circle(self.screen, Game.RADAR_CIRC_COLOR, (Game.AERIALPANE_W / 2, Game.AERIALPANE_H / 2), Game.RADAR_RADIUS * 1/3, 1)
            pygame.draw.circle(self.screen, Game.RADAR_CIRC_COLOR, (Game.AERIALPANE_W / 2, Game.AERIALPANE_H / 2), Game.RADAR_RADIUS * 2/3, 1)
            pygame.draw.circle(self.screen, Game.RADAR_CIRC_COLOR, (Game.AERIALPANE_W / 2, Game.AERIALPANE_H / 2), Game.RADAR_RADIUS, 1)

            #Draw destinations
            for x in self.destinations:
                x.draw(self.screen)

            #Draw obstacles
            for x in self.obstacles:
                x.draw(self.screen)

            #Move/redraw/collide aircraft
            self.__update()

            #Draw black rect over RHS of screen, to occult bits of plane/obstacle that may be there
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect((Game.FSPANE_LEFT, 0), (Game.SCREEN_W - 1 - Game.FSPANE_LEFT, Game.FSPANE_TOP - 4)))
            pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect((Game.FSPANE_LEFT, Game.FSPANE_TOP), (Game.SCREEN_W - 1 - Game.FSPANE_LEFT, Game.SCREEN_H - Game.FSPANE_TOP)))

            #Draw flightstrips
            for n in range(0, len(self.aircraft)):
                self.aircraft[n].drawFlightstrip(self.screen, pygame.Rect((Game.FSPANE_LEFT, Game.FSPANE_TOP + (n * Game.FS_H)), (Game.FS_W, Game.FS_H)))

            #Draw score/time indicators
            sf_score = self.font.render("Score: " + str(self.score), True, Game.COLOR_SCORETIME)
            sf_time = self.font.render("Time: " + str( math.floor((Config.GAMETIME - self.ms_elapsed) / 1000) ), True, Game.COLOR_SCORETIME)

            self.screen.blit(sf_score, (Game.FSPANE_LEFT + 30, 10))
            self.screen.blit(sf_time, (Game.FSPANE_LEFT + 30, 40))
            
            #Draw game end button
            
            #Recalc time and check for game end
            self.ms_elapsed = self.ms_elapsed + timepassed
            if(self.ms_elapsed >= Config.GAMETIME):
                self.gameEndCode = Config.GAME_CODE_TIME_UP
                
            #Flip the framebuffers
            pygame.display.flip()

        return (self.gameEndCode, self.score)
            
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
                a.draw(self.screen)

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
                self.aircraftspawns.remove(sp)
                self.aircraftspawntimes.remove(self.aircraftspawntimes[0])


    def __handleUserInteraction(self):

        for event in pygame.event.get():

            if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):

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
                            #Not clicked waypoint, check lines
                            way_added = False
                            wayps = self.ac_selected.getWaypoints()
                            for x in range(-1, len(wayps) - 1):
                                if(x == -1):
                                    currP = self.ac_selected.getLocation()
                                else:
                                    currP = wayps[x].getLocation()
                                nextP = wayps[x+1].getLocation()
                                (intersect, dist) = Utility.getPointLineIntersect(currP, nextP, event.pos)
                                if((intersect != None) and (dist <= 10)):
                                    newway = Waypoint(event.pos)
                                    self.ac_selected.addWaypoint(newway, x+1)
                                    self.way_clicked = newway
                                    way_added = True
                                    break
                            if (way_added == False):
                                self.ac_selected = None

            elif(event.type == pygame.MOUSEBUTTONUP and event.button == 1):

                if(self.way_clicked != None):
                    self.way_clicked = None

            elif(event.type == pygame.MOUSEMOTION):

                if(self.way_clicked != None):
                    if(event.pos[0] >= Game.AERIALPANE_W - 3):
                        self.way_clicked.setLocation((Game.AERIALPANE_W - 3, event.pos[1]))
                    else:
                        self.way_clicked.setLocation(event.pos)

            elif(event.type == pygame.KEYDOWN):

                if(event.key == pygame.K_ESCAPE):
                    self.gameEndCode = Config.GAME_CODE_KILL
        
    def __callback_User_End(self):
        self.gameEndCode = Config.GAME_CODE_USER_END

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
            if( ac.clickedOnFlightstrip(clickpos) ):
                foundac = ac
                break;
            elif( distsq < mindistsq ):
                foundac = ac
                mindistsq = distsq
        return foundac

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

