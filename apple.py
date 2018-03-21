import pygame
import random


class Apple:
    def __init__(self, pys_settings, screen):
        self.pys_settings = pys_settings
        self.screen = screen
        self.rect = None

    def spawn(self, body):
        x = int(self.pys_settings.screen_width / self.pys_settings.block_length * random.random()) \
            * self.pys_settings.block_length
        y = int(self.pys_settings.screen_height / self.pys_settings.block_length * random.random()) \
            * self.pys_settings.block_length

        occupied = False
        for segment in body.body:
            if segment.centerx == x:
                if segment.centery == y:
                    occupied = True
        if occupied:
            self.spawn(body)
        else:
            self.rect = pygame.Rect((x, y, self.pys_settings.block_length, self.pys_settings.block_length))

    def update(self):
        pygame.draw.rect(self.screen, self.pys_settings.apple_color, self.rect)
