## Refactoring

We've reached another point where refactoring is useful. Because the 
game requires checking a number of events on each iteration, we can
separate the code for keydown and keyup events into separate functions.

### Keydown and Keyup Events

We'll create the following functions:

```python
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
```

---

### Modifying the `check_events` Function

Now that we have the new functions, we can modify the `check_events` to
call them instead of checking for keyboard events directly.

```python
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
```

---

### Pressing `Q` to Quit

As long as we're here, we can add a convenience feature to allow the
user to exit the game without having to mouse-click the `X` button.

```python
    def _check_keydown_events(self, event):
        # -- SNIP --
        elif event.key == pygame.K_q:
            sys.exit()
```

---

### Running in Full Screen

We can modify the game to run in full screen mode. To do this, we'll
modify the `AlienInvasion` class `__init__` method as follows:

```python
    def __init__(self):
        # -- SNIP --
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.screen_rect = self.screen.get_rect()
```

While the book simply implements this change, in my code file, I have
made this optional by adding the following to the `Settings` class:

```python
class Settings:
    # -- SNIP --
    def __init__(self):
        # -- SNIP --
        self.fullscreen = True
```

We'll then modify the code above like this:

```python
    def __init__(self):
        # -- SNIP --
        if self.settings.fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
```

---
