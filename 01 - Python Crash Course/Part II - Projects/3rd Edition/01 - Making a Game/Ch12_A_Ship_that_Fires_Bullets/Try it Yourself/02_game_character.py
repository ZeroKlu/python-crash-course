"""Assignment 12.2"""

# Game Character: Find a bitmap image of a game character you like or
#                 convert an image to a bitmap. Make a class that draws
#                 the character at the center of the screen and match the
#                 background color of the image to the background color
#                 of the screen, or vice versa.

import os
import sys
import pygame

# pylint: disable=too-few-public-methods
class GameCharacter:
    """ Overall class to manage game assets and behavior. """

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Game Character")

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
                    except SystemExit:
                        os._exit(1)

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.rocket.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

class Rocket:
    """A class to manage the rocket."""

    def __init__(self, bs_game):
        """Initialize the rocket and set its starting position."""
        self.screen = bs_game.screen
        self.screen_rect = bs_game.screen.get_rect()

        # Load the ship image and get its rect.
        ROOT_DIR = os.path.dirname(__file__)
        file_name = "rocket.bmp"
        file_path = os.path.join(ROOT_DIR, "images", file_name)
        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_rect()

        # Start each new rocket at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

class Settings:
    """ Settings for Blue Sky game """
    def __init__(self):
        """ Initialize game settings """
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)

def main():
    """ Main function """
    # Make a game instance, and run the game.
    bs = GameCharacter()
    bs.run_game()

if __name__ == "__main__":
    main()

# Assignment 12.3
# Pygame Documentation: We're far enough into the game now that you might
#        want to look at some of the Pygame documentation. The Pygame home
#        page is at https:// www.pygame.org/, and the page for the
#        documentation is at https:// www.pygame.org/ docs/. Just skim
#        the documentation for now. You won't need it to complete this
#        project, but it will help if you want to modify Alien Invasion
#        or make your own game afterward.
