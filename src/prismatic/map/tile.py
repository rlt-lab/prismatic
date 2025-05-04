import pygame
from src.prismatic.config import REVERSED_GLYPH_MAPPINGS
import logging

logging.basicConfig(level=logging.DEBUG)

class Tile:
    """Represents a map tile."""

    def __init__(self, tile_type: str, collision: bool, color: tuple):
        """Initialize tile attributes."""
        self.tile_type = tile_type
        self.collision = collision
        self.color = color

    def render(self, screen: pygame.Surface, x: int, y: int):
        """Render the tile."""
        pygame.draw.rect(screen, self.color, (x, y, 32, 32))
        glyph = REVERSED_GLYPH_MAPPINGS.get(self.tile_type, "?")
        if glyph == "?":
            logging.debug(f"Unknown tile_type '{self.tile_type}' - rendering '?'")
        text_surface = pygame.font.Font(None, 24).render(glyph, True, (0, 0, 0))
        screen.blit(text_surface, text_surface.get_rect(center=(x + 16, y + 16)))