import sys
import pygame


def check_events(body):
    """Checks for events happening within pygame"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                body.stop_moving()
                body.is_moving_right = True
            elif event.key == pygame.K_LEFT:
                body.stop_moving()
                body.is_moving_left = True
            elif event.key == pygame.K_UP:
                body.stop_moving()
                body.is_moving_up = True
            elif event.key == pygame.K_DOWN:
                body.stop_moving()
                body.is_moving_down = True


def update_screen(pys_settings, screen, body):
    screen.fill(pys_settings.background_color)
    body.update()
    pygame.display.flip()
