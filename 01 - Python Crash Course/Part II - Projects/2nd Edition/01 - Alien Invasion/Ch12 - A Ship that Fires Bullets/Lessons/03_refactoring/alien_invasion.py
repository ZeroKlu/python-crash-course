import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        # After implementing 'settings.py', add this
        self.settings = Settings()

        # Pygame "display.set_mode" creates the game window surface
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Set the name that appears in the title bar
        pygame.display.set_caption("Alien Invasion")

        # Add the ship to the game
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # To better organize out code, we've refactored these sections to separate functions
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
