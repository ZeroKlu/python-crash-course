## Introducing Pygame

The Pygame library provides pre-built functionality for 
creating and running games.

Using Pygame, the book walks us through the process of creating a
playable game called "Alien Invasion" in Python.

This game is similar to the classic arcade game "Space Invaders".

---

### Installing Pygame

To install Pygame, make sure your virtual environment is 
active and then run the following command:

```
python -m pip install pygame
```

Note: If you're using `pylint` to check your code, you may see errors
indicating that:  
`pygame has no _____ member`

This occurs because Pygame is written in C and is seen as an unsafe
library by Pylint.

You can correct this issue by adding the following to your VS Code
User Settings JSON file:

```json
    "pylint.args": [
        "--extension-pkg-whitelist=pygame"
    ]
```

---

### Creating a Pygame Window

To create a Pygame window, we'll do the following:

1. Create a Python file called `alien_invasion.py`
   ```python
   """Alien Invasion (a Space Invaders clone)"""
   ```
2. Import the `pygame` and `sys` libraries
   ```python
   # -- SNIP --

   import sys
   import pygame
   ```
3. Create a class called `AlienInvasion` and initialize
   the pygame system:
   ```python
   # -- SNIP --

    class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
   ```
    * The Pygame `init()` function initializes the `pygame` 
      system. It must be called before any other Pygame function
      can be used.
    * The Pygame `display.set_caption()` function sets the 
      caption (in the title bar) of the Pygame window.
    * The Pygame `display.set_mode()` function sets the size of
      the Pygame window.
        * The function takes a tuple as an argument, where the
          first value is the width and the second value is the
          height.
        * This returns a Pygame `surface` object, which we'll store as
          `self.screen`.
            * In a Pygame game, we will have a `surface` object for
              each element that has to be displayed (in this case,
              the overall Pygame window).
4. In the class, add a `run_game` method that 
   ```python
   # -- SNIP --

   class AlienInvasion:

       # -- SNIP --

       def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible
            pygame.display.flip()
   ```
    * We'll use a `while True` loop to keep the game running until
      we explicitly quit the game or close the game window.
        * In the loop, we'll continuously watch for keyboard and mouse 
          events.
            * If we catch the `pygame.QUIT` event, we'll exit the game.
        * Unless the QUIT event occurs, we'll redraw the screen.
5. Outside the class, we'll add a guarded main function that
    * Creates an instance of the `AlienInvasion` class
    * Calls the `run_game` method
      ```python
      # -- SNIP --

      def main() -> None:
          """Run the game."""
          ai = AlienInvasion()
          ai.run_game()
      
      if __name__ == "__main__":
          main()
      ```

---

### Running the Game

When we execute the program, the game will start.

![](../images/empty_game.png)

Not much is happening here, but we can see that the game is running.

---
