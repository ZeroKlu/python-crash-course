# Assignment 13.4
# Steady Rain: Modify your code in Exercise 13-3 so when a row of raindrops disappears off the bottom
#              of the screen, a new row appears at the top of the screen and begins to fall.

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
            self._update_raindrops()
            self._update_screen()       
            
    def _update_raindrops(self):
        """Update the positions of all raindrops."""
        self._check_rain_bottom()
        self.raindrops.update()

    def _check_rain_bottom(self):
        for drop in self.raindrops.sprites():
            if drop.check_edge():
                self.raindrops.remove(drop)
                self._create_raindrop(True)

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

    def _create_raindrop(self, new_drop = False):
        """Create a raindrop on the screen"""
        raindrop = Raindrop(self, new_drop)
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
