import unittest
from unittest.mock import patch, mock_open
from src.prismatic.map.map_loader import MapLoader
from src.prismatic.map.tile import Tile

class TestMapLoader(unittest.TestCase):
    def setUp(self):
        self.loader = MapLoader()

    @patch("builtins.open", new_callable=mock_open, read_data='{"test_room": ["FFF", "WSW", "FFF"]}')
    @patch("json.load", return_value={
        "FLOOR": {"collision": False, "color": [200, 200, 200]},
        "WALL": {"collision": True, "color": [50, 50, 50]},
        "PLAYER_SPAWN": {"collision": False, "color": [0, 255, 0]},
    })
    def test_load_valid_room(self, mock_json_load, mock_open_file):
        grid, player_spawn = self.loader.load_room("test_room")
        self.assertEqual(len(grid), 3)
        self.assertEqual(player_spawn, (32, 32))  # Player spawn at (1, 1)

    def test_load_invalid_glyph(self):
        self.loader.prefab_rooms = {"invalid_room": ["FZ"]}
        with self.assertRaises(ValueError) as context:
            self.loader.load_room("invalid_room")
        self.assertIn("Unknown glyph 'Z'", str(context.exception))
