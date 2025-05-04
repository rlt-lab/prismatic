import pygame
import sys
from pathlib import Path

from src.prismatic.config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, BLACK, FPS
from src.prismatic.player import Player
from src.prismatic.render import RenderEngine
from src.prismatic.input import handle_player_input  # Import input handling
from src.prismatic.map.map_loader import MapLoader
from src.prismatic.map.map_renderer import MapRenderer
from src.prismatic.ui.message_box import MessageBox  # Import the MessageBox class

def setup_game_window():
    """Set up the game window."""
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(SCREEN_TITLE)
    return screen

def setup_message_box(screen):
    """Initialize the message box."""
    font_path = Path(__file__).parent / "assets" / "fonts" / "ps2p.ttf"
    messages_path = Path(__file__).parent / "src" / "prismatic" / "data" / "messages.json"
    message_box = MessageBox(screen, 960, 224, font_path, messages_path=messages_path)
    message_box.add_message(message_box.get_message("WELCOME"))
    message_box.add_message(message_box.get_message("INSTRUCTIONS"))
    return message_box

def setup_player(grid, player_spawn, message_box):
    """Create the player at the spawn position."""
    if player_spawn:
        return Player(*player_spawn, message_box)
    raise ValueError("No player spawn point ('S') found in the map!")

def main():
    """Main game loop."""
    screen = setup_game_window()
    map_loader = MapLoader()
    grid, player_spawn = map_loader.load_room("test_room_1")
    map_renderer = MapRenderer(screen)
    message_box = setup_message_box(screen)
    player = setup_player(grid, player_spawn, message_box)
    clock = pygame.time.Clock()

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        dx, dy = handle_player_input(events)
        if dx or dy:
            message_box.add_message(f"Player moved: dx={dx}, dy={dy}")
        player.move(dx, dy, grid)

        # Clear the screen and render all game elements
        screen.fill(BLACK)
        map_renderer.render(grid)
        player.draw(screen)
        message_box.render()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()