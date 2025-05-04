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
    """Update key states from events."""
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

def handle_player_input(events):
    """Handle player input and return movement."""
    update_key_states(events)
    return _calculate_movement_deltas()

def _calculate_movement_deltas():
    """Calculate movement deltas."""
    dx, dy = 0, 0
    current_time = time.time()

    for action, state in key_states.items():
        if state["pressed"] and _can_move(state, current_time):
            dx, dy = _update_deltas(action, dx, dy)
            state["last_move_time"] = current_time

    return dx, dy

def _can_move(state, current_time):
    """Check if movement is allowed."""
    time_since_last_move = current_time - state["last_move_time"]
    return state["last_move_time"] == 0 or time_since_last_move >= KEY_REPEAT_DELAY or time_since_last_move >= KEY_REPEAT_INTERVAL

def _update_deltas(action, dx, dy):
    """Update movement deltas."""
    movement_map = {
        "MOVE_UP": (0, -1),
        "MOVE_DOWN": (0, 1),
        "MOVE_LEFT": (-1, 0),
        "MOVE_RIGHT": (1, 0),
    }
    delta = movement_map.get(action, (0, 0))
    return dx + delta[0], dy + delta[1]

def reset_key_states():
    """Reset all key states to unpressed."""
    for state in key_states.values():
        state["pressed"] = False
        state["last_move_time"] = 0

def get_key_state(action):
    """Get the current state of a specific key."""
    return key_states.get(action, {"pressed": False})["pressed"]