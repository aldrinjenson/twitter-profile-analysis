import streamlit as st
from utils.get_tweets import fetch_tweets
from utils.misc_utils import print_user_profile, create_streamlit_base
from utils.tweets_analyser import analyse_tweets



def main():
    create_streamlit_base()
    twitter_profile_url = st.text_input("Enter twitter link:")
    # twitter_profile_url = "https://twitter.com/elonmusk"
    if st.button("Submit"):
        if twitter_profile_url:
            info_text = st.info("Fetching Profile...")
            tweets, user = fetch_tweets(twitter_profile_url)

            info_text.empty()
            # info_text.empty()
            print_user_profile(user)
            analyse_tweets(tweets, user)
        else:
            st.warning("Please enter a valid twitter link.")


if __name__ == "__main__":
    main()
