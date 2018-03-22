import sys
import pygame


def check_events(body):
    """Checks for events happening within pygame"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if len(body.body) > 1 and body.is_moving_left:
                    None
                else:
                    body.stop_moving()
                    body.is_moving_right = True
            elif event.key == pygame.K_LEFT:
                if len(body.body) > 1 and body.is_moving_right:
                    None
                else:
                    body.stop_moving()
                    body.is_moving_left = True
            elif event.key == pygame.K_UP:
                if len(body.body) > 1 and body.is_moving_down:
                    None
                else:
                    body.stop_moving()
                    body.is_moving_up = True
            elif event.key == pygame.K_DOWN:
                if len(body.body) > 1 and body.is_moving_up:
                    None
                else:
                    body.stop_moving()
                    body.is_moving_down = True


def update_screen(pys_settings, screen, body, apple):
    screen.fill(pys_settings.background_color)
    body.update()
    apple.update()
    score(pys_settings, screen, body)
    pygame.display.flip()

def score(pys_settings, screen, body):
    score_text = pys_settings.font.render("Length = " + str(len(body.body)), 1, (255, 255, 255))
    screen.blit(score_text, score_text.get_rect())

