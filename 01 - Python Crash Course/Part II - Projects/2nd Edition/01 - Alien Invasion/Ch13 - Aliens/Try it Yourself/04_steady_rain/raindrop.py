import os
import pygame
from pygame.sprite import Sprite
from random import randint
from random import uniform

class Raindrop(Sprite):
    """ A class to represent a raindrop in a rain_shower"""

    def __init__(self, rs_game, new_drop = False):
        """Initialize a raindrop and set its size and starting position"""
        super().__init__()
        self.screen = rs_game.screen
        self.settings = rs_game.settings

        self.size = randint(0, 3)
        self.speed = uniform(2.100, 5.001)
        ROOT_DIR = os.path.dirname(__file__)
        file_name = None
        if self.size == 0:
            file_name = self.settings.rain_img_lg
        elif self.size == 1:
            file_name = self.settings.rain_img_med
        else:
            file_name = self.settings.rain_img_sm
        file_path = os.path.join(ROOT_DIR, "images", file_name)
        image = pygame.image.load(file_path)
        rotation = 0
        if self.settings.wind_speed != 0:
            rotation = self.settings.wind_speed // 1 * 15
        self.image = pygame.transform.rotate(image, rotation)
        self.rect = self.image.get_rect()
        
        self.x = float(randint(0, self.screen.get_rect().width - self.rect.width))
        self.y = float(randint(0, self.screen.get_rect().width - self.rect.width))

        if new_drop:
            offset = self.settings.wind_speed * 20
            left_or_top = randint(0, 2)
            if left_or_top == 0:
                if offset < 0:
                    self.x = self.screen.get_rect().width + offset
                else:
                    self.x /= offset
            else:
                self.y /= offset

        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        """Move the raindrop"""
        self.y += self.speed
        self.rect.y = self.y
        self.x += self.settings.wind_speed
        self.rect.x = self.x

    def check_edge(self):
        """Return true if raindrop passes the edge of screen"""
        screen_rect = self.screen.get_rect()
        return self.rect.top >= screen_rect.bottom or self.rect.right <= 0 or self.rect.left >= screen_rect.right
