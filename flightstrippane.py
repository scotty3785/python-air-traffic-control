#File:  flightstrippane.py

import math;
from pgu import gui;
from config import *;

class FlightStripPane(gui.Table):

    def __init__(self, **params):
        gui.Table.__init__(self, **params)
    
    def addNewFlightStrip(self, ac):
        rows = self.getRows()
        fs = FlightStrip(ac, width=self.rect.width, height=60, align=-1, valign=-1, background=(0,0,255))
        self.tr()
        self.td(fs)
       
class FlightStrip(gui.Container):

    def __init__(self, ac, **params):
        gui.Container.__init__(self, **params)
        self.ac = ac
        self.ac.setFS(self)
        
        self.l_id = gui.Label(self.ac.getIdent(), color=(255,255,255))
        self.add(self.l_id, 2, 2)
        
        self.l_speed = gui.Label(str(self.ac.getSpeed() * Config.AC_SPEED_SCALEFACTOR), color=(255, 255, 255))
        self.add(self.l_speed, 2, 20)
        
        self.l_heading = gui.Label("Hdg: " + self.ac.getHeadingStr(), color=(255, 255, 255))
        self.add(self.l_heading, 50, 2)
        
        self.connect(gui.CLICK, self.__handle_Click)
              
    def __handle_Click(self):
        self.ac.requestSelected()
        
    def updateAllFields(self):
        self.l_id.value = self.ac.getIdent()
        self.l_speed.value = str(self.ac.getSpeed() * Config.AC_SPEED_SCALEFACTOR)
        self.l_heading.value = "Hdg: " + self.ac.getHeadingStr()
