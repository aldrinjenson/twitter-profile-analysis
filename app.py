import streamlit as st
import time
from sentiment_analyser import analysis_sentiment

def main():
    st.title("Twitter Profile Analyser")
    st.markdown("**Analyse a profile and get insights for you CyberSecurity Research!**")
    st.markdown("A person's tweets are an insight to their mind!"
                "Based on Twitter APIs the power of machine learning.")
    st.write(
        "Eg: try pasting this link maybe: https://twitter.com/elonmusk")

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

    twitter_link = st.text_input("Enter twitter link:")
    if st.button("Submit"):
        if twitter_link:
            info_text = st.info("Performing analysis... Please wait.")
            # comments = get_comments(twitter_link)
            # info_text.empty()
            # sentiment_text = analysis_sentiment(comments)
            st.success("Sentiment Analysis:")
            st.write(sentiment_text)
        else:
            st.warning("Please enter a valid twitter link.")


if __name__ == "__main__":
    main()
