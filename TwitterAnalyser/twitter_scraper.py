import snscrape.modules.twitter as sntwitter


class TwitterScraper:
    exclude_replies = True
    max_tweet_count = 40

    def __init__(self, exclude_replies=True, max_tweet_count=60):
        self.exclude_replies = exclude_replies
        self.max_tweet_count = max_tweet_count

    def get_user_from_url(self, profile_url):
        try:
            username = profile_url.split("/")[-1]
            user = sntwitter.TwitterUserScraper(username).entity
            print("Fetched user details")
            print(user.username)
            return user
        except Exception as e:
            print("Error:", str(e))
            return None


    def get_tweets_from_user_name(self, username):
        print(f"Fetching tweets from {username}")
        tweets_generator = sntwitter.TwitterSearchScraper(f"from:{username} -filter:media").get_items()
        tweets = []
        for i, tweet in enumerate(tweets_generator):
            print(tweet.links)
            if i == self.max_tweet_count: break
            tweets.append(tweet)
        return tweets
    
    def get_tweet_text_from_tweets(self,tweets):
        tweet_texts = []
        for tweet in tweets:
            tweet_texts.append(tweet.rawContent)
        return tweet_texts

