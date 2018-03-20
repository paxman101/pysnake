import pygame

class Body:
    def __init__(self, pys_settings, screen):
        self.pys_settings = pys_settings
        assert isinstance(screen, pygame.Surface)
        self.screen = screen

        self.body = []
        self.block = pygame.Rect((0, 0, pys_settings.block_length, pys_settings.block_length))
        self.body.append(self.block)
        self.speed = pys_settings.snake_speed

    def drawme(self):
        for segment in self.body:
           pygame.draw.rect(self.screen, self.pys_settings.snake_color, segment)
