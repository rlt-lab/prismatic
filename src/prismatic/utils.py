import json
from pathlib import Path

def load_json(filename):
    """Load JSON from the data directory."""
    path = Path(__file__).parent / "data" / filename
    with open(path, "r") as f:
        return json.load(f)