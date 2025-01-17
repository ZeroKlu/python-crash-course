## The Settings Dilemma

At each step of the process, as we add functions to the game, we're also
adding new settings.

At some point, it will become awkward to keep adding new settings to the
game file itself. Instead, we can create a new settings class where we
can store all the settings in one place.

---

### Creating a Settings Class

So far, we've only inserted a few settings into the game file. We can
easily extract these settings into the new class.

```python
class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.frame_rate = 60
```

Note: In the final project, this will be a separate file called
`settings.py`, but in the lesson examples, I will keep all of the
classes in the same file.

---

### Modify the Game Class

After moving the settings to the new class, the `ALienInvasion` class
would look like this:

```python
class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()

        self.settings = Settings()

        # We're using our Settings class for the size of the screen
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Background color comes from the Settings class
            self.screen.fill(self.settings.bg_color)

            pygame.display.flip()

            # Clock framerate comes from the Settings class
            self.clock.tick(self.settings.frame_rate)
```