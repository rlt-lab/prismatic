import pygame

class MapRenderer:
    """Renders the map."""

    def __init__(self, screen: pygame.Surface):
        """Initialize with screen."""
        self.screen = screen

    def render(self, grid):
        """Render the map grid."""
        for y, row in enumerate(grid):
            for x, tile in enumerate(row):
                tile.render(self.screen, x * 32, y * 32)

    def render_partial(self, grid, view_rect):
        """Render only a portion of the map grid."""
        for y, row in enumerate(grid[view_rect.top:view_rect.bottom]):
            for x, tile in enumerate(row[view_rect.left:view_rect.right]):
                tile.render(self.screen, (view_rect.left + x) * 32, (view_rect.top + y) * 32)