from . import json

def save_state(state_id, state_value, valid_modes, STATE_FILE='user_states.json'):
    # Cek apakah mode valid
    if state_value not in valid_modes:
        return 0

    # Baca data lama dari file
    try:
        with open(STATE_FILE, 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}  # Jika file tidak ditemukan atau kosong, buat dict kosong

    # Update state
    data[state_id] = state_value

    # Simpan data yang diperbarui ke file
    with open(STATE_FILE, 'w') as file:
        json.dump(data, file)

    return 1