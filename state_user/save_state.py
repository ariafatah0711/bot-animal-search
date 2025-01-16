from . import json

def save_state(state_id, state_value, valid_modes, STATE_FILE = 'user_states.json'):
    data = {state_id: state_value}

    if state_value not in valid_modes:
        return 0
    
    with open (STATE_FILE, 'w') as file:
        json.dump(data, file)
    return 1