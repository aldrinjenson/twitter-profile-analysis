import streamlit as st
from TwitterAnalyser.pretty_print import PrettyPrint
from TwitterAnalyser.twitter_scraper import TwitterScraper
from TwitterAnalyser.nouns_processor import NounsProcessor
from TwitterAnalyser.metadata_processor import MetaDataProcessor
from TwitterAnalyser.emotion_processor import EmotionProcessor
from TwitterAnalyser.sentiment_processor import SentimentProcessor
from TwitterAnalyser.visualiser import Visualiser


def main():
	pp = PrettyPrint()
	pp.create_streamlit_base()
	notification_msg = st.empty()

	notification_msg.info("Loading preprocess classes...")
	ts = TwitterScraper()
	# sp = SentimentProcessor()
	npr = NounsProcessor()
	mdp = MetaDataProcessor()
	emp = EmotionProcessor()
	vsr = Visualiser()
	notification_msg.success("Preprocess classes loaded")

	twitter_profile_url = st.text_input(
		"Enter twitter username or profile link:")

	if not twitter_profile_url:
		twitter_profile_url = "https://twitter.com/elonmusk"
	if len(twitter_profile_url.split('/')) == 1:
		twitter_profile_url = f"https://twitter.com/{twitter_profile_url}"

	if st.button("Submit"):
		if twitter_profile_url:
			notification_msg.info("Fetching Profile...")
			user = ts.get_user_from_url(twitter_profile_url)
			if user is None:
				notification_msg.info("Invlid username or profile! Check and try again")
				return
			username = user.username
			pp.print_user_profile(user)

			notification_msg.info(f"Fetching tweets by @{user.username}...")
			tweets = ts.get_tweets_from_user_name(user.username)
			tweets_text = ts.get_tweet_text_from_tweets(tweets)
			notification_msg.success("Tweets fetched")

			st.title("Metadata Analysis")
			st.write(f"Analysis from tweets of @{username} without using any ML models, purely based on metadata")
			tweets_metadata = mdp.process_tweets_metadata(tweets)
			mdp.print_metadata_summary(tweets_metadata)

			notification_msg.info("Performing ML models based Analysis...")
			st.title("Deep Learning analysis")
			st.write("Tweet analysis using several Deep Learning and ML based models")
			st.title("Emotion Analysis")
			tweets_emotions = emp.get_emotions_from_text_array(tweets_text)
			vsr.generate_pie_chart(tweets_emotions, "Tweet Emotion Analysis")

			st.title("Entity Analysis")
			st.write(f"Common Nouns and keywords used by @{username}")
			nouns = npr.get_nouns_from_tweets(tweets_text)
			vsr.generateWordCloud(nouns)
			vsr.generate_bar_chart(nouns)

			st.title("Sentiment Analysis")
			st.write(f"Amount of Positivity and Negativity in tweets by @{username}")
			tweets_sentiments = sp.get_sentiment_in_text_array(tweets_text)
			vsr.generate_sentiment_bar_char(tweets_sentiments)

			notification_msg.empty()
		else:
			st.warning("Please enter a valid twitter link.")


if __name__ == "__main__":
	main()
