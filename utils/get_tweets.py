import tweepy
from dotenv import dotenv_values
import json

# Load the environment variables from .env file
env = dotenv_values('.env')

# Access the Twitter authentication keys
api_key = env['TWITTER_API_KEY']
api_secret = env['TWITTER_API_SECRET']
access_token = env['TWITTER_ACCESS_TOKEN']
access_token_secret = env['TWITTER_ACCESS_TOKEN_SECRET']


# Authenticate to Twitter API
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def fetch_tweets(profile_url, exclude_replies=True):
    username = profile_url.split("/")[-1]

    try:
        user = api.get_user(screen_name=username)
        print("Username:", user.screen_name)
        print("Bio:", user.description)
        print("Followers Count:", user.followers_count)
        print("Friends Count:", user.friends_count)
        print("--------------------")

        tweets = api.user_timeline(screen_name=username, count=60, tweet_mode="extended", exclude_replies=exclude_replies)
        for tweet in tweets:
            print("Tweet:", tweet.full_text)
            print("Likes:", tweet.favorite_count)
            print("--------------------")
        # filename = 'tweets.json'
        # save_tweets_to_json(tweets, filename)
        return tweets, user

    except tweepy.TweepError as e:
        print("Error:", str(e))
        return []
