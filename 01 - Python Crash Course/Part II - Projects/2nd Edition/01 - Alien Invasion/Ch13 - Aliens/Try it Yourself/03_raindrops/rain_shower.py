# Assignment 13.3
# Raindrops: Find an image of a raindrop and create a grid of raindrops. Make the raindrops fall
#            toward the bottom of the screen until they disappear.

import sys
import os
import pygame
from settings import Settings
from raindrop import Raindrop
from random import randint

class RainShower():
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Rain Shower")

        self.raindrops = pygame.sprite.Group()
        self._create_rain()

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()        

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                try:
                    pygame.quit()
                    sys.exit()
                except SystemExit as ex:
                    os._exit(1)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q or  event.key == pygame.K_ESCAPE:
            try:
                pygame.quit()
                sys.exit()
            except SystemExit as ex:
                os._exit(1)

    def _check_keyup_events(self, event):
        """Respond to key releases."""

    def _create_rain(self):
        """Create the field of raindrops."""
        for drop_num in range(self.settings.num_raindrops):
            self._create_raindrop()

    def _create_raindrop(self, atTop = False):
        """Create a raindrop on the screen"""
        raindrop = Raindrop(self, atTop)
        rain_width = raindrop.rect.width
        rain_height = raindrop.rect.height
        self.raindrops.add(raindrop)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    rs = RainShower()
    rs.run_game()
