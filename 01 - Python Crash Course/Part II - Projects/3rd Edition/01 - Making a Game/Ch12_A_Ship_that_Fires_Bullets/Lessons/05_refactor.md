## Refactoring

During development, it can be useful to refactor existing code regularly.

We're at a point now where it makes sense to refactor the `run_game()`
function.

We are adding screen elements (like the ship we just created), and in the 
next step, we'll start monitoring more events.

Because of this, it's useful to extract the code for event handling and
screen updates into separate functions.

```python
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
```

We can then modify the `run_game()` function like this:

```python
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            self._update_screen()

            self.clock.tick(self.settings.frame_rate)
```

This now not only makes the code more extensible for upcoming steps but
also makes the function easier to read (self-commenting).

---
