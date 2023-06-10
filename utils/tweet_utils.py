
from utils.misc_utils import format_ordered_list
from utils.visual_utils import generate_bar_chart, generate_pie_chart, generateWordCloud

def extract_user_information(user):
    name = user.name
    username = user.screen_name
    bio = user.description
    followers_count = user.followers_count
    friends_count = user.friends_count
    return name, username, bio, followers_count, friends_count


def generate_summary_report(tweets, tweet_features, limit=5):
    print(tweet_features)

    hashtags = tweet_features['hashtags']
    mentions = tweet_features['mentions']
    urls = tweet_features['urls']
    all_emotions = tweet_features['emotions']
    all_nouns = tweet_features['nouns']
    top_liked_tweets = tweet_features['top_liked_tweets']
    top_retweeted_tweets = tweet_features['top_retweeted_tweets']
    top_viewed_tweets = tweet_features['top_viewed_tweets']
    tweet_count = len(tweets)


    report = f"## Tweet Analysis\n\n"
    # Extract top limit hashtags
    top_hashtags = format_ordered_list(hashtags[:limit])
    report += "### Top Hashtags\n\n"
    report += top_hashtags + "\n\n"

    # Extract top limit mentions
    top_mentions = format_ordered_list(mentions[:limit])
    report += "### Top Mentions\n\n"
    report += top_mentions + "\n\n"

    # Extract top limit URLs
    top_urls = format_ordered_list(urls[:limit])
    report += "### Top URLs\n\n"
    report += top_urls + "\n\n"

    # Extract tweets with most likes
    report += "### Tweets with Most Likes\n\n"
    for tweet, likes in top_liked_tweets[:limit]:
        report += f"- Likes: {likes}\n\n"
        report += f"{tweet}\n\n"

    # Extract tweets with most retweets
    report += "### Tweets with Most Retweets\n\n"
    for tweet, retweets in top_retweeted_tweets[:limit]:
        report += f"- Retweets: {retweets}\n\n"
        report += f"{tweet}\n\n"
    
    # generateWordCloud(all_nouns)
    generate_pie_chart(all_emotions,"Emotions Present")
    # generate_bar_chart(all_nouns)

    return report

