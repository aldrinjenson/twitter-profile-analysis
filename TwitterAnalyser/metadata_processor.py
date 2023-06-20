import datetime
import streamlit as st


class MetaDataProcessor:

    def __init__(self, top_hashtags_limit=5, top_mentions_limit=5):
        self.top_hashtags_limit = top_hashtags_limit
        self.top_mentions_limit = top_mentions_limit

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
            "mentionedUsers": [user.username for user in tweet.mentionedUsers] if tweet.mentionedUsers else []
        }
        return metadata

    def process_tweets_metadata(self, tweets):
        metadata = {
            "hashtags": [],
            "mentionedUsers": []
        }

        for tweet in tweets:
            tweet_metadata = self.extract_metadata(tweet)
            metadata['hashtags'] += tweet_metadata["hashtags"]
            metadata["mentionedUsers"] += tweet_metadata["mentionedUsers"]
        return metadata

    def _format_ordered_list(self, items, limit=5):
        unique_items = list(set(items))
        limited_items = unique_items[:limit]
        return "\n".join([f"{i+1}. {item}" for i, item in enumerate(limited_items)])

    def print_metadata_summary(self, metadata):
        hashtags = metadata["hashtags"]
        mentions = metadata["mentionedUsers"]

        report = f"## Tweet Analysis\n\n"
        top_hashtags = self._format_ordered_list(hashtags, self.top_hashtags_limit)
        report += "## Top Hashtags\n\n"
        report += top_hashtags + "\n\n"

        top_mentions = self._format_ordered_list(mentions,self.top_mentions_limit)
        report += "## Top Mentions\n\n"
        report += top_mentions + "\n\n"

        st.write(report)
