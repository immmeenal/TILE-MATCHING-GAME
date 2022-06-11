import pygame

# Variables
WIDTH = 1200
HEIGHT = 800
FPS = 60
BOXSIZE = 200
fontname = pygame.font.match_font('calibri')

# Colours
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# Load images
aard = pygame.image.load("aard.png","aard")
axii = pygame.image.load("axii.png")
igni = pygame.image.load("igni.png")
tile = pygame.image.load("tile.png")