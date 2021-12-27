import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from Menu import Sidebar
from Menu import Quickmenu
from Map import Map
from Map import Tile

WIDTH, HEIGHT = 1200, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("DnDestiny")

FPS = 60

COLOR_BACKGROUND_MAIN = (45, 55, 55)
COLOR_SIDEBAR = (55, 55, 55)
COLOR_QUICKMENU = (5, 5, 5)
COLOR_MAP = (20, 20, 20)
COLOR_TILE = (185, 185, 185)

def drawWindow(sidebar, quickmenu, map):
    WIN.fill(COLOR_BACKGROUND_MAIN)
    sidebar.update(WIN)
    quickmenu.update(WIN)
    map.update(WIN)
    pygame.display.update()

def main():
    pygame.init()
    gameClock = pygame.time.Clock()
    gameIsRun = True
    sidebar = Sidebar(WIN)
    quickmenu = Quickmenu(WIN)
    map = Map(WIN)
    while(gameIsRun):
        gameClock.tick(FPS)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                gameIsRun = False
                pygame.display.quit()
                pygame.quit()
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_n):
                    if(map.hasTiles):
                        map.tiles.clear()
                    map.generateMap(WIN)
        drawWindow(sidebar, quickmenu, map)
        

if __name__ == "__main__":
    main()