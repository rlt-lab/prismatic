import pygame

class Tile:
    def __init__(self, tile_type: str, collision: bool, color: tuple):
        """
        Initialize a tile.
        :param tile_type: The type of the tile (e.g., "FLOOR", "WALL").
        :param collision: Whether the tile blocks movement.
        :param color: The color of the tile (RGB tuple).
        """
        self.tile_type = tile_type
        self.collision = collision
        self.color = color

    def render(self, screen: pygame.Surface, x: int, y: int):
        """
        Render the tile on the screen.
        :param screen: The pygame Surface to render on.
        :param x: The x-coordinate in pixels.
        :param y: The y-coordinate in pixels.
        """
        pygame.draw.rect(screen, self.color, (x, y, 32, 32))