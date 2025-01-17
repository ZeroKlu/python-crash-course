## Game Settings

We'll need to set up some additional settings for the pygame module.

---

### Setting the Clock

Pygame includes the ability to configure the clock to control the frame
rate. To ensure that the game runs at a consistent speed, we'll set the
clock to run at 60 frames per second.

```python
class AlienInvasion:
    
    # -- SNIP --

    def __init__(self):

        # -- SNIP --
        self.clock = pygame.time.Clock()

    def run_game(self):

        # -- SNIP --
        while True:

        # -- SNIP --
            self.clock.tick(60)
```

---

### Setting the Screen Color

The `fill()` method allows us to set the color of the screen. We'll set
it to a light gray color: (red=230, green=230, blue=230).

```python
class AlienInvasion:
    
    # -- SNIP --

    def __init__(self):

        # -- SNIP --
        self.bg_color = (230, 230, 230)

    def run_game(self):

        # -- SNIP --
        while True:

        # -- SNIP --
            self.screen.fill(self.bg_color)
```

---

### Running the Game

Now, when we run the program, we should see something similar to this:

![](../images/bg_color.png)

There's still nothing interesting happening, but we can see that the
background color is set to a light gray.

---
