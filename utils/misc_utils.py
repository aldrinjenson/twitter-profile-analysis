import streamlit as st
from PIL import Image
import requests
from io import BytesIO


def print_user_profile(user):
    col1, col2 = st.columns([1, 3])
    with col1:
        img_url = user.profile_image_url.replace('_normal.jpg', '.jpg')
        response = requests.get(img_url)
        image = Image.open(BytesIO(response.content))
        st.image(image, caption='Profile Picture' )
    with col2:
        st.subheader(f"{user.name} (@{user.screen_name})")
        st.write(f"Bio: {user.description}")
        st.write(f"Followers: {user.followers_count} | Following: {user.friends_count}")
        # st.write(f"Following: {user.friends_count}")
        st.write(f"Total Tweets: {user.statuses_count}")


def create_streamlit_base():
    st.title("Twitter Profile Analyser")
    st.markdown(
        "**Analyse a profile and get insights for you CyberSecurity Research!**")
    st.markdown("A person's tweets are an insight to their mind!"
                "Based on Twitter APIs the power of machine learning.")
    st.write(
        "Eg: try pasting this link maybe: https://twitter.com/elonmusk")

    # Remove Streamlit's made with Streamlit footer
    # st.markdown(
    #     '<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>', unsafe_allow_html=True)

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


def save_tweets_to_json(tweets, filename):
    with open(filename, 'w') as file:
        json.dump(tweets, file)


def format_ordered_list(items):
    return "\n".join([f"{i+1}. {item}" for i, item in enumerate(items)])
