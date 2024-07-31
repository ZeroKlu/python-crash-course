# Assignment 12.2
# Game Character: Find a bitmap image of a game character you like or convert an image to a bitmap.
#                 Make a class that draws the character at the center of the screen and match the
#                 background color of the image to the background color of the screen, or vice versa.

import os
import sys
import pygame
from settings import Settings
from rocket import Rocket


class BlueSky:
    """ Overall class to manage game assets and behavior. """

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Blue Sky")

        self.rocket = Rocket(self)

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
            self.rocket.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    bs = BlueSky()
    bs.run_game()

# Assignment 12.3
# Pygame Documentation: We're far enough into the game now that you might want to look at some of
#                       the Pygame documentation. The Pygame home page is at https:// www.pygame.org/,
#                       and the home page for the documentation is at https:// www.pygame.org/ docs/.
#                       Just skim the documentation for now. You won't need it to complete this project,
#                       but it will help if you want to modify Alien Invasion or make your own game afterward.
