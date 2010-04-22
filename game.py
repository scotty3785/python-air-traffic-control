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

        #Game state vars
        self.radar_angle = 0

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

            #Draw + update radar
            if(self.radar_angle == 0):
                self.radar_angle = 359
            else:
                self.radar_angle -= Config.RADAR_SCAN_ANGLE
            pygame.draw.circle(self.screen, Config.RADAR_CIRC_COLOR, (Game.AERIALPANE_W / 2, Game.AERIALPANE_H / 2), Config.RADAR_RADIUS * 1/3, 1)
            pygame.draw.circle(self.screen, Config.RADAR_CIRC_COLOR, (Game.AERIALPANE_W / 2, Game.AERIALPANE_H / 2), Config.RADAR_RADIUS * 2/3, 1)
            pygame.draw.circle(self.screen, Config.RADAR_CIRC_COLOR, (Game.AERIALPANE_W / 2, Game.AERIALPANE_H / 2), Config.RADAR_RADIUS, 1)
            pygame.draw.line(self.screen, Config.RADAR_LINE_COLOR, (Game.AERIALPANE_W / 2, Game.AERIALPANE_H / 2), self.__calcRadarEndPoint(self.radar_angle), 3)

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
            self.aircraft.remove(a)

        #4: Spawn new aircraft due for spawning
        if(len(self.aircraftspawntimes) != 0):
            if self.ms_elapsed >= self.aircraftspawntimes[0]:
                sp = self.aircraftspawns[0]
                ac = Aircraft(sp.getSpawnPoint(), Config.AC_SPEED_DEFAULT, sp.getDestination(), "BA" + str(random.randint(1, 100)))
                self.aircraft.append(ac)
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
                    self.ac_selected = None

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
        dx2 = (ac1.getLocation()[0] - ac2.getLocation()[0])**2
        dy2 = (ac1.getLocation()[1] - ac2.getLocation()[1])**2
        if( dx2 + dy2 < (Config.AC_COLLISION_RADIUS ** 2) ):
            self.score += Config.SCORE_AC_COLLIDE

    def __calcRadarEndPoint(self, angle):
        dx = Config.RADAR_RADIUS * math.sin(math.radians(angle))
        dy = Config.RADAR_RADIUS * math.cos(math.radians(angle))
        return ( (Game.AERIALPANE_W / 2) + dx, (Game.AERIALPANE_H / 2) - dy)

    def __getACClickedOn(self, clickpos):
        foundac = None
        #TODO
        #mindistsq = (Game.AERIALPANE_W ** 2, Game.AERIALPANE_H ** 2)
        for i in range(0, len(self.aircraft)):
            ac = self.aircraft[i]
            #distsq = Utility.locDistSq( ac.getLocation(), clickpos )
            #if( (ac.clickedOn(clickpos) == True) and ( distsq < mindistsq ) ):
            #    foundac = ac
            #    mindistsq = distsq
            if( ac.clickedOn(clickpos, i) ):
                foundac = ac
                break
        return foundac

