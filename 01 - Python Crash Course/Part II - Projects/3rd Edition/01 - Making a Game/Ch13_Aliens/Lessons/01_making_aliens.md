## Adding Aliens

By now, our game includes a ship that moves and shoots.

But that's not really an interesting game. We need to add some aliens
for the ship to shoot.

Before we can add a whole fleet, we'll practice by putting a single alien in place.

---

### Making the Alien Class

We'll start by creating a new class: `Alien`.

```python
class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load(file_path("images/alien.bmp"))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
```

---

### Creating an Alien Instance

Now we can add an alien to the screen.

