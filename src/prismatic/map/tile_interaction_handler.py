class TileInteractionHandler:
    def __init__(self, message_box):
        """
        Initialize the TileInteractionHandler.
        :param message_box: The MessageBox instance to display messages.
        """
        self.message_box = message_box
        self.last_tile_type = None  # Track the last tile type the player was on

    def handle_tile_interaction(self, current_tile):
        """
        Handle interactions based on the current tile type.
        """
        tile_type = current_tile.tile_type

        # Define tile interaction messages
        tile_messages = {
            "WATER": "WATER_TILE",
            "PITFALL": "PITFALL",
            "DOOR_OPEN": "DOOR_OPEN",
            "WALL": "HIT_WALL",
            "WALL_TOP": "HIT_WALL_TOP",
            "WALL_SIDE": "HIT_WALL_SIDE",
        }

        # Handle entering a new tile type
        if tile_type != self.last_tile_type:
            if tile_type in tile_messages:
                self.message_box.add_message(self.message_box.get_message(tile_messages[tile_type]))
            elif self.last_tile_type == "WATER" and tile_type != "WATER":
                self.message_box.add_message(self.message_box.get_message("LEAVE_WATER"))

        # Update the last tile type
        self.last_tile_type = tile_type

    def reset_last_tile(self):
        """Reset the last tile type."""
        self.last_tile_type = None
