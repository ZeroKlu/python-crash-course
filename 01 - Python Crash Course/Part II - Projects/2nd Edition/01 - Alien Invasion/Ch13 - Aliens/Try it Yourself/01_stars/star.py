import pygame
from pygame.sprite import Sprite
from settings import Settings

class Star(Sprite):
    """A class to represent a single star in the field."""

    def __init__(self, sf_game):
        """Initialize the star and set its starting position."""
        super().__init__()
        self.screen = sf_game.screen

        self.image = pygame.image.load(sf_game.settings.star_file_path)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
