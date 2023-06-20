import streamlit as st
from TwitterAnalyser.pretty_print import PrettyPrint
from TwitterAnalyser.twitter_scraper import TwitterScraper


def main():
    pp = PrettyPrint()
    pp.create_streamlit_base()
	# st.info("Loading Scraper")
    ts = TwitterScraper()

    twitter_profile_url = st.text_input("Enter twitter username or profile link:")
    if not twitter_profile_url:
        twitter_profile_url = "https://twitter.com/elonmusk"
    if len(twitter_profile_url.split('/')) == 1:
        twitter_profile_url = f"https://twitter.com/{twitter_profile_url}"

    if st.button("Submit"):
        if twitter_profile_url:
            st.info("Fetching Profile...")
            user = ts.get_user_from_url(twitter_profile_url)
            pp.print_user_profile(user)
            tweets = ts.get_raw_tweets_from_user(user.username)
        else:
            st.warning("Please enter a valid twitter link.")



if __name__ == "__main__":
    main()
