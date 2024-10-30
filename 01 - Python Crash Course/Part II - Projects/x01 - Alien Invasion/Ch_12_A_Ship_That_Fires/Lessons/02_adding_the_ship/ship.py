import os
import pygame
 
class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        ROOT_DIR = os.path.dirname(__file__)
        file_name = "ship.bmp"
        file_path = os.path.join(ROOT_DIR, "images", file_name)
        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Note: The following location attributes are available in pygame rectangles:
        # - x, y
        # - top, left, bottom, right
        # - topleft, bottomleft, topright, bottomright
        # - midtop, midleft, midbottom, midright
        # - center, centerx, centery
        # And these additional attributes can be written: 
        # - size, width, height
        # - w, h

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)