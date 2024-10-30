import pygame
from pygame.sprite import Sprite

class Missile(Sprite):
    """A class to manage missiles fired from the rocket"""

    def __init__(self, bs_game):
        """Create a missile object at the ship's current position."""
        super().__init__()
        self.screen = bs_game.screen
        self.settings = bs_game.settings
        self.color = self.settings.missile_color

        # Create a missile rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.missile_width, self.settings.missile_height)
        self.rect.midleft = bs_game.rocket.rect.midright
        
        # Store the missile's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):
        """Move the missile across the screen."""
        self.x += self.settings.missile_speed
        self.rect.x = self.x

    def draw_missile(self):
        """Draw the missile to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
