#_______________________________________________________________________________
import pygame, csv, os, sys
from pygame import *
from pygame.locals import *
#_______________________________________________________________________________

class TileMap():

    def __init__(self, filename):
        self.tilesetcollision = pygame.image.load(".\data\\tileset_1bit-collisions.png").convert()
        self.tilesetcollision.set_colorkey((255,0,255))
        self.tileset = pygame.image.load(".\data\\tileset_1bit.png").convert()
        self.map = self.read_csv(filename)
        self.collisionmap = self.read_csv(filename)

    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=",")
            for row in data:
                map.append(list(row))
        return map

    def load_tiles(self, surface):
        x, y = 0, 0
        for row in self.map:
            x = 0
            for tile in row:
                tr = int(int(tile)/8)
                tc = int(int(tile) % 8)
                rect1 = pygame.Rect((tc * 32), (tr * 32), 32, 32)
                surface.blit(self.tileset, (x, y), rect1)
                x += 32
            y += 32

    def load_tiles_coll(self, surface):
        x, y = 0, 0
        for row in self.collisionmap:

            x = 0
            for tile in row:
                tr = int(int(tile)/2)
                tc = int(int(tile) % 2)
                rect1 = pygame.Rect((tc * 32), (tr * 32), 32, 32)
                surface.blit(self.tilesetcollision, (x, y), rect1)
                x += 32
            y += 32
    #def currtile(self, x, y):

#_______________________________________________________________________________
