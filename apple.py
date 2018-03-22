import pygame
import random


class Apple:
    def __init__(self, pys_settings, screen, body):
        self.pys_settings = pys_settings
        self.screen = screen
        self.rect = pygame.Rect((0, 0, 0, 0))
        self.body = body
        self.x = None
        self.y = None

    def spawn(self):
        self.x = int(self.pys_settings.screen_width / self.pys_settings.block_length * random.random()) \
            * self.pys_settings.block_length
        self.y = int(self.pys_settings.screen_height / self.pys_settings.block_length * random.random()) \
            * self.pys_settings.block_length

        self.rect = pygame.Rect((self.x, self.y, self.pys_settings.block_length, self.pys_settings.block_length))

        if self.has_collided():
            self.spawn()

    def update(self):
        if self.has_collided():
            self.body.add_block()
            self.spawn()
        pygame.draw.rect(self.screen, self.pys_settings.apple_color, self.rect)

    def has_collided(self):
        collided = False
        for segment in self.body.body:
            if segment.centerx == self.rect.centerx:
                if segment.centery == self.rect.centery:
                    collided = True

        return collided
