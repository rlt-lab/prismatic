import pygame

class MapRenderer:
    def __init__(self, screen: pygame.Surface):
        """
        Initialize the map renderer.
        :param screen: The pygame Surface to render on.
        """
        self.screen = screen

    def render(self, grid):
        """
        Render the map grid.
        :param grid: A 2D list of Tile objects.
        """
        for y, row in enumerate(grid):
            for x, tile in enumerate(row):
                tile.render(self.screen, x * 32, y * 32)