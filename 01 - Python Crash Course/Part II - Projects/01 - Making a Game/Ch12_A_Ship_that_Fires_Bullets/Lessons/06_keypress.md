## Piloting the Ship

Before the ship can be useful, the player needs to be able to move it.

We'll accomplish this by monitoring the keyboard events for the left and
right arrow keys.

---

### Keyboard Events

When the player presses a key on the keyboard, the computer generates a
`pygame.KEYDOWN` event. The event contains information about the key that 
was pressed.

When we capture an event, we'll check to see if:

1. The event's `type` is `pygame.KEYDOWN`
2. The event's `key` attribute is `pygame.K_RIGHT` or `pygame.K_LEFT`

Let's update the `_check_events()` method to handle these events.

```python
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.rect.x += 1
                if event.key == pygame.K_LEFT:
                    self.ship.rect.x -= 1
```

---

### Moving the Ship

Now, when we run the program, each time we tap one of the arrow keys, the
ship moves to the left or right.

However, in the game, we would prefer that the user be able to hold the
key down and move the ship continuously until the key is released.

#### Set a "moving" Flag

To accomplish this, we'll add `moving_left` and `moving_right` flags that
we can set when the key is pressed and unset when the key is released.

```python
class Ship():
    # -- SNIP --
    def __init__(self):
        # -- SNIP --
        self.moving_left = False
        self.moving_right = False
```

#### Update the Ship's Position Based on the Flags

Then we can add a function to update the ship's position based on the
`moving_left` and `moving_right` flags.

```python
class Ship():
    # -- SNIP --
    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
```

#### Set the Flags when the Key is Pressed/Released

Now that we have the `moving_left` and `moving_right` flags, we can
update the `_check_events()` method to set them when the key is pressed and 
unset them when the key is released.

```python
class AlienInvasion():
    # -- SNIP --
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
```

#### Move the Ship When the Flags Are Set

Finally, we can add a call to the `update()` method in to move the ship
when the flags are set.

```python
class AlienInvasion():
    def run_game(self):
        # -- SNIP --
        while True:
            # -- SNIP --
            self.ship.update()
            # -- SNIP --
```

---

### Checking Our Work

Now when we run the game, we can see that the ship moves as expected. When 
we tap the left and right arrow keys, the ship moves to the left and 
right once, but when we hold the key down, the ship moves continuously.

---
