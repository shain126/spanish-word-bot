import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_spanish_word_post(used_words: set):
    banned = ", ".join(sorted(used_words)) if used_words else "none"

    prompt = f"""
    Give ONE Spanish word for learners.

    Rules:
    - The word MUST NOT be any of these: {banned}
    - Use a different word than all previous ones
    - Beginner to intermediate level

    Format EXACTLY like this:

    🇪🇸 Word of the Day: <word>

    Meaning: <meaning>
    Example: <spanish sentence>
    (<english translation>)

    Include hashtags: #Spanish #LearnSpanish
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text.strip()
