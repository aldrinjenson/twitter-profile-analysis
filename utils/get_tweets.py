import tweepy
from dotenv import dotenv_values
import json
import snscrape.modules.twitter as sntwitter

env = dotenv_values('.env')

def fetch_tweets(profile_url, exclude_replies=True):
    username = profile_url.split("/")[-1]
    try:
        user = sntwitter.TwitterUserScraper(username).entity
        print(user)
        print(user.statusesCount)
        print("Username:", user.displayname)
        print("Bio:", user.rawDescription)
        print("Followers Count:", user.followersCount)
        print("Friends Count:", user.friendsCount)
        print("--------------------")

        tweets_generator = sntwitter.TwitterSearchScraper(f"from:{username} -filter:media").get_items()
        tweets = []
        max_count = 10
        for i, tweet in enumerate(tweets_generator):
            if i == max_count:
                break
            tweets.append(tweet)
            print("Tweet:", tweet.rawContent)
            print("Likes:", tweet.likeCount)
            print("--------------------")
        return tweets, user

    except Exception as e :
        print("Error:", str(e))
        return []


if __name__ == "__main__":
    fetch_tweets('https://twitter.com/elonmusk')