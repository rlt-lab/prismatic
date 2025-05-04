import unittest
from unittest.mock import Mock
from src.prismatic.player import Player
from src.prismatic.map.tile import Tile

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.message_box = Mock()
        self.player = Player(32, 32, self.message_box)
        self.grid = [
            [Tile("FLOOR", False, (200, 200, 200)) for _ in range(3)],
            [Tile("WALL", True, (50, 50, 50)) for _ in range(3)],
            [Tile("FLOOR", False, (200, 200, 200)) for _ in range(3)],
        ]

    def test_player_initial_position(self):
        self.assertEqual(self.player.rect.x, 32)
        self.assertEqual(self.player.rect.y, 32)

    def test_player_move_no_collision(self):
        self.player.move(1, 0, self.grid)  # Move right
        self.assertEqual(self.player.rect.x, 64)
        self.assertEqual(self.player.rect.y, 32)

    def test_player_move_with_collision(self):
        self.player.move(0, 1, self.grid)  # Move down into a wall
        self.assertEqual(self.player.rect.x, 32)
        self.assertEqual(self.player.rect.y, 32)

    def test_tile_interaction(self):
        self.player.move(0, 1, self.grid)  # Move down into a wall
        self.player.tile_interaction_handler.handle_tile_interaction = Mock()
        self.player.move(1, 0, self.grid)  # Move right
        self.player.tile_interaction_handler.handle_tile_interaction.assert_called()
