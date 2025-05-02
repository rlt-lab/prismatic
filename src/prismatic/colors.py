import pygame
import json
from pathlib import Path

# Load colors from JSON
colors_path = Path(__file__).parent / "data" / "colors.json"
with open(colors_path, "r") as f:
    raw_colors = json.load(f)

# Convert raw RGB values into pygame.Color objects
COLORS = {name: pygame.Color(*rgb) for name, rgb in raw_colors.items()}