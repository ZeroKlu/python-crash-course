## Adding the Ship to the Game

The next logical step is to add a ship that the player can control.

---

### Provided Images

The book provides pre-built images for you to use in your game. The two
provided images are:

<details>
<summary>Book Images</summary>

* ship.bmp  
  ![Ship](../alien_invasion/images/image-files/book/ship.bmp)
* alien.bmp  
  ![Alien](../alien_invasion/images/image-files/book/alien.bmp)

</details>
<br>

I have also included a set of images that I created in case you want to
enhance the game beyond two images. 

<details>
<summary>Scott's Images</summary>

#### Animated GIFs

![Blue Alien](../alien_invasion/images/blue-anim.gif)
![Green Alien](../alien_invasion/images/green-anim.gif)
![Pink Alien](../alien_invasion/images/pink-anim.gif)
![Yellow Alien](../alien_invasion/images/yellow-anim.gif)
![Ship](../alien_invasion/images/ship-anim.gif)

There are also associated animated explosion images for each alien.

![Blue Boom](../alien_invasion/images/image-files/original/animated-gif/gif-frames/blue-boom/frame_4_delay-0.08s.gif)
![Blue Boom](../alien_invasion/images/image-files/original/animated-gif/gif-frames/green-boom/frame_4_delay-0.08s.gif)
![Blue Boom](../alien_invasion/images/image-files/original/animated-gif/gif-frames/pink-boom/frame_4_delay-0.08s.gif)
![Blue Boom](../alien_invasion/images/image-files/original/animated-gif/gif-frames/yellow-boom/frame_4_delay-0.08s.gif)
![Blue Boom](../alien_invasion/images/image-files/original/animated-gif/gif-frames/kaboom/frame_4_delay-0.08s.gif)

#### Static PNGs

![Blue Alien](../alien_invasion/images/image-files/original/static-png/blue.png)
![Green Alien](../alien_invasion/images/image-files/original/static-png/green.png)
![Pink Alien](../alien_invasion/images/image-files/original/static-png/pink.png)
![Yellow Alien](../alien_invasion/images/image-files/original/static-png/yellow.png)
![Ship Alien](../alien_invasion/images/image-files/original/static-png/ship.png)

#### Sprite Sheets

<img alt="Blue Alien" src="../alien_invasion/images/image-files/original/sprite-sheets/blue-sprites.png" style="width:72px;">
<img alt="Blue Explosion" src="../alien_invasion/images/image-files/original/sprite-sheets/blue-boom.png" style="width:72px;">
<img alt="Green Alien" src="../alien_invasion/images/image-files/original/sprite-sheets/green-sprites.png" style="width:72px;">
<img alt="Green Explosion" src="../alien_invasion/images/image-files/original/sprite-sheets/green-boom.png" style="width:72px;">
<img alt="Pink Alien" src="../alien_invasion/images/image-files/original/sprite-sheets/pink-sprites.png" style="width:72px;">
<img alt="Pink Explosion" src="../alien_invasion/images/image-files/original/sprite-sheets/pink-boom.png" style="width:72px;">  
<img alt="Yellow Alien" src="../alien_invasion/images/image-files/original/sprite-sheets/yellow-sprites.png" style="width:72px;">
<img alt="Yellow Explosion" src="../alien_invasion/images/image-files/original/sprite-sheets/yellow-boom.png" style="width:72px;">
<img alt="Ship" src="../alien_invasion/images/image-files/original/sprite-sheets/ship-sprites.png" style="width:72px;">
<img alt="Fiery Explosion" src="../alien_invasion/images/image-files/original/sprite-sheets/kaboom.png" style="width:72px;">

</details>

### Other Images

If you choose to hunt the internet for graphics, please be sure not to use
licensed images that you don't own the rights to.

The book recommends [opengameart.org](https://opengameart.org/) for acquiring
open-license images that anyone is allowed to use.

Note: It's important to make sure your image either has a transparent
background or has a background color that matches the background color of
the pygame screen (currently we're using (230, 230, 230), which matches the
background color of the images provided in the book).

---

### Creating the Ship

Pygame exposes a method `blit()` that allows you to draw an image onto
your game screen. We'll implement this in a new class called `Ship`.

```python
class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
```

We've done a few things here:

* Obtained the pygame screen and its rectangular space
* Loaded the ship image from a file and obtained its rectangular space
* Set the ship's starting position to the bottom center of the screen
* Exposed a function to allow us to draw the ship in the game

Note: The rectangle attributes ease both positioning and (later) collision
detection.

---

### Adding the Ship in Pygame

Now we'll add the ship to the game.

```python
class AlienInvasion:
    # -- SNIP --

    def __init__(self):
        # -- SNIP --
        self.ship = Ship(self)

    def run_game(self):
        # -- SNIP --
        while True:
            # -- SNIP --
            self.ship.blitme()
                # -- SNIP --
```

---

### Checking Our Work

Now, we can see the ship in the game.

![](../images/add_ship.png)