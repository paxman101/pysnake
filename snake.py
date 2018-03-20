import pygame
import game_functions as gf
from settings import Settings
from body import Body

# Initialize pygame
pygame.init()

pys_settings = Settings()

screen = pygame.display.set_mode(pys_settings.screen_size)

body = Body(pys_settings, screen)

while True:
    gf.check_events()
    gf.update_screen(pys_settings, screen, body)


