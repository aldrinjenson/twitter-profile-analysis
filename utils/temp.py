import snscrape.modules.twitter as sntwitter

username = "elonmusk"  # Replace with the actual username

# Define the search query
query = f"from:{username} -filter:media"

# Fetch the tweets using the query
tweets = sntwitter.TwitterSearchScraper(query).get_items()

for i, tweet in enumerate(tweets):
    if i == 10:
        break
    print(tweet.content)
