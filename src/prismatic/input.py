import pygame
import json
from pathlib import Path
import time

# Load controls from JSON
controls_path = Path(__file__).parent / "data" / "input.json"
with open(controls_path, "r") as f:
    controls = json.load(f)

# Map control names to pygame key constants
KEY_BINDINGS = {action: getattr(pygame, key) for action, key in controls.items()}

# Key repeat settings
KEY_REPEAT_DELAY = 1.0  # Delay before continuous movement starts (in seconds)
KEY_REPEAT_INTERVAL = 0.2  # Time between repeated movements (in seconds)

# Track key states
key_states = {
    action: {"pressed": False, "last_move_time": 0}
    for action in KEY_BINDINGS
}

def update_key_states(events):
    """
    Update the key states based on pygame events.
    :param events: The list of pygame events.
    """
    current_time = time.time()
    for event in events:
        if event.type == pygame.KEYDOWN:
            for action, key in KEY_BINDINGS.items():
                if event.key == key:
                    key_states[action]["pressed"] = True
                    key_states[action]["last_move_time"] = 0  # Trigger immediate movement
        elif event.type == pygame.KEYUP:
            for action, key in KEY_BINDINGS.items():
                if event.key == key:
                    key_states[action]["pressed"] = False

def get_movement_deltas():
    """
    Calculate movement deltas (dx, dy) based on key states.
    :return: Tuple (dx, dy) representing movement direction.
    """
    dx, dy = 0, 0
    current_time = time.time()

    for action, state in key_states.items():
        if state["pressed"]:
            time_since_last_move = current_time - state["last_move_time"]
            if state["last_move_time"] == 0 or time_since_last_move >= KEY_REPEAT_DELAY or time_since_last_move >= KEY_REPEAT_INTERVAL:
                if action == "MOVE_UP":
                    dy = -1
                elif action == "MOVE_DOWN":
                    dy = 1
                elif action == "MOVE_LEFT":
                    dx = -1
                elif action == "MOVE_RIGHT":
                    dx = 1
                state["last_move_time"] = current_time  # Update the last move time

    return dx, dy

def handle_player_input(events):
    """
    Handle player input by updating key states and calculating movement deltas.
    :param events: The list of pygame events.
    :return: Tuple (dx, dy) representing movement direction.
    """
    update_key_states(events)
    return get_movement_deltas()