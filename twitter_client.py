import os
import time
import tweepy

def post_tweet(text: str, retries: int = 3, delay: int = 10):
    client = tweepy.Client(
        consumer_key=os.getenv("X_API_KEY"),
        consumer_secret=os.getenv("X_API_SECRET"),
        access_token=os.getenv("X_ACCESS_TOKEN"),
        access_token_secret=os.getenv("X_ACCESS_SECRET")
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
