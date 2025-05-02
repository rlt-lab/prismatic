import pygame

from src.prismatic.colors import COLORS  # Import the COLORS dictionary
from src.prismatic.map.collision import check_collision  # Import collision logic

class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)  # Player's rectangle
        self.color = COLORS["WHITE"]  # Use color from the COLORS dictionary

    def move(self, dx, dy, grid):
        """
        Move the player by one tile in the specified direction if no collision occurs.
        :param dx: Change in x direction (-1, 0, or 1).
        :param dy: Change in y direction (-1, 0, or 1).
        :param grid: The 2D list of Tile objects representing the map.
        """
        new_x = self.rect.x + dx * 32  # Move one tile (32 pixels) in the x direction
        new_y = self.rect.y + dy * 32  # Move one tile (32 pixels) in the y direction

        # Check for collisions before moving
        if not check_collision(grid, new_x, self.rect.y):  # Check horizontal movement
            self.rect.x = new_x
        if not check_collision(grid, self.rect.x, new_y):  # Check vertical movement
            self.rect.y = new_y

    def draw(self, screen):
        """Draw the player on the screen."""
        pygame.draw.rect(screen, self.color, self.rect)