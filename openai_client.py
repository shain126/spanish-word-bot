import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_spanish_word_post():
    prompt = """
    Give ONE Spanish word for learners.
    Include:
    - The word
    - Its English meaning
    - One short example sentence in Spanish

    Keep it concise and tweet-friendly.
    """

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    return response.output_text.strip()
