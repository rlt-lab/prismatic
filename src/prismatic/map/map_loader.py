import json
from pathlib import Path
from src.prismatic.map.tile import Tile
from src.prismatic.config import GLYPH_MAPPINGS
from src.prismatic.utils import load_json

class MapLoader:
    """Loads map data."""

    def __init__(self):
        """Initialize tiles and rooms."""
        self.tiles = load_json("tile_types.json")
        self.prefab_rooms = load_json("prefab_rooms.json")

    def load_room(self, room_name: str):
        """Load a room and return grid and spawn point."""
        if room_name not in self.prefab_rooms:
            raise ValueError(f"Room '{room_name}' not found in prefab rooms.")
        
        room_data = self.prefab_rooms[room_name]
        grid = []
        player_spawn = None
        
        for y, row in enumerate(room_data):
            grid_row = []
            for x, glyph in enumerate(row):
                tile_type = GLYPH_MAPPINGS.get(glyph)
                if tile_type is None:
                    raise ValueError(f"Unknown glyph '{glyph}' in room '{room_name}'")
                
                if tile_type == "PLAYER_SPAWN":
                    player_spawn = (x * 32, y * 32)
                
                # Get tile properties from tile_types.json
                if tile_type in self.tiles:
                    properties = self.tiles[tile_type]
                    collision = properties["collision"]
                    color = tuple(properties["color"])
                else:
                    # Default values if tile type not found
                    collision = False
                    color = (200, 200, 200)
                
                grid_row.append(Tile(tile_type, collision, color))
            grid.append(grid_row)
        
        if player_spawn is None:
            player_spawn = (32, 32)  # Default spawn point
        
        return grid, player_spawn

    def _generate_procedural_room(self):
        """Generate a procedural room (placeholder implementation)."""
        grid = [
            [Tile("FLOOR", False, (200, 200, 200)) for _ in range(30)]
            for _ in range(18)
        ]
        player_spawn = (32, 32)  # Default spawn point
        return grid, player_spawn