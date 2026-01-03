from twitter_client import post_tweet

def main():
    text = (
        "🇪🇸 Word of the Day: Hola\n\n"
        "Meaning: Hello\n"
        "Example: Hola, ¿cómo estás?\n"
        "(Hello, how are you?)\n\n"
        "#Spanish #LearnSpanish"
    )

    post_tweet(text)

if __name__ == "__main__":
    main()
