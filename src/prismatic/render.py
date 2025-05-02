import pygame

class RenderEngine:
    def __init__(self, screen: pygame.Surface):
        """
        Initialize the render engine with the game screen.
        :param screen: The pygame Surface representing the game window.
        """
        self.screen = screen  # The game window surface

    def clear_screen(self, color: pygame.Color):
        """
        Clear the screen with the given color.
        :param color: The color to fill the screen with.
        """
        self.screen.fill(color)

    def render_player(self, player):
        """
        Render the player on the screen.
        :param player: The player object with a draw() method.
        """
        player.draw(self.screen)

    def update_display(self):
        """
        Update the display to show the latest rendered frame.
        """
        pygame.display.flip()