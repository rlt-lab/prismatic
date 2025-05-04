import unittest
from unittest.mock import Mock
from src.prismatic.map.tile_interaction_handler import TileInteractionHandler
from src.prismatic.map.tile import Tile

class TestTileInteractionHandler(unittest.TestCase):
    def setUp(self):
        self.message_box = Mock()
        self.handler = TileInteractionHandler(self.message_box)

    def test_water_tile_interaction(self):
        tile = Tile("WATER", False, (0, 0, 255))
        self.handler.handle_tile_interaction(tile)
        self.message_box.add_message.assert_called_with(self.message_box.get_message("WATER_TILE"))

    def test_leave_water_interaction(self):
        self.handler.last_tile_type = "WATER"
        tile = Tile("FLOOR", False, (200, 200, 200))
        self.handler.handle_tile_interaction(tile)
        self.message_box.add_message.assert_called_with(self.message_box.get_message("LEAVE_WATER"))

    def test_no_interaction_on_same_tile(self):
        tile = Tile("FLOOR", False, (200, 200, 200))
        self.handler.last_tile_type = "FLOOR"
        self.handler.handle_tile_interaction(tile)
        self.message_box.add_message.assert_not_called()
