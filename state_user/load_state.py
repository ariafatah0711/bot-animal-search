from . import json

def load_state(STATE_FILE = 'user_states.json'):
    try:
        with open(STATE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}