import json
from pathlib import Path
from src.prismatic.colors import COLORS  # Import the centralized COLORS dictionary

# Load the JSON configuration file from the data directory
config_path = Path(__file__).parent / "data" / "config.json"
with open(config_path, "r") as f:
    config = json.load(f)

# Extract constants
SCREEN_WIDTH = config["SCREEN_WIDTH"]
SCREEN_HEIGHT = config["SCREEN_HEIGHT"]
SCREEN_TITLE = config["SCREEN_TITLE"]
FPS = config["FPS"]

# Use COLORS directly for color constants
BLACK = COLORS["BLACK"]
WHITE = COLORS["WHITE"]