import pygame


class Body:
    def __init__(self, pys_settings, screen):
        self.pys_settings = pys_settings
        assert isinstance(screen, pygame.Surface)
        self.screen = screen

        self.body = []
        self.block = pygame.Rect((pys_settings.screen_width / 2, pys_settings.screen_height / 2,
                                  pys_settings.block_length, pys_settings.block_length))
        self.body.append(self.block)
        self.speed = pys_settings.snake_speed

        # Is moving in a direction booleans
        self.is_moving_right = False
        self.is_moving_left = False
        self.is_moving_up = False
        self.is_moving_down = False

    def drawme(self):
        """Draws snake"""
        for segment in self.body:
            pygame.draw.rect(self.screen, self.pys_settings.snake_color, segment)

    def move(self, x, y):
        """Moves the snake"""
        for segment in self.body:
            segment.centerx += x
            segment.centery += y

    def update(self):
        """Updates location and draws self"""
        if self.is_moving_right:
            self.move(1 * self.pys_settings.snake_speed[0], 0)
        if self.is_moving_left:
            self.move(-1 * self.pys_settings.snake_speed[0], 0)
        if self.is_moving_up:
            self.move(0, -1 * self.pys_settings.snake_speed[1])
        if self.is_moving_down:
            self.move(0, 1 * self.pys_settings.snake_speed[1])

        self.drawme()