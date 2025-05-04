import pygame

class RenderEngine:
    """Handles rendering."""

    def __init__(self, screen: pygame.Surface):
        """Initialize with screen."""
        self.screen = screen  # The game window surface

    def clear_screen(self, color: pygame.Color):
        """Clear the screen."""
        self.screen.fill(color)

    def render_player(self, player):
        """Render the player."""
        player.draw(self.screen)

    def render_objects(self, objects):
        """Render multiple objects."""
        for obj in objects:
            obj.draw(self.screen)

    def update_display(self):
        """Update the display."""
        pygame.display.flip()

    def render_frame(self, color: pygame.Color):
        """Clear the screen and update the display."""
        self.screen.fill(color)
        pygame.display.flip()