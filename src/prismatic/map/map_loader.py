import json
from pathlib import Path
from src.prismatic.map.tile import Tile

class MapLoader:
    def __init__(self):
        # Load tile definitions
        tiles_path = Path(__file__).parent.parent / "data" / "tiles.json"
        with open(tiles_path, "r") as f:
            self.tiles = json.load(f)

        # Load prefab rooms
        prefab_path = Path(__file__).parent.parent / "data" / "prefab_rooms.json"
        with open(prefab_path, "r") as f:
            self.prefab_rooms = json.load(f)

    def load_room(self, room_name: str):
        """
        Load a prefab room and convert it into a grid of Tile objects.
        """
        room_layout = self.prefab_rooms[room_name]
        grid, player_spawn = [], None

        glyph_to_tile = {
            "F": "FLOOR",
            "W": "WALL",
            "S": "PLAYER_SPAWN",
            "L": "WATER",
            "V": "LAVA",
            ">": "DOWNSTAIRS",
            "<": "UPSTAIRS",
            "D": "DOOR_OPEN",
            "X": "DOOR_CLOSED",
            "H": "SWITCH_OFF",
            "O": "SWITCH_ON",
            "P": "PITFALL",
        }

        for y, row in enumerate(room_layout):
            grid_row = []
            for x, glyph in enumerate(row):
                if glyph not in glyph_to_tile:
                    raise ValueError(f"Unknown glyph '{glyph}' in room layout.")
                tile_type = glyph_to_tile[glyph]
                tile_data = self.tiles[tile_type]
                if tile_type == "PLAYER_SPAWN":
                    player_spawn = (x * 32, y * 32)
                grid_row.append(Tile(tile_type, tile_data["collision"], tuple(tile_data["color"])))
            grid.append(grid_row)

        return grid, player_spawn