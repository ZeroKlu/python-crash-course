"""Implements Conway's Game of Life"""

import os
import json
import pygame
from cell import Cell

# pylint: disable=too-many-instance-attributes
class GameOfLife:
    """Implements Conway's Game of Life"""
    # Rules:
    # * A living cell dies if it has fewer than two living neighboring cells.
    # * A living cell with two or three living neighbors lives on.
    # * A living cell with more than three living neighboring cells dies in the next time step.
    # * A dead cell is revived if it has exactly three living neighboring cells.

    def __init__(self):
        # Load the settings from the JSON file
        self.ROOT_DIR = os.path.dirname(__file__)
        file_path = os.path.join(self.ROOT_DIR, "settings.json")
        with open(file_path, encoding="utf-8") as f:
            settings = json.load(f)
        self.debug_mode = settings["debug"]
        if self.debug_mode:
            print(settings)
        # Initialize game settings
        self.wraparound = settings["wraparound"]
        self.rows = settings["rows"]
        self.cols = settings["cols"]
        self.width = settings["width"]
        self.height = settings["height"]
        self.color_dead = tuple(settings["dead"])
        self.color_alive = tuple(settings["alive"])
        self.color_grid = tuple(settings["grid"])
        self.onein = settings["onein"]
        self.preload = settings["preload"]
        self.framerate = settings["framerate"]
        # Create the initial grid
        self.grid = self.create_grid()
        self.progress = True
        self.screen = None
        self.cell_width = None
        self.cell_height = None
        self.clock = pygame.time.Clock()

    def play(self):
        """Play the game until stopped"""
        self.progress = False
        # pylint: disable=no-member
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        name = f"random 1/{str(self.onein)}" if self.preload == "none" else self.preload
        pygame.display.set_caption(f"Conway's Game of Life ({name})")
        self.screen.fill(self.color_grid)
        self.draw_grid()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            if self.progress:
                self.update_grid()
            self.draw_grid()
            self.clock.tick(self.framerate)

    def create_grid(self):
        """Create the initial grid"""
        if self.preload.lower() != "none":
            return self.preload_grid()
        grid = []
        for _ in range(0, self.rows):
            row = []
            for _ in range(0, self.cols):
                row.append(Cell(self.onein))
            grid.append(row)
        return grid

    def preload_grid(self):
        """Load a pre-designed grid"""
        file_path = os.path.join(self.ROOT_DIR, "preloads.json")
        with open(file_path, encoding="utf-8") as f:
            preloads = json.load(f)
        if self.preload not in preloads.keys():
            self.preload = "none"
            return self.create_grid()
        preload = preloads[self.preload]
        if preload is None:
            self.preload = "none"
            return self.create_grid()
        self.rows = len(preload)
        self.cols = len(preload[0])
        grid = []
        for y in range(0, self.rows):
            row = []
            for x in range(0, self.cols):
                c = Cell()
                c.set(preload[y][x] == 1)
                row.append(c)
            grid.append(row)
        return grid

    def update_grid(self):
        """Update the grid for the next generation"""
        # Create a copy of the current grid
        next_cell = self.grid[:]
        # Update all cells in the copy
        for row in self.grid:
            for cell in row:
                cell.update(cell.get_neighbors())
        # Use the updated copy for the next generation
        self.grid = next_cell

    def draw_grid(self):
        """Populate the grid with live and dead cells"""
        self.cell_width = self.width // self.cols - 1
        self.cell_height = self.height // self.rows - 1
        # pylint: disable=consider-using-enumerate
        for r in range(0, len(self.grid)):
            y = (self.cell_height + 1) * r + 1
            for c in range(0, len(self.grid[r])):
                x = (self.cell_width + 1) * c + 1
                color = self.color_alive if self.grid[r][c].is_alive() else self.color_dead
                rect = pygame.Rect(x, y, self.cell_width, self.cell_height)
                pygame.draw.rect(self.screen, color, rect)
                self.grid[r][c].count_neighbors(self.grid, r, c, self.wraparound)
                if self.debug_mode:
                    self.screen.blit(pygame.font.SysFont('Arial', 16).render(
                        str(self.grid[r][c].get_neighbors()), True, (200, 0, 0)),
                        (x + 1, y + 2))
        self.progress = True
        pygame.display.update()
