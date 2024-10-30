## Modifying the Ship's Attributes

Now that the ship is moving, we can see that its speed is quite slow. In
game play, it would be clearly insufficient to keep up with the planned
alien attack. We need to make the ship move faster.

---

### Setting the Ship's Speed

The problem is that in our update function, we're moving the ship a single
pixel at a time.

We could set this to a constant value, but this would be a bad idea. A 
better choice is to add a `ship_speed` attribute to the `Settings` class.

```python
class Settings:
    # -- SNIP --
    def __init__(self):
        # -- SNIP --
        self.ship_speed = 1.5
```

---

### Storing the Ship's Location

Now, let's update the `Ship` class to use the `ship_speed` attribute.

In the `__init__()` function, we'll add two new attributes:

1. `settings` - a reference to the `Settings` object
2. `x` - the ship's horizontal position

```python
class Ship:
    # -- SNIP --
    def __init__(self, ai_game):
        # -- SNIP --
        self.settings = ai_game.settings
        # -- SNIP --
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        # -- SNIP --
```

---

### Moving the Ship at the New Speed

Then we can modify the `update()` function in the `Ship` class to use the
`ship_speed` attribute to modify the ship's position (`x`).

We can then simply relocate the ship's `rect` to the new `x` value.

```python
    def update(self):
        # -- SNIP --

        # Update rect object from self.x.
        self.rect.x = self.x
```

Note: We've set the `ship_speed` to a floating point number. This will
allow granular control of the ship's speed later on.

---

### Limiting the Ship's Range

Currently, the ship can move off the edges of the screen. We need to 
limit the ship's movement so that it doesn't go off the screen.

We'll do that by checking for the edges of the screen in the `update()`
function before changing the ship's position.

```python
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right and \
           self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x
```

---
