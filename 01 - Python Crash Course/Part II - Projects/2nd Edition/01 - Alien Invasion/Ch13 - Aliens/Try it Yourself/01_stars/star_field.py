# Assignment 13.1
# Stars: Find an image of a star. Make a grid of stars appear on the screen.

import sys
import os
import pygame
from settings import Settings
from star import Star

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
        star = Star(self)
        star_width, star_height = star.rect.size
        max_width_x = self.settings.screen_width - (2 * star_width)
        max_height_y = self.settings.screen_height - (2 * star_height)
        num_cols = max_width_x // (2 * star_width)
        num_rows = max_height_y // (2 * star_height)
        for row_num in range(num_rows):
            for col_num in range(num_cols):
                self._create_star(row_num, col_num)

    def _create_star(self, row_num, col_num):
        """Create a star and place it in the row."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * col_num
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_num
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
