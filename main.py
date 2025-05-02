import pygame
import sys

from src.prismatic.config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, BLACK, FPS
from src.prismatic.player import Player
from src.prismatic.render import RenderEngine
from src.prismatic.input import handle_player_input  # Import input handling
from src.prismatic.map.map_loader import MapLoader
from src.prismatic.map.map_renderer import MapRenderer

def main():
    # Initialize pygame
    pygame.init()

    # Set up the game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(SCREEN_TITLE)

    # Load the map
    map_loader = MapLoader()
    grid, player_spawn = map_loader.load_room("test_room_1")

    # Create a map renderer
    map_renderer = MapRenderer(screen)

    # Create a player instance at the spawn position
    if player_spawn:
        player = Player(*player_spawn)  # Unpack (x, y) for the player's position
    else:
        raise ValueError("No player spawn point ('S') found in the map!")

    # Clock to control the frame rate
    clock = pygame.time.Clock()

    # Main game loop
    running = True
    while running:
        events = pygame.event.get()  # Get all events
        for event in events:
            if event.type == pygame.QUIT:  # Handle window close
                running = False

        # Handle player movement
        dx, dy = handle_player_input(events)
        if dx != 0 or dy != 0:  # Debugging: Print movement deltas
            print(f"Player movement: dx={dx}, dy={dy}")
        player.move(dx, dy, grid)  # Pass the grid for collision checks

        # Clear the screen
        screen.fill(BLACK)

        # Render the map
        map_renderer.render(grid)

        # Render the player
        player.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()