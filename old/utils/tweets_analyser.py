import streamlit as st
from transformers import pipeline
import nltk
from utils.tweet_utils import generate_summary_report
import re
from transformers import pipeline
from utils.sentiment_analysis import getTopEmotion, get_top_sentiment
from utils.visual_utils import generate_sentiment_bar_char


def extractEntities(text):
    tokens = nltk.word_tokenize(text)
    tagged_words = nltk.pos_tag(tokens)
    urls_present = re.findall(r'https?://\S+', text)
    nouns = [word for word, pos in tagged_words if pos.startswith('N') and len(
        word) > 2 and not word.startswith(("https", "http://", "https://", "//t.co"))]
    return nouns, urls_present


def get_features_from_tweet(tweets):
    hashtags = []
    mentions = []
    urls = []
    all_emotions = []
    all_nouns = []

    top_liked_tweets = []
    top_retweeted_tweets = []
    top_viewed_tweets = []

    for tweet in tweets:
        if tweet.hashtags:
            hashtags += tweet.hashtags
        if tweet.mentionedUsers:
            mentioned_usernames = [
                user.username for user in tweet.mentionedUsers]
        if tweet.links:
            urls += tweet.links

        tweet_text = tweet.rawContent
        nouns = extractEntities(tweet_text)[0]
        all_nouns += nouns
        top_emotion = getTopEmotion(tweet_text)[0]
        # top_emotion = "happy"
        all_emotions.append(top_emotion)

        if tweet.likeCount > 0:
            top_liked_tweets.append((tweet.rawContent, tweet.likeCount))

        if tweet.retweetCount > 0:
            top_retweeted_tweets.append(
                (tweet.rawContent, tweet.retweetCount))

        # if tweet.retweetCount > 0 and tweet.user.displayname == user.displayname:
        #     top_retweeted_tweets.append((tweet.rawContent, tweet.retweetCount))

    result = {
        'hashtags': hashtags,
        'mentions': mentions,
        'urls': urls,
        'emotions': all_emotions,
        'nouns': all_nouns,
        'top_liked_tweets': top_liked_tweets,
        'top_retweeted_tweets': top_retweeted_tweets,
        'top_viewed_tweets': top_viewed_tweets
    }
    return result
    # return hashtags, mentions, urls, all_emotions, all_nouns, top_liked_tweets, top_retweeted_tweets, top_viewed_tweets



def analyse_tweets(tweets, user):
    # tweets_text = [t.rawContent for t in tweets]
    # sentiments_array = get_top_sentiment(tweets_text)
    # generate_sentiment_bar_char(sentiments_array)
    tweet_features = get_features_from_tweet(tweets)
    print(tweet_features)
    summary_report = generate_summary_report(tweets, tweet_features)
    st.write(summary_report)

# summary_report = generate_summary_report(tweets, user)
# print(summary_report)
