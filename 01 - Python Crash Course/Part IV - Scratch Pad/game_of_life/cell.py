"""Model a cell in the game of life"""

from random import randint

class Cell:
    """Defines a cell for the game of life"""

    def __init__(self, onein = 16):
        """Initialize cell properties"""
        # Default assumes gives 1 in 16 chance a cell will be created alive
        self.alive = True if randint(0, onein) == 0 else False
        self.turns_alive = 1 if self.alive else 0
        # Initial state - neighbors is not defined
        self.neighbors = None

    def is_alive(self):
        """Check if the cell is alive"""
        return self.alive

    def get_age(self):
        """Check how many turns the cell has been alive"""
        return self.turns_alive

    def set(self, alive):
        """Set the cell alive state"""
        self.alive = alive
        if self.alive:
            self.turns_alive += 1
        else:
            self.turns_alive = 0

    def get_neighbors(self):
        """Get the current neighbor value of the cell"""
        return self.neighbors

    def set_neighbors(self, n):
        """Set the current neighbor value of the cell"""
        self.neighbors = n

    def count_neighbors(self, grid, r, c, wrap = False):
        """Check how many neighboring cells are alive in the current generation"""
        n = 0
        # In both x and y dimensions, we check one before through one after
        pos = [-1, 0, 1]
        for i in pos:
            y = r + i
            if wrap:
                y = (y + len(grid)) %  len(grid)
            if y < 0 or y >=  len(grid):
                continue
            for j in pos:
                if i == 0 and j == 0:
                    continue
                x = c + j
                if wrap:
                    x = (x + len(grid[r])) % len(grid[r])
                if x < 0 or x >= len(grid[r]):
                    continue
                if grid[y][x].is_alive():
                    n += 1
        self.set_neighbors(n)

    def update(self, n):
        """Apply the rules to update the cell for the next generation"""
        if n == 3:
            self.set(True)
        if n < 2 or n > 3:
            self.set(False)
