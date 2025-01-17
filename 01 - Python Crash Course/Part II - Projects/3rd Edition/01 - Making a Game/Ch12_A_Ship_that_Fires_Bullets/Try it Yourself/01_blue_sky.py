"""Assignment 12.1"""

# Blue Sky: Make a Pygame window with a blue background.

import os
import sys
import pygame

# pylint: disable=too-few-public-methods
class BlueSky:
    """ Overall class to manage game assets and behavior. """

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Blue Sky")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    try:
                        pygame.quit()
                        sys.exit()
                    except SystemExit:
                        os._exit(1)

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()

class Settings:
    """ Settings for Blue Sky game """
    def __init__(self):
        """ Initialize game settings """
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)

def main() -> None:
    """Main function to run the game."""
    bs = BlueSky()
    bs.run_game()

if __name__ == "__main__":
    main()
