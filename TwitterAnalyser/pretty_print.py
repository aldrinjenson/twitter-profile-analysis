import streamlit as st
import requests
from PIL import Image
from io import BytesIO


class PrettyPrint:
    @staticmethod
    def print_user_profile(user):
        col1, col2 = st.columns([1, 3])
        with col1:
            img_url = user.profileImageUrl.replace('_normal.jpg', '.jpg')
            response = requests.get(img_url)
            image = Image.open(BytesIO(response.content))
            st.image(image, caption='Profile Picture')
        with col2:
            st.subheader(f"{user.displayname} (@{user.displayname})")
            st.write(f"Bio: {user.rawDescription}")
            st.write(
                f"Followers: {user.followersCount} | Following: {user.friendsCount}")
            # st.write(f"Following: {user.friendsCount}")
            st.write(f"Total Tweets: {user.statusesCount}")

    @staticmethod
    def create_streamlit_base():
        st.title("Twitter Profile Analyser")
        st.markdown(
            "**Analyse a profile and get insights for you CyberSecurity Research!**")
        st.markdown("A person's tweets are an insight to their mind!"
                    "Based on Twitter APIs the power of machine learning.")
        st.write(
            "Eg: try pasting this link maybe: https://twitter.com/elonmusk")

        st.markdown('<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>', unsafe_allow_html=True)
        # Remove Streamlit's made with Streamlit footer
        st.markdown(
            '<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>', unsafe_allow_html=True)

        # Sidebar
        st.sidebar.title("Created by Aldrin Jenson")
        st.sidebar.markdown(
            "[Aldrin Jenson](https://aldrinjenson.tech)"
        )

        st.sidebar.markdown("### Connect with me:")
        st.sidebar.markdown("[GitHub](https://github.com/aldrinjenson)")
        st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/aldrinjenson)")
        st.sidebar.markdown("[Twitter](https://twitter.com/aldrinjenson)")
        st.sidebar.markdown("Email: mdl19cs008@mec.ac.in")

