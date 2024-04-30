import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

#COLORS
RED = (203,109,81)
WHITE = (255, 255, 255)
BLACK =  (0, 0, 0)
BLUE = (0, 0, 255)
SKY_BLUE = (54, 141, 197)
SAND_COLOR = (244, 196, 96)
YELLOW = (112,112,0)
DARK_GREY = (49, 53, 55)

starfish = pygame.transform.scale(pygame.image.load('assets/starfish.png'), (70, 75) )
