# Assignment 12.1
# Blue Sky: Make a Pygame window with a blue background.

import os
import sys
import pygame
from settings import Settings

class BlueSky:
    """ Overall class to manage game assets and behavior. """

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
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
                    except SystemExit as ex:
                        os._exit(1)

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            
if __name__ == '__main__':
    # Make a game instance, and run the game.
    bs = BlueSky()
    bs.run_game()
