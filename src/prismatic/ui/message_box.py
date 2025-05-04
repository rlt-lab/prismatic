import pygame
from pathlib import Path
import json

class MessageBox:
    """Displays messages in a UI box."""

    def __init__(self, screen, width, height, font_path, padding=20, messages_path=None):
        """Initialize message box."""
        self.screen = screen
        self.width = width
        self.height = height
        self.padding = padding
        self.font = pygame.font.Font(font_path, 12)
        self.messages = []
        self.messages_data = {}
        self.max_messages = 11

        if messages_path:
            with open(messages_path, "r") as f:
                self.messages_data = json.load(f)

        self.rect = pygame.Rect(0, screen.get_height() - height, width, height)

    def add_message(self, message):
        """Add a message to the box."""
        self.messages.append(message)
        if len(self.messages) > self.max_messages:
            self.messages.pop(0)

    def get_message(self, key, **kwargs):
        """Retrieve a predefined message."""
        return self.messages_data.get(key, "Message not found.").format(**kwargs)

    def render(self):
        """Render the message box."""
        self._draw_background()
        self._render_messages()

    def clear_messages(self):
        """Clear all messages from the box."""
        self.messages = []

    def _draw_background(self):
        pygame.draw.rect(self.screen, (50, 50, 50), self.rect)

    def _render_messages(self):
        """Render messages in the box."""
        y_offset = self.rect.top + self.padding
        for message in self.messages:
            text_surface = self.font.render(message, True, (255, 255, 255))
            self.screen.blit(text_surface, (self.padding, y_offset))
            y_offset += text_surface.get_height() + 5
