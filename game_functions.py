import sys
import pygame


def check_events(body):
    """Checks for events happening within pygame"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                body.is_moving_right = True
            elif event.key == pygame.K_LEFT:
                body.is_moving_left = True
            elif event.key == pygame.K_UP:
                body.is_moving_up = True
            elif event.key == pygame.K_DOWN:
                body.is_moving_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                body.is_moving_right = False
            elif event.key == pygame.K_LEFT:
                body.is_moving_left = False
            elif event.key == pygame.K_UP:
                body.is_moving_up = False
            elif event.key == pygame.K_DOWN:
                body.is_moving_down = False


def update_screen(pys_settings, screen, body):
    screen.fill(pys_settings.background_color)
    body.update()
    pygame.display.flip()
