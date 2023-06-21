import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
from urllib.parse import urlparse
import random


class Visualiser:

    @staticmethod
    def generate_pie_chart(arr, title):
        arr_counts = Counter(arr)
        labels, counts = zip(*arr_counts.items())
        labels = [label.capitalize() for label in labels]

        fig, ax = plt.subplots()
        ax.pie(counts, labels=labels, autopct='%1.1f%%')
        ax.set_title(title)

        st.pyplot(fig)

    @staticmethod
    def generateWordCloud(words):
        entities_text = ' '.join(words)
        wordcloud = WordCloud(width=800, height=400,
                              background_color='white').generate(entities_text)
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)

    @staticmethod
    def generate_bar_chart(keywords, num_show=10, title="Top Keyword Occurrences"):
        keyword_counts = Counter(keywords)
        sorted_keywords = sorted(keyword_counts.items(),
                                 key=lambda x: x[1], reverse=True)
        top_keywords = sorted_keywords[:num_show]

        labels = [keyword[0] for keyword in top_keywords]
        counts = [keyword[1] for keyword in top_keywords]

        colors = [random.choice(['#'+format(random.randint(0, 16777215), '06x')
                                for _ in range(6)]) for _ in range(num_show)]

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(labels, counts, color=colors)
        ax.set_xticklabels(labels, rotation=45)
        ax.set_xlabel("Keywords")
        ax.set_ylabel("Occurrences")
        ax.set_title(title)

        plt.tight_layout()
        st.pyplot(fig)

    @staticmethod
    def generate_sentiment_bar_char(data):

        fig, ax = plt.subplots(figsize=(10, 6))
        labels = ["Positive", "Negative"]

        counter = Counter(data)
        positive_count = counter[4]
        negative_count = counter[0]
        print(counter)
        st.markdown(f"Positive Tweets = {positive_count}\nNegative Tweets = {negative_count}")
        ax.bar(labels, [positive_count, negative_count], color=["blue", "red"])
        ax.set_xticklabels(labels, rotation=45)
        ax.set_xlabel("Sentiment")
        ax.set_ylabel("Tweet count")
        ax.set_title("Sentiment Distribution")

        plt.tight_layout()
        st.pyplot(fig)
