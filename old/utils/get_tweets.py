import json
import tweepy
from dotenv import dotenv_values
import json
import snscrape.modules.twitter as sntwitter

env = dotenv_values('.env')

def fetch_tweets(profile_url, exclude_replies=True):
    username = profile_url.split("/")[-1]
    try:
        user = sntwitter.TwitterUserScraper(username).entity
        print("Fetched user details")
        print(user)

        tweets_generator = sntwitter.TwitterSearchScraper(f"from:{username} -filter:media").get_items()
        tweets = []
        max_count = 50
        for i, tweet in enumerate(tweets_generator):
            print(tweet.cashtags)
            # print(tweet.mentionedUsers[0])
            if i == max_count:
                break
            tweets.append(tweet)
        return tweets, user

    except Exception as e :
        print("Error:", str(e))
        return []

