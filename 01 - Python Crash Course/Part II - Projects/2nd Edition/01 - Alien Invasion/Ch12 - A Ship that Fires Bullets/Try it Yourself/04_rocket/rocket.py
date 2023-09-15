import os
import pygame
 
class Rocket:
    """A class to manage the rocket."""

    def __init__(self, bs_game):
        """Initialize the rocket and set its starting position."""
        self.screen = bs_game.screen
        self.settings = bs_game.settings
        self.screen_rect = bs_game.screen.get_rect()

        # Load the ship image and get its rect.
        ROOT_DIR = os.path.dirname(__file__)
        file_name = "rocket.bmp"
        file_path = os.path.join(ROOT_DIR, "images", file_name)
        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_rect()

        # Start each new rocket at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Store decimal values for the rocket's position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed

        # Update rect object
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
