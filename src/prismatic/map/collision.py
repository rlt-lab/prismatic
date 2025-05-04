def check_collision(grid, x, y):
    """Check if position collides with a tile."""
    tile_x, tile_y = x // 32, y // 32
    if not (0 <= tile_y < len(grid) and 0 <= tile_x < len(grid[0])):
        return True  # Out-of-bounds is a collision
    return grid[tile_y][tile_x].collision

def check_area_collision(grid, rect):
    """Check if any tile in a rectangular area has collision."""
    for y in range(rect.top // 32, rect.bottom // 32):
        for x in range(rect.left // 32, rect.right // 32):
            if check_collision(grid, x * 32, y * 32):
                return True
    return False

def is_tile_walkable(grid, x, y):
    """Check if a specific tile is walkable."""
    tile_x, tile_y = x // 32, y // 32
    if not (0 <= tile_y < len(grid) and 0 <= tile_x < len(grid[0])):
        return False  # Out-of-bounds is not walkable
    return not grid[tile_y][tile_x].collision