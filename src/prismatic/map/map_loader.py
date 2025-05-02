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
        Detect the player's spawn position if present.
        :param room_name: The name of the room to load.
        :return: A tuple (grid, player_spawn) where grid is a 2D list of Tile objects
                 and player_spawn is a tuple (x, y) for the player's spawn position.
        """
        room_layout = self.prefab_rooms[room_name]
        grid = []
        player_spawn = None

        for y, row in enumerate(room_layout):
            grid_row = []
            for x, glyph in enumerate(row):  # Iterate over each character in the string
                if glyph == "F":
                    tile_data = self.tiles["FLOOR"]
                elif glyph == "W":
                    tile_data = self.tiles["WALL"]
                elif glyph == "S":
                    tile_data = self.tiles["PLAYER_SPAWN"]
                    player_spawn = (x * 32, y * 32)  # Store the player's spawn position in pixels
                else:
                    raise ValueError(f"Unknown glyph '{glyph}' in room layout.")
                grid_row.append(Tile(glyph, tile_data["collision"], tuple(tile_data["color"])))
            grid.append(grid_row)

        return grid, player_spawn