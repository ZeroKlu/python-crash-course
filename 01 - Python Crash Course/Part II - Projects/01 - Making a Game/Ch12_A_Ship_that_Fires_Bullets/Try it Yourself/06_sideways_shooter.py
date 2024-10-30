"""Assignment 12.6"""

# Sideways Shooter: Write a game that places a ship on the left side
#                   of the screen and allows the player to move the
#                   ship up and down. Make the ship fire a missile
#                   that travels right across the screen when the
#                   player presses the spacebar. Make sure missiles
#                   are deleted once they disappear off the screen.

import os
import sys
import pygame
from pygame.sprite import Sprite

# pylint: disable=too-few-public-methods
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
                except SystemExit:
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
        elif event.key in [pygame.K_q, pygame.K_ESCAPE]:
            try:
                pygame.quit()
                sys.exit()
            except SystemExit:
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

# pylint: disable=too-many-instance-attributes
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

        # missile settings
        self.missile_speed = 1.0
        self.missile_width = 15
        self.missile_height = 3
        self.missile_color = (0, 143, 17)
        self.missiles_allowed = 5

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
        self.image = pygame.transform.rotate(
            pygame.image.load(file_path), 270)
        self.rect = self.image.get_rect()

        # Start each new rocket at the center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # Store decimal values for the rocket's position.
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket's position based on the movement flag."""
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed

        # Update rect object
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

class Missile(Sprite):
    """A class to manage missiles fired from the rocket"""

    def __init__(self, bs_game):
        """Create a missile object at the ship's current position."""
        super().__init__()
        self.screen = bs_game.screen
        self.settings = bs_game.settings
        self.color = self.settings.missile_color

        # Create a missile rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.missile_width, self.settings.missile_height)
        self.rect.midleft = bs_game.rocket.rect.midright

        # Store the missile's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self, *args, **kwargs):
        """Move the missile across the screen."""
        self.x += self.settings.missile_speed
        self.rect.x = self.x

    def draw_missile(self):
        """Draw the missile to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

if __name__ == "__main__":
    # Make a game instance, and run the game.
    bs = BlueSky()
    bs.run_game()
