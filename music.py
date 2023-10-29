def get_musical_keys():
    return {
        "Major": "Bright and happy sound. Follows a specific pattern of whole and half steps.",
        "Minor": "Somber or melancholic sound. Three types: natural, harmonic, and melodic minor.",
        "Chromatic": "Uses all twelve notes within the octave equally. Often found in atonal or serial compositions.",
        "Modal": "Based on ancient and medieval modes.",
        "Major Pentatonic": "Five-note scale derived from the major scale. Often used in folk, country, and rock music.",
        "Minor Pentatonic": "Five-note scale derived from the minor scale. Common in blues, rock, and jazz.",
        "Blues": "A six-note scale that adds a flattened fifth ('blue note') to the minor pentatonic scale. Widely used in blues music."
    }

def generate_scale(key, type_of_key):
    notes_sharp = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    notes_flat = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

    if key in ["F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb"]:
        notes = notes_flat
    else:
        notes = notes_sharp

    start_index = notes.index(key)
    scale = notes[start_index:] + notes[:start_index]

    if type_of_key == "Major":
        return [scale[i] for i in [0, 2, 4, 5, 7, 9, 11]]
    elif type_of_key == "Minor":
        return [scale[i] for i in [0, 2, 3, 5, 7, 8, 10]]
    elif type_of_key == "Chromatic":
        return scale
    elif type_of_key == "Major Pentatonic":
        return [scale[i] for i in [0, 2, 4, 7, 9]]
    elif type_of_key == "Minor Pentatonic":
        return [scale[i] for i in [0, 3, 5, 7, 10]]
    elif type_of_key == "Blues":
        return [scale[i] for i in [0, 3, 5, 6, 7, 10]]

def generate_modes(key):
    notes_sharp = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    notes_flat = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]

    if key in ["F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb"]:
        notes = notes_flat
    else:
        notes = notes_sharp

    start_index = notes.index(key)
    scale = notes[start_index:] + notes[:start_index]

    return {
        "Ionian (or Major)": scale,
        "Dorian": scale[1:] + scale[:1],
        "Phrygian": scale[2:] + scale[:2],
        "Lydian": scale[3:] + scale[:3],
        "Mixolydian": scale[4:] + scale[:4],
        "Aeolian (or Natural Minor)": scale[5:] + scale[:5],
        "Locrian": scale[6:] + scale[:6],
    }

def main():
    print("Welcome to the Terminal Game: Music Composition!")
    print("In this game, you'll explore different musical keys and their notes.")
    print("Here are the types of keys in Western music:")
    
    musical_keys = get_musical_keys()
    for key_type, description in musical_keys.items():
        print(f"{key_type} Key: {description}")

    type_of_key = input("Enter the type of key you're interested in (Major, Minor, Chromatic, Modal, Major Pentatonic, Minor Pentatonic, Blues): ").strip().title()
    while type_of_key not in musical_keys:
        print("Invalid key type. Please try again.")
        type_of_key = input("Enter the type of key you're interested in (Major, Minor, Chromatic, Modal, Major Pentatonic, Minor Pentatonic, Blues): ").strip().title()

    key = input("Enter the tonic note (e.g., C, D#, Gb): ").upper().strip()

    if type_of_key == 'Modal':
        modes = generate_modes(key)
        for mode_name, notes in modes.items():
            print(f"{mode_name} mode: {', '.join(notes)}")
    else:
        scale = generate_scale(key, type_of_key)
        print(f"{type_of_key} Scale in {key}: {', '.join(scale)}")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
