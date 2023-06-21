import streamlit as st
from TwitterAnalyser.pretty_print import PrettyPrint
from TwitterAnalyser.twitter_scraper import TwitterScraper
from TwitterAnalyser.nouns_processor import NounsProcessor
from TwitterAnalyser.metadata_processor import MetaDataProcessor
from TwitterAnalyser.emotion_processor import EmotionProcessor
from TwitterAnalyser.visualiser import Visualiser


def main():
    pp = PrettyPrint()
    pp.create_streamlit_base()

    info_text = st.info("Loading preprocess classes")
    ts = TwitterScraper()
    npr = NounsProcessor()
    mdp = MetaDataProcessor()
    emp = EmotionProcessor()
    vsr = Visualiser()
    info_text = st.success("Preprocess classes loaded")

    twitter_profile_url = st.text_input(
        "Enter twitter username or profile link:")
    if not twitter_profile_url:
        twitter_profile_url = "https://twitter.com/elonmusk"
    if len(twitter_profile_url.split('/')) == 1:
        twitter_profile_url = f"https://twitter.com/{twitter_profile_url}"

    if st.button("Submit"):
        if twitter_profile_url:
            st.info("Fetching Profile...")
            user = ts.get_user_from_url(twitter_profile_url)
            pp.print_user_profile(user)

            st.info("Fetching tweets")
            tweets = ts.get_tweets_from_user_name(user.username)
            tweets_text = ts.get_tweet_text_from_tweets(tweets)
            st.success("Tweets fetched")

            st.title("Metadata Analysis")
            tweets_metadata = mdp.process_tweets_metadata(tweets)
            mdp.print_metadata_summary(tweets_metadata)

            st.title("Emotion Analysis")
            tweets_emotions = emp.get_emotions_from_text_array(tweets_text)
            vsr.generate_pie_chart(tweets_emotions, "Tweet Emotion Analysis")

            st.title("Entity Analysis")
            nouns = npr.get_nouns_from_tweets(tweets_text)
            vsr.generateWordCloud(nouns)
            vsr.generate_bar_chart(nouns)

        else:
            st.warning("Please enter a valid twitter link.")


if __name__ == "__main__":
    main()
