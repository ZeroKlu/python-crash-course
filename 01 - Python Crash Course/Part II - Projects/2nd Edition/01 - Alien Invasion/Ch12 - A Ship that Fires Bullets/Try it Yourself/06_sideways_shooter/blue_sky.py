# Assignment 12.6
# Sideways Shooter: Write a game that places a ship on the left side of the screen and allows the player
#                   to move the ship up and down. Make the ship fire a missile that travels right across
#                   the screen when the player presses the spacebar. Make sure missiles are deleted once
#                   they disappear off the screen.

import os
import sys
import pygame
from settings import Settings
from rocket import Rocket
from missile import Missile

class BlueSky:
    """ Overall class to manage game assets and behavior. """

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Blue Sky")

        self.rocket = Rocket(self)
        self.missiles = pygame.sprite.Group()
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_missiles()
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
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            try:
                pygame.quit()
                sys.exit()
            except SystemExit as ex:
                os._exit(1)
        elif event.key == pygame.K_SPACE:
            self._fire_missile()

    def _fire_missile(self):
        """Create a new missile and add it to the missiles group."""
        if len(self.missiles) < self.settings.missiles_allowed:
            new_missile = Missile(self)
            self.missiles.add(new_missile)

    def _update_missiles(self):
        """Update position of missiles and get rid of old missiles."""
        # Update missile positions.
        self.missiles.update()

        # Get rid of missiles that have disappeared.
        for missile in self.missiles.copy():
            if missile.rect.right >= self.settings.screen_width:
                 self.missiles.remove(missile)

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        for missile in self.missiles.sprites():
            missile.draw_missile()
        pygame.display.flip()
            
if __name__ == '__main__':
    # Make a game instance, and run the game.
    bs = BlueSky()
    bs.run_game()
