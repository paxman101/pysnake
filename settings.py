class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_size = (self.screen_width, self.screen_height)
        self.background_color = (0, 0, 0)
        self.block_length = 40
        self.snake_speed = [self.block_length * 1, self.block_length * 1]
        self.snake_color = (255, 255, 255)
