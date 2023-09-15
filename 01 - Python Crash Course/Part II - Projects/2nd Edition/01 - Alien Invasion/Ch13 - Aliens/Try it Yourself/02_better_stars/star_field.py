# Assignment 13.1
# Better Stars: You can make a more realistic star pattern by introducing randomness when you place each star.
#               Recall that you can get a random number like this:
#               ----------
#               from random import randint
#               random_number = randint(-10, 10)
#               ----------
#               This code returns a random integer between –10 and 10. Using your code in Exercise 13-1,
#               adjust each star’s position by a random amount.

import sys
import os
import pygame
from settings import Settings
from star import Star
from random import randint

class StarField:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        self.stars = pygame.sprite.Group()
        self._create_star_field()

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

    def _create_star_field(self):
        """Create the field of stars."""
        star_num = 0
        while star_num < self.settings.num_stars:
            self._create_star()
            star_num += 1;

    def _create_star(self):
        """Create a star and place it in the row."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = randint(0, self.settings.screen_width - star_width)
        star.rect.x = star.x
        star.y = randint(0, self.settings.screen_height - star_height)
        star.rect.y = star.y

        self.stars.add(star)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    sf = StarField()
    sf.run_game()
