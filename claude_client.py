import subprocess

def generate_spanish_word_post(used_words: set):
    banned = ", ".join(sorted(used_words)) if used_words else "none"

    prompt = f"""
    Give ONE Spanish word for learners.

    Rules:
    - The word MUST NOT be any of these: {banned}
    - Use a different word than all previous ones
    - Beginner to intermediate level

    Output ONLY the post text, nothing else. Format EXACTLY like this:

    🇪🇸 Word of the Day: <word>

    Meaning: <meaning>
    Example: <spanish sentence>
    (<english translation>)

    Include hashtags: #Spanish #LearnSpanish
    """

    result = subprocess.run(
        ["claude", "-p", prompt],
        capture_output=True,
        text=True,
        timeout=120,
    )

    if result.returncode != 0:
        raise RuntimeError(f"claude CLI failed: {result.stderr.strip()}")

    return result.stdout.strip()
