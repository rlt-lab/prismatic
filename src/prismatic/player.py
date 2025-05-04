import pygame
from src.prismatic.colors import COLORS
from src.prismatic.map.collision import check_collision
from src.prismatic.map.tile_interaction_handler import TileInteractionHandler

class Player:
    """Represents the player."""

    def __init__(self, x, y, message_box):
        """Initialize player attributes."""
        self.rect = pygame.Rect(x, y, 32, 32)
        self.color = COLORS["WHITE"]
        self.tile_interaction_handler = TileInteractionHandler(message_box)

    def move(self, dx, dy, grid):
        """Move player and handle interactions."""
        for delta_x, delta_y in [(dx, 0), (0, dy)]:
            self._attempt_move(delta_x, delta_y, grid)
        self._handle_tile_interaction(grid)

    def _attempt_move(self, dx, dy, grid):
        """Try moving the player."""
        new_x, new_y = self.rect.x + dx * 32, self.rect.y + dy * 32
        if not check_collision(grid, new_x, new_y):
            self.rect.x, self.rect.y = new_x, new_y

    def _handle_tile_interaction(self, grid):
        """Handle tile interactions."""
        tile = grid[self.rect.y // 32][self.rect.x // 32]
        self.tile_interaction_handler.handle_tile_interaction(tile)

    def reset_position(self, x, y):
        """Reset the player's position."""
        self.rect.x, self.rect.y = x, y

    def draw(self, screen):
        """Draw the player."""
        pygame.draw.rect(screen, self.color, self.rect)

    def is_within_bounds(self, width, height):
        """Check if the player is within the screen bounds."""
        return 0 <= self.rect.x < width and 0 <= self.rect.y < height