import streamlit as st
from transformers import pipeline
import nltk
from utils.tweet_utils import generate_summary_report
import re


def extractEntities(text):
    tokens = nltk.word_tokenize(text)
    tagged_words = nltk.pos_tag(tokens)
    urls_present = re.findall(r'https?://\S+', text)
    nouns = [word for word, pos in tagged_words if pos.startswith('N') and len(word) > 2 and not word.startswith(("https", "http://", "https://", "//t.co"))]
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
        hashtags += [tag['text'] for tag in tweet.entities['hashtags']]
        mentions += [mention['screen_name']
                     for mention in tweet.entities['user_mentions']]
        urls += [url['expanded_url'] for url in tweet.entities['urls']]

        tweet_text = tweet.full_text
        nouns = extractEntities(tweet_text)[0]
        # nouns = []
        all_nouns += nouns
        # top_emotion = getTopEmotion(tweet_text)[0]
        top_emotion = "happy"
        all_emotions.append(top_emotion)

        if tweet.favorite_count > 0:
            top_liked_tweets.append((tweet.full_text, tweet.favorite_count))

        if tweet.retweet_count > 0:
            top_retweeted_tweets.append((tweet.full_text, tweet.retweet_count))

        # if tweet.retweet_count > 0 and tweet.user.screen_name == user.screen_name:
        #     top_retweeted_tweets.append((tweet.full_text, tweet.retweet_count))

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
    tweet_features = get_features_from_tweet(tweets)
    print(tweet_features)
    summary_report = generate_summary_report(tweets, tweet_features)
    st.write(summary_report)

# summary_report = generate_summary_report(tweets, user)
# print(summary_report)
