import streamlit as st
import time
from itertools import islice
from youtube_comment_downloader import *
from sentiment_analyser import analysis_sentiment

downloader = YoutubeCommentDownloader()


def get_comments(youtube_link):
    # Code to fetch comments from YouTube API
    # Replace this with your own implementation

    # Simulating a delay to show loading message
    # time.sleep(3)
    comments_generator = downloader.get_comments_from_url(
        youtube_link, sort_by=SORT_BY_POPULAR)
    comments = []

    for comment in islice(comments_generator, 50):
        comments.append(comment["text"])

    # Returning sample comments for demonstration
    # comments = ["Great video!", "Interesting analysis", "Nice work!"]
    print(comments)
    return comments


def main():
    # Set app title and description
    st.title("Youtube Video Sentiment Analysis")
    st.markdown("**Save your time before watching a YouTube video!**")
    st.markdown("Analyse YouTube videos to get sentiment analysis and understand what people think. "
                "Based on popular YouTube comments and using the power of machine learning.")
    st.write(
        "Eg: try pasting this link maybe: https://www.youtube.com/watch?v=c7Dg8zkTmHI")

    # Remove Streamlit's made with Streamlit footer
    st.markdown(
        '<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>', unsafe_allow_html=True)

    # Sidebar
    st.sidebar.title("Created by Aldrin Jenson")
    st.sidebar.markdown(
        "[Aldrin Jenson](https://aldrinjenson.tech)"
    )

    st.sidebar.markdown("#### Connect with me:")
    st.sidebar.markdown("[GitHub](https://github.com/aldrinjenson)")
    st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/aldrinjenson)")
    st.sidebar.markdown("[Twitter](https://twitter.com/aldrinjenson)")
    st.sidebar.markdown("Email: mdl19cs008@mec.ac.in")

    youtube_link = st.text_input("Enter YouTube link:")
    if st.button("Submit"):
        if youtube_link:
            info_text = st.info("Fetching comments... Please wait.")
            comments = get_comments(youtube_link)
            info_text.empty()
            sentiment_text = analysis_sentiment(comments)
            st.success("Sentiment Analysis:")
            st.write(sentiment_text)
        else:
            st.warning("Please enter a valid YouTube link.")


if __name__ == "__main__":
    main()
