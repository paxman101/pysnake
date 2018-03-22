import pygame
import sys

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
        oldx = self.body[0].centerx
        oldy = self.body[0].centery
        collides = False
        if len(self.body) > 1:
            for i in range(1, len(self.body)):
                if self.body[0].centerx + x == self.body[i].centerx:
                    if self.body[0].centery + y == self.body[i].centery:
                        collides = True
        if not collides:
            self.body[0].centerx += x
            self.body[0].centery += y
            for x in range(1, len(self.body)):
                tmpx = self.body[x].centerx
                tmpy = self.body[x].centery
                self.body[x].centerx = oldx
                self.body[x].centery = oldy
                oldx = tmpx
                oldy = tmpy
        else:
            self.body = []
            self.body.append(self.block)


    def update(self):
        """Updates location and draws self"""
        if self.is_moving_right and self.body[0].right < self.pys_settings.screen_width:
            self.move(self.pys_settings.snake_speed[0], 0)
        if self.is_moving_left and self.body[0].left > 0:
            self.move(-1 * self.pys_settings.snake_speed[0], 0)
        if self.is_moving_up and self.body[0].top > 0:
            self.move(0, -1 * self.pys_settings.snake_speed[1])
        if self.is_moving_down and self.body[0].bottom < self.pys_settings.screen_height:
            self.move(0, self.pys_settings.snake_speed[1])

        self.drawme()

    def add_block(self):
        self.body.append(pygame.Rect((self.body[len(self.body) - 2].centerx - (self.pys_settings.block_length / 2),
                                      (self.body[len(self.body) - 2].centery + (self.pys_settings.block_length / 2)),
                         self.pys_settings.block_length, self.pys_settings.block_length)))

    def stop_moving(self):
        self.is_moving_left = False
        self.is_moving_right = False
        self.is_moving_up = False
        self.is_moving_down = False
