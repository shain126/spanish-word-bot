from twitter_client import post_tweet
from openai_client import generate_spanish_word_post
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
    match = re.search(r"Word of the Day:\s*(\w+)", post_text)
    return match.group(1) if match else None

def main():
    used_words = load_used_words()

    post = generate_spanish_word_post(used_words)
    word = extract_word(post)

    if not word:
        raise RuntimeError("Could not extract word from OpenAI output")

    if word.lower() in used_words:
        raise RuntimeError("Duplicate word generated — aborting")

    post_tweet(post)
    save_used_word(word)

if __name__ == "__main__":
    main()
