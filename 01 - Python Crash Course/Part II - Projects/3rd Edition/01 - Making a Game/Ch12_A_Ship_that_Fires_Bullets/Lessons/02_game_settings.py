"""Lesson 12.2 - Implementing Game Settings"""

import sys
import pygame

# pylint: disable=too-few-public-methods
class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)

def main() -> None:
    """Run the game."""
    ai = AlienInvasion()
    ai.run_game()

if __name__ == "__main__":
    main()
