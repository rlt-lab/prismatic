import json
from pathlib import Path
from src.prismatic.colors import COLORS

config_path = Path(__file__).parent / "data" / "config.json"
with open(config_path, "r") as f:
    config = json.load(f)

SCREEN_WIDTH = config["SCREEN_WIDTH"]
SCREEN_HEIGHT = config["SCREEN_HEIGHT"]
SCREEN_TITLE = config["SCREEN_TITLE"]
FPS = config["FPS"]

BLACK = COLORS["BLACK"]
WHITE = COLORS["WHITE"]

GLYPH_MAPPINGS = {
    ".": "FLOOR",
    "#": "WALL",
    "S": "PLAYER_SPAWN",
    "~": "WATER",
    "%": "LAVA",
    "<": "DOWNSTAIRS",
    ">": "UPSTAIRS",
    "-": "DOOR_OPEN",
    "+": "DOOR_CLOSED",
    "0": "SWITCH_OFF",
    "1": "SWITCH_ON",
    "P": "PITFALL",
    "T": "WALL_TOP",
    "|": "WALL_SIDE"  # Changed from "S" to "|"
}

REVERSED_GLYPH_MAPPINGS = {v: k for k, v in GLYPH_MAPPINGS.items()}

def reload_config():
    """Reload configuration from the JSON file."""
    global config, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, FPS
    with open(config_path, "r") as f:
        config = json.load(f)
    SCREEN_WIDTH = config["SCREEN_WIDTH"]
    SCREEN_HEIGHT = config["SCREEN_HEIGHT"]
    SCREEN_TITLE = config["SCREEN_TITLE"]
    FPS = config["FPS"]

def validate_config():
    """Validate configuration values."""
    if SCREEN_WIDTH <= 0 or SCREEN_HEIGHT <= 0:
        raise ValueError("Screen dimensions must be positive.")
    if FPS <= 0:
        raise ValueError("FPS must be a positive integer.")