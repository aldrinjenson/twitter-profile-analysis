import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
from urllib.parse import urlparse
import random

def generate_pie_chart(arr,title):
    arr_counts = Counter(arr)
    labels, counts = zip(*arr_counts.items())
    labels = [label.capitalize() for label in labels]
    plt.pie(counts, labels=labels, autopct='%1.1f%%')
    plt.title(title)
    st.show()
    
 
def generateWordCloud(words):
    entities_text = ' '.join(words)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(entities_text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.show()   


def generate_bar_chart(keywords, num_show=10, title="Top Keyword Occurrences"):
    keyword_counts = Counter(keywords)
    sorted_keywords = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)
    top_keywords = sorted_keywords[:num_show]
    
    labels = [keyword[0] for keyword in top_keywords]
    counts = [keyword[1] for keyword in top_keywords]
    
    colors = [random.choice(['#'+format(random.randint(0, 16777215), '06x') for _ in range(6)]) for _ in range(num_show)]
    
    plt.figure(figsize=(10, 6))
    plt.bar(labels, counts, color=colors)
    plt.xticks(rotation=45)
    plt.xlabel("Keywords")
    plt.ylabel("Occurrences")
    plt.title(title)
    
    plt.tight_layout()
    st.show()

