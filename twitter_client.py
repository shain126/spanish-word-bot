import tweepy
import os

def post_tweet(text: str):
    client = tweepy.Client(
        consumer_key=os.getenv("X_API_KEY"),
        consumer_secret=os.getenv("X_API_SECRET"),
        access_token=os.getenv("X_ACCESS_TOKEN"),
        access_token_secret=os.getenv("X_ACCESS_SECRET")
    )

    response = client.create_tweet(text=text)
    print("Tweet posted with ID:", response.data["id"])
