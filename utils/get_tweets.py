import tweepy
from dotenv import dotenv_values
import json

env = dotenv_values('.env')

api_key = env['TWITTER_API_KEY']
api_secret = env['TWITTER_API_SECRET']
access_token = env['TWITTER_ACCESS_TOKEN']
access_token_secret = env['TWITTER_ACCESS_TOKEN_SECRET']


# auth = tweepy.OAuthHandler(api_key, api_secret)
# # client = tweepy.Client("Bearer Token here")
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)

client = tweepy.Client("")
api = client

def fetch_tweets(profile_url, exclude_replies=True):
    username = profile_url.split("/")[-1]
    print(('ok'))

    try:
        u=api.get_user(username=username)
        print(u)
        print(('hehe'))
        user = api.get_user(screen_name=username)
        print('bro')
        print(user)
        print("Username:", user.screen_name)
        print("Bio:", user.description)
        print("Followers Count:", user.followers_count)
        print("Friends Count:", user.friends_count)
        print("--------------------")

        tweets = api.user_timeline(screen_name=username, count=100, tweet_mode="extended", exclude_replies=exclude_replies)
        for tweet in tweets:
            print("Tweet:", tweet.full_text)
            print("Likes:", tweet.favorite_count)
            print("--------------------")
        return tweets, user

    except Exception as e :
        print("Error:", str(e))
        return []
