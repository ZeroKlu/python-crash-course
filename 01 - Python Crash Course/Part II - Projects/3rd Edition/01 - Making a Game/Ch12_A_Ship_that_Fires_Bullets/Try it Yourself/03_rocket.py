"""Assignments 12.4 & 12.5"""

import os
import sys
import pygame

# Rocket: Make a game that begins with a rocket in the center of the
#         screen. Allow the player to move the rocket up, down, left,
#         or right using the four arrow keys. Make sure the rocket
#         never moves beyond any edge of the screen.

# Keys: Make a Pygame file that creates an empty screen. In the event
#       loop, print the event.key attribute whenever a pygame.KEYDOWN
#       event is detected. Run the program and press various keys to
#       see how Pygame responds.

# pylint: disable=too-many-instance-attributes
class Rocket:
    """A class to manage the rocket."""

    def __init__(self, bs_game):
        """Initialize the rocket and set its starting position."""
        self.screen = bs_game.screen
        self.settings = bs_game.settings
        self.screen_rect = bs_game.screen.get_rect()

        # Load the ship image and get its rect.
        ROOT_DIR = os.path.dirname(__file__)
        file_name = "rocket.bmp"
        file_path = os.path.join(ROOT_DIR, "images", file_name)
        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_rect()

        # Start each new rocket at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Store decimal values for the rocket's position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update_rocket(self):
        """Update the rocket's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed

        # Update rect object
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

# pylint: disable=too-few-public-methods
class Settings:
    """ Settings for Blue Sky game """
    def __init__(self):
        """ Initialize game settings """
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)

        # Rocket settings
        self.rocket_speed = 1.0

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
            self._check_events()
            self.rocket.update_rocket()
            self._update_screen()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                try:
                    pygame.quit()
                    sys.exit()
                except SystemExit:
                    os._exit(1)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        print(event.key)
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            try:
                pygame.quit()
                sys.exit()
            except SystemExit:
                os._exit(1)

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

def main():
    """Run the game."""
    bs_game = BlueSky()
    bs_game.run_game()

if __name__ == "__main__":
    main()
