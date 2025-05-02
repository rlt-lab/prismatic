import pygame
from pathlib import Path

class MessageBox:
    def __init__(self, screen, width, height, font_path, padding=20):
        """
        Initialize the message box.
        :param screen: The pygame Surface to render on.
        :param width: The width of the message box.
        :param height: The height of the message box.
        :param font_path: Path to the font file.
        :param padding: Padding inside the message box.
        """
        self.screen = screen
        self.width = width
        self.height = height
        self.padding = padding
        self.font = pygame.font.Font(font_path, 12)  # Font size 12
        self.messages = []  # List to store messages

        # Define the message box rectangle
        self.rect = pygame.Rect(0, screen.get_height() - height, width, height)

    def add_message(self, message):
        """
        Add a new message to the message box.
        :param message: The message string to add.
        """
        self.messages.append(message)
        if len(self.messages) > 11:  # Limit to 11 messages
            self.messages.pop(0)

    def render(self):
        """
        Render the message box and its messages.
        """
        # Draw the background of the message box
        pygame.draw.rect(self.screen, (50, 50, 50), self.rect)

        # Render each message with padding
        y_offset = self.rect.top + self.padding
        for message in self.messages:
            text_surface = self.font.render(message, True, (255, 255, 255))
            self.screen.blit(text_surface, (self.padding, y_offset))
            y_offset += text_surface.get_height() + 5  # Add spacing between messages
