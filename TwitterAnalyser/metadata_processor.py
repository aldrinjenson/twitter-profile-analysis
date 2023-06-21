import datetime
import streamlit as st
import streamlit.components.v1 as components
import datetime


class MetaDataProcessor:

    def __init__(self, top_hashtags_limit=5, top_mentions_limit=5, top_links_limit=5):
        self.top_hashtags_limit = top_hashtags_limit
        self.top_mentions_limit = top_mentions_limit
        self.top_links_limit = top_links_limit
        self.top_liked_tweet_limit = 5

    def extract_metadata(self, tweet):
        metadata = {
            "URL": tweet.url,
            "Date": tweet.date.strftime("%Y-%m-%d %H:%M:%S"),
            "Content": tweet.rawContent,
            "Username": tweet.user.username,
            "ReplyCount": tweet.replyCount,
            "RetweetCount": tweet.retweetCount,
            "LikeCount": tweet.likeCount,
            "QuoteCount": tweet.quoteCount,
            "hashtags": tweet.hashtags or [],
            "mentionedUsers": [user.username for user in tweet.mentionedUsers] if tweet.mentionedUsers else [],
            "links": [tl.url for tl in tweet.links] if tweet.links else []
        }
        return metadata

    def process_tweets_metadata(self, tweets):
        metadata = {
            "hashtags": [],
            "mentionedUsers": [],
            "links": []
        }

        for tweet in tweets:
            tweet_metadata = self.extract_metadata(tweet)
            metadata['hashtags'] += tweet_metadata["hashtags"]
            metadata["mentionedUsers"] += tweet_metadata["mentionedUsers"]
            metadata["links"] += tweet_metadata["links"]

        metadata["top_liked_tweets"] = sorted(
            tweets, key=lambda x: x.likeCount, reverse=True)[:self.top_liked_tweet_limit]
        metadata["top_retweeted_tweets"] = sorted(
            tweets, key=lambda x: x.retweetCount, reverse=True)[:5]
        metadata["top_quoted_tweets"] = sorted(
            tweets, key=lambda x: x.quoteCount, reverse=True)[:5]

        return metadata

    def _format_ordered_list(self, items, limit=5, prefix=""):
        unique_items = list(set(items))
        limited_items = unique_items[:limit]
        return "\n".join([f"{i+1}. {prefix}{item}" for i, item in enumerate(limited_items)])

    def print_metadata_summary(self, metadata):
        hashtags = metadata["hashtags"]
        mentions = metadata["mentionedUsers"]
        links = metadata["links"]
        top_quoted_tweets = metadata["top_quoted_tweets"]
        top_liked_tweets = metadata["top_liked_tweets"]

        report = ""
        top_hashtags = self._format_ordered_list(
            hashtags, self.top_hashtags_limit, '#')
        report += "## Top Hashtags Used\n\n"
        report += top_hashtags + "\n\n"

        top_mentions = self._format_ordered_list(
            mentions, self.top_mentions_limit, '@')
        report += "## Top Mentions\n\n"
        report += top_mentions + "\n\n"

        top_links = self._format_ordered_list(links, self.top_links_limit, '')
        report += "## Top Links\n\n"
        report += top_links + "\n\n"

        st.write(report)

        report = "## Most Popular Tweets (based on likes) ##\n\n"

        for tweet in top_liked_tweets:
            report += f"> **Tweet:** {tweet.rawContent}\n" \
                    f"> **Posted on:** {tweet.date.strftime('%Y-%m-%d %H:%M:%S')} | " \
                    f"**Likes:** {tweet.likeCount} | " \
                    f"**Retweets:** {tweet.retweetCount} | " \
                    f"**Replies:** {tweet.replyCount}\n\n"
        report += "---"
