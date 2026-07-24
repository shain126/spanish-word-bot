from twitter_client import post_tweet
from claude_client import generate_spanish_word_post
from local_word_provider import get_next_unused_word, format_post
import re

USED_WORDS_FILE = "used_words.txt"

def load_used_words():
    try:
        with open(USED_WORDS_FILE, "r") as f:
            return set(line.strip().lower() for line in f if line.strip())
    except FileNotFoundError:
        return set()

def save_used_word(word):
    with open(USED_WORDS_FILE, "a") as f:
        f.write(word.lower() + "\n")

def extract_word(post_text):
    match = re.search(r"Word of the Day:\s*(.+)", post_text)
    return match.group(1).strip() if match else None

def main():
    used_words = load_used_words()

    try:
        post = generate_spanish_word_post(used_words)
        word = extract_word(post)
        if word is None:
            raise ValueError("Could not extract word from Claude response")
        source = "Claude CLI"
    except Exception:
        entry = get_next_unused_word(used_words)
        post = format_post(entry)
        word = entry["word"]
        source = "Local DB"

    post_tweet(post)
    save_used_word(word)
    print(f"Posted '{word}' via {source}")

if __name__ == "__main__":
    main()
