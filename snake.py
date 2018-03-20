import pygame
import sys
import Settings from settings
pygame.init()

size = width, height = 400, 320

screen = pygame.display.set_mode(size)
speed = [2, 2]
body = []

block_length = 20
block = pygame.Rect((0, 0, block_length, block_length))
print(type(block))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.flip()
