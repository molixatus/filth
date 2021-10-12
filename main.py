#_______________________________________________________________________________
from tiles import *
import pygame
from pygame import *
from pygame.locals import *
import time, math, random, sys, fractions, os
#_______________________________________________________________________________CHARACTER OBJECT CLASS
class charclass(object):
    def __init__(self, x, y):
        self.width = 32
        self.height = 32
        self.frames = 2
        self.velocity = 10
        self.blitmap = pygame.Rect(0, 0, 32, 32)
        self.pos = pygame.math.Vector2(x,y)
        self.sprite = pygame.image.load("roy.png").convert()
        self.sprite.set_colorkey((255,0,255))
        self.currframe = 0
        self.currframe2 = 0
#_______________________________________________________________________________RENDER
    def drawGW(self, screen):
        screen.blit(self.sprite, self.pos, self.blitmap)
#_______________________________________________________________________________INPUT
    def controlInput(self, screen):
        keys = pygame.key.get_pressed()
        vec = pygame.math.Vector2(0,0)

        if keys[pygame.K_a] and self.pos.x > 0 and not keys[pygame.K_d]:
            vec += pygame.math.Vector2(-1,0)
            if self.currframe < 1:
                self.blitmap = pygame.Rect(0, 0, 32, 32)
                self.currframe += 0.3
            else:
                self.blitmap = pygame.Rect(32, 0, 32, 32)
                self.currframe += 0.3

        if keys[pygame.K_d] and self.pos.x < (screen.get_width() - self.width) and not keys[pygame.K_a]:
            vec += pygame.math.Vector2(1,0)
            if self.currframe < 1:
                self.blitmap = pygame.Rect(64, 0, 32, 32)
            else:
                self.blitmap = pygame.Rect(0, 32, 32, 32)

        if keys[pygame.K_w] and self.pos.y > 0 and not keys[pygame.K_s]:
            vec += pygame.math.Vector2(0,-1)
            if self.currframe < 1:
                self.blitmap = pygame.Rect(32, 32, 32, 32)
            else:
                self.blitmap = pygame.Rect(64, 32, 32, 32)

        if keys[pygame.K_s] and self.pos.y < (screen.get_height() - self.height) and not keys[pygame.K_w]:
            vec += pygame.math.Vector2(0,1)
            if self.currframe < 1:
                self.blitmap = pygame.Rect(0,  64, 32, 32)
            else:
                self.blitmap = pygame.Rect(32, 64, 32, 32)

        if (vec.length() != 0):
            self.vec = vec.normalize()
            self.vec.scale_to_length(self.velocity)
            self.pos += self.vec;

            self.currframe += 0.3
            if self.currframe >= self.frames:
                self.currframe = 0

        #if int((self.pos.y) / 32)
        #self.pos.x/32

        if self.pos.x < 0: self.pos.x = 0
        if self.pos.x > screen.get_width() - self.width: self.pos.x = screen.get_width() - self.width
        if self.pos.y < 0: self.pos.y = 0
        if self.pos.y > screen.get_height() - self.height: self.pos.y = screen.get_height() - self.height

#_______________________________________________________________________________ __MAIN__
if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1344, 768))
    #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("screen title")
    #imageDirect = ".\data\\"

    character1 = charclass((screen.get_width()/2), (screen.get_height()/2))

    Tile1 = TileMap("map-1.csv")
    Tile2 = TileMap("map-1-collision-mask.csv")
    #look_1 = pygame.image.load('spr_bee1_0.png').convert()
    #look_1 = pygame.transform.scale(look_1, (2120, 1600))

    test = pygame.image.load('pixil-frame-0.png').convert()
    test.set_colorkey((255,0,255))

    running = True
    while running:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

        character1.controlInput(screen)

        #screen.fill((62,35,44))
        #screen.fill((237,246,214))
        Tile1.load_tiles(screen)
        Tile2.load_tiles_coll(screen)

        #screen.blit(look_1, (screen.get_width()/2 - look_1.get_width()/2, screen.get_height()/2 - look_1.get_height()/2))
        character1.drawGW(screen)


        screen.blit(test, [300,150])

        pygame.display.flip()
