import pygame
import json
from pathlib import Path

# Load colors from JSON
colors_path = Path(__file__).parent / "data" / "colors.json"
with open(colors_path, "r") as f:
    raw_colors = json.load(f)

# Convert raw RGB values into pygame.Color objects
try:
    COLORS = {name: pygame.Color(*rgb) for name, rgb in raw_colors.items()}
except ValueError as e:
    raise ValueError(f"Invalid color definition in colors.json: {e}")

def get_color(name, default=(255, 255, 255)):
    """Get a color by name, or return a default color if not found."""
    return COLORS.get(name, pygame.Color(*default))