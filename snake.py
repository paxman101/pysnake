import pygame
import game_functions as gf
from settings import Settings
from body import Body
from apple import Apple

# Initialize pygame
pygame.init()

# Initialize settings, screen, snake body, and apple
pys_settings = Settings()
screen = pygame.display.set_mode(pys_settings.screen_size)
body = Body(pys_settings, screen)
apple = Apple(pys_settings, screen, body)
# Main Game Loop
apple.spawn()
while True:
    gf.check_events(body)
    gf.update_screen(pys_settings, screen, body, apple)

