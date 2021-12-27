import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random

random.seed()
COLOR_MAP = (20, 20, 20)
COLOR_TILE = (185, 185, 185)

class Map:
    def __init__(self, WIN):
        self.width = WIN.get_width()*.75
        self.height = WIN.get_height()*.75
        self.x = 0
        self.y = 0
        self.map = pygame.Rect(self.x, self.y, self.width, self.height)
        self.hasTiles = False
        self.tiles = []
        self.tileOffsetX = WIN.get_width()*.02
        self.tileOffsetY = WIN.get_height()*.02
        
    def update(self, WIN):
        pygame.draw.rect(WIN, COLOR_MAP, self.map)
        if(self.hasTiles == True):
            for tile in self.tiles:
                pygame.draw.rect(WIN, COLOR_TILE, tile.tile, 2)
    
    def generateMap(self, WIN):
        size = random.randrange(0, 3)
        self.hasTiles = True
        
        if(size == 0):              #small 5x5 map
            tileWidth = self.width*.18
            tileHeight = self.height*.18
            for row in range(5):
                for column in range(5):
                    tileX = (tileWidth * row) + 1 + self.tileOffsetX
                    tileY = (tileHeight * column) + 1 + self.tileOffsetY
                    self.tiles.append(Tile(tileX, tileY, tileWidth, tileHeight))
        if(size == 1):              #medium 8x8 map
            tileWidth = self.width*.12
            tileHeight = self.height*.12
            for row in range(8):
                for column in range(8):
                    tileX = (tileWidth * row) + 1 + self.tileOffsetX
                    tileY = (tileHeight * column) + 1 + self.tileOffsetY
                    self.tiles.append(Tile(tileX, tileY, tileWidth, tileHeight))
        if(size == 2):              #large 12x12 map
            tileWidth = self.width*.075
            tileHeight = self.height*.075
            for row in range(12):
                for column in range(12):
                    tileX = (tileWidth * row) + 1 + self.tileOffsetX
                    tileY = (tileHeight * column) + 1 + self.tileOffsetY
                    self.tiles.append(Tile(tileX, tileY, tileWidth, tileHeight))
            
        
class Tile():
    def __init__(self, x, y, width, height):
        self.width = width
        self.height =height
        self.x = x
        self.y = y
        self.tile = pygame.Rect(self.x, self.y, self.width, self.height)