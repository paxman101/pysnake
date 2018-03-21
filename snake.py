import pygame
import game_functions as gf
from settings import Settings
from body import Body

# Initialize pygame
pygame.init()

# Initialize settings, screen, and snake body
pys_settings = Settings()
screen = pygame.display.set_mode(pys_settings.screen_size)
body = Body(pys_settings, screen)
for i in range(0, 10):
    body.add_block()
# Main Game Loop
while True:
    gf.check_events(body)
    gf.update_screen(pys_settings, screen, body)

