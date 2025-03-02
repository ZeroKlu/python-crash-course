import os
import pygame
from pygame.sprite import Sprite
 
class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game) -> None:
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        ROOT_DIR = os.path.dirname(__file__)
        file_name = "alien.bmp"
        file_path = os.path.join(ROOT_DIR, "images", file_name)
        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self) -> None:
        """Move the alien"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self) -> bool:
        """Return true if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        return False
