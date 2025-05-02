def check_collision(grid, x, y):
    """
    Check if the given position collides with a tile that has collision enabled.
    :param grid: The 2D list of Tile objects representing the map.
    :param x: The x-coordinate in pixels.
    :param y: The y-coordinate in pixels.
    :return: True if there is a collision, False otherwise.
    """
    tile_x = x // 32  # Convert pixel position to grid position
    tile_y = y // 32

    # Ensure the position is within the bounds of the grid
    if tile_y < 0 or tile_y >= len(grid) or tile_x < 0 or tile_x >= len(grid[0]):
        return True  # Treat out-of-bounds as a collision

    tile = grid[tile_y][tile_x]
    return tile.collision