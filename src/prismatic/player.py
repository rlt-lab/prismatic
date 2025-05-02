import pygame

from src.prismatic.colors import COLORS  # Import the COLORS dictionary
from src.prismatic.map.collision import check_collision  # Import collision logic
from src.prismatic.map.tile_interaction_handler import TileInteractionHandler

class Player:
    def __init__(self, x, y, message_box):
        self.rect = pygame.Rect(x, y, 32, 32)  # Player's rectangle
        self.color = COLORS["WHITE"]  # Use color from the COLORS dictionary
        self.tile_interaction_handler = TileInteractionHandler(message_box)  # Initialize the handler

    def move(self, dx, dy, grid):
        """
        Move the player by one tile in the specified direction if no collision occurs.
        """
        self._attempt_move(dx, 0, grid)  # Horizontal movement
        self._attempt_move(0, dy, grid)  # Vertical movement
        self._handle_tile_interaction(grid)

    def _attempt_move(self, dx, dy, grid):
        """Attempt to move the player in the specified direction."""
        new_x = self.rect.x + dx * 32
        new_y = self.rect.y + dy * 32
        if not check_collision(grid, new_x, new_y if dx == 0 else self.rect.y):
            self.rect.x, self.rect.y = new_x, new_y

    def _handle_tile_interaction(self, grid):
        """Handle interactions with the current tile."""
        tile_x, tile_y = self.rect.x // 32, self.rect.y // 32
        self.tile_interaction_handler.handle_tile_interaction(grid[tile_y][tile_x])

    def draw(self, screen):
        """Draw the player on the screen."""
        pygame.draw.rect(screen, self.color, self.rect)