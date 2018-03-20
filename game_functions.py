import sys
import pygame


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(pys_settings, screen, body):
    screen.fill(pys_settings.background_color)
    body.drawme()
    pygame.display.flip()
