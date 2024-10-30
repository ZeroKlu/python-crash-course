import sys
import pygame
# After implementing 'settings.py', add this
from settings import Settings

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        # After implementing 'settings.py', add this
        self.settings = Settings()

        # Pygame "display.set_mode" creates the game window surface
        # Initially, we'll make the window static setting height and width using a tuple
        # self.screen = pygame.display.set_mode((1200, 800))
        # After implementing 'settings.py', change to use the settings file
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Set the name that appears in the title bar
        pygame.display.set_caption("Alien Invasion")

        # Set the background color (RGB - decimal)
        # self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                # The "pygame.QUIT" event is thrown when the user clicks the window close button
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            # self.screen.fill(self.bg_color)
            # After implementing 'settings.py', change to use the settings file
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
