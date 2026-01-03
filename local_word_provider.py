import json

WORDS_FILE = "words.json"

def load_words():
    with open(WORDS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def get_next_unused_word(used_words):
    words = load_words()
    for entry in words:
        if entry["word"].lower() not in used_words:
            return entry
    raise RuntimeError("No unused words left")

def format_post(entry):
    return (
        f"🇪🇸 Word of the Day: {entry['word']}\n\n"
        f"Meaning: {entry['meaning']}\n"
        f"Example: {entry['example_es']}\n"
        f"({entry['example_en']})\n\n"
        f"{entry['hashtags']}"
    )
