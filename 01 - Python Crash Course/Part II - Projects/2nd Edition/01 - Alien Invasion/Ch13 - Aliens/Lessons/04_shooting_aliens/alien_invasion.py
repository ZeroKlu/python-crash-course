import sys
import os
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        # After implementing 'settings.py', add this
        self.settings = Settings()

        # Pygame "display.set_mode" creates the game window surface
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # Set the name that appears in the title bar
        pygame.display.set_caption("Alien Invasion")

        # Add the ship to the game
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        # Create the alien fleet
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """Change direction and drop if fleet reaches either edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Change direction and drop fleet"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien and calculate number of aliens.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        ship_height = self.ship.rect.height
        available_space_x = self.settings.screen_width - (2 * alien_width)
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        # I've removed one column and row so they move more before dropping
        number_rows = available_space_y // (2 * alien_height) - 1
        number_aliens_x = available_space_x // (2 * alien_width) - 1
        
        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                try:
                    pygame.quit()
                    sys.exit()
                except SystemExit as ex:
                    os._exit(1)

            # Handle keypresses
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q or  event.key == pygame.K_ESCAPE:
            try:
                pygame.quit()
                sys.exit()
            except SystemExit as ex:
                os._exit(1)
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                 self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Respond to collisions between bullets and aliens"""
        # Check for bullets that hit aliens, and remove the bullet and the alien when they do
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # Recreate the fleet when all aliens are destroyed
        if not self.aliens:
            self.bullets.empty()
            # I've added this so that the aliens speed up each time a new fleet is generated
            self.settings.alien_speed += 0.1
            self._create_fleet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
