# File: menu_base.py
# Description: A generic class to produce a menu screen.

import pygame
import os
import math
import configparser
from pgu import gui
from config import *

class menu_base:
    def __init__(self,our_surface,width,height):
        self.SURFACE_W,self.SURFACE_H = our_surface.get_size()
        self.surface = our_surface
        self.app = gui.App()
        self.container = gui.Container(align=-1,valign=-1)
        self.button_list = []
        self.button_width = width
        self.button_height = height
        self.separator = 5
        self.finalized = False
        self.button_pressed = None
        
    def add_button(self,text,button_code,position=None):
        if self.finalized: 
            return False
        for button in self.button_list:
            if button['button_code'] == button_code:
                return False
            if button['position'] == position:
                return False
        if position == None:
            position = len(self.button_list)
        self.button_list.insert(position,{'text':text,'button_code':button_code,'position':position})
    
    def menu_callback(self,value):
        for button in self.button_list:
            if value == button['button_code']:
                self.button_pressed = value
    
    def finalize_buttons(self):
        button_start_height = (self.SURFACE_H/2) - ((self.button_height * len(self.button_list)) + ((len(self.button_list) - 1)*self.separator))
        for button in self.button_list:
            button_widget = gui.Button(value=button['text'],width=self.button_width,height=self.button_height)
            button_widget.connect(gui.CLICK,self.menu_callback,button['button_code'])
            self.container.add(button_widget,((self.SURFACE_W/2) - (self.button_width/2)),(button_start_height + (button['position'] * self.button_height) + ((button['position'] - 1) * self.separator)))
        self.finalized = True
        self.app.init(self.container,self.surface)
        
    def event(self,event):
        press = None
        if not self.finalized:
            self.finalize_buttons()
        self.app.event(event)
        self.app.repaint()
        self.app.update(self.surface)
        if self.button_pressed != None:
            press = self.button_pressed
            self.button_pressed = None
        return press
    
    #Placeholder
    def from_file(self,configfile):
        pass
    
