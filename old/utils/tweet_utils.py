
from utils.misc_utils import format_ordered_list
from utils.visual_utils import generate_bar_chart, generate_pie_chart, generateWordCloud
import streamlit as st


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
    # report += f'<blockquote class="twitter-tweet"><p lang="en" dir="ltr">{tweet.rawContent}</p>&mdash; {tweet.username} (<a href="{tweet.url}">{tweet.username}</a>)</blockquote>'

    # Extract tweets with most likes
    report += "### Tweets with Most Likes\n\n"
    for tweet, likes in top_liked_tweets[:limit]:
        report += f"- Likes: {likes}\n\n"
        report += f"{tweet}\n\n"
    # report += "### Tweets with Most Likes\n\n"
    # for tweet, likes in top_liked_tweets[:limit]:
    #     tweet_url = tweet.url  # Assuming the tweet object has a 'url' attribute containing the URL of the original tweet
    #     report += f"- Likes: {likes}\n\n"
    #     report += f"[{tweet}]({tweet_url})\n\n"

    # Extract tweets with most retweets
    report += "### Tweets with Most Retweets\n\n"
    for tweet, retweets in top_retweeted_tweets[:limit]:
        report += f"- Retweets: {retweets}\n\n"
        report += f"{tweet}\n\n"

    generateWordCloud(all_nouns)
    col1, col2 = st.columns([1, 1])
    with col1:
        generate_pie_chart(all_emotions, "Emotions Present")
    with col2:
        generate_pie_chart(all_emotions, "Emotions Present")
    generate_bar_chart(all_nouns)

    return report
