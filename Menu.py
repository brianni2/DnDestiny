import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

COLOR_QUICKMENU = (5, 5, 5)
COLOR_SIDEBAR = (55, 55, 55)
COLOR_STATSFRAME = (65, 65, 65)

class Sidebar:
    def __init__(self, WIN):
        self.width = WIN.get_width()*.25            #percentage of screen width
        self.height = WIN.get_height()*.75          #percentage of screen height
        self.x = WIN.get_width() - self.width       #right align
        self.y = 0                                  #top align
        self.sidebar = pygame.Rect(self.x, self.y, self.width, self.height)
        self.statsFrame = pygame.Rect(0, 0, 0, 0)
        
    def update(self, WIN):
        pygame.draw.rect(WIN, COLOR_SIDEBAR, self.sidebar)
        self.statsDisplay()
        pygame.draw.rect(WIN, COLOR_STATSFRAME, self.statsFrame, 5)
        
    def statsDisplay(self):
        statsWidth = self.width *.85
        statsHeight = self.height * .40
        statsX = self.x + ((self.width - statsWidth)//2)
        statsY = ((self.height - statsHeight) - (self.height *.025))
        self.statsFrame = pygame.Rect(statsX, statsY, statsWidth, statsHeight)
        
class Quickmenu:
    def __init__(self, WIN):
        self.width = WIN.get_width()                    #screen width
        self.height = WIN.get_height()*.25              #Should be (1 - sidebarHeight)
        self.x = 0                                      #left align
        self.y = WIN.get_height() - self.height         #top align
        self.quickmenu = pygame.Rect(self.x, self.y, self.width, self.height)
        
    def update(self, WIN):
        pygame.draw.rect(WIN, COLOR_QUICKMENU, self.quickmenu)