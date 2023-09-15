import os
import pygame
from pygame.sprite import Sprite
from random import randint

class Raindrop(Sprite):
    """ A class to represent a raindrop in a rain_shower"""

    def __init__(self, rs_game, atTop = False):
        """Initialize a raindrop and set its size and starting position"""
        super().__init__()
        self.screen = rs_game.screen
        self.settings = rs_game.settings

        self.size = randint(0, 3)
        self.speed = randint(0, 6)
        ROOT_DIR = os.path.dirname(__file__)
        file_name = None
        if self.size == 0:
            file_name = self.settings.rain_img_lg
        elif self.size == 1:
            file_name = self.settings.rain_img_med
        else:
            file_name = self.settings.rain_img_sm
        file_path = os.path.join(ROOT_DIR, "images", file_name)
        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_rect()
        
        self.x = float(randint(0, self.screen.get_rect().width - self.rect.width))
        self.y = float(randint(0, self.screen.get_rect().width - self.rect.width))
        if atTop:
            self.y = 0

        self.rect.x = self.x
        self.rect.y = self.y
