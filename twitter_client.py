import os
import time
import tweepy

def _cred(name: str) -> str:
    raw = os.getenv(name) or ""
    cleaned = raw.strip()
    if len(raw) != len(cleaned):
        print(f"{name}: len={len(cleaned)} (stripped {len(raw) - len(cleaned)} whitespace char(s))")
    else:
        print(f"{name}: len={len(cleaned)}")
    return cleaned

def post_tweet(text: str, retries: int = 3, delay: int = 10):
    client = tweepy.Client(
        consumer_key=_cred("X_API_KEY"),
        consumer_secret=_cred("X_API_SECRET"),
        access_token=_cred("X_ACCESS_TOKEN"),
        access_token_secret=_cred("X_ACCESS_SECRET")
    )

    for attempt in range(1, retries + 1):
        try:
            response = client.create_tweet(text=text)
            print("Tweet posted with ID:", response.data["id"])
            return
        except tweepy.errors.TwitterServerError as e:
            if attempt < retries:
                print(f"Twitter server error (attempt {attempt}/{retries}): {e}. Retrying in {delay}s...")
                time.sleep(delay)
            else:
                raise
