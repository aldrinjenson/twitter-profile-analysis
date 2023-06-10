import nltk
import json
from nltk.sentiment import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

comments = []
with open('comments.json') as f:
    data = json.load(f)
    comments = data

print(data)


def analysis_sentiment(comments):
    sentimentMap = {"Positive": 0, "Negative": 0, "Neutral": 0}
    for comment in comments:
        sentiment_scores = sid.polarity_scores(comment)
        sentiment = sentiment_scores['compound']
        if sentiment >= 0.05:
            print(f"Positive: {comment}")
            sentimentMap["Positive"] += 1
        elif sentiment <= -0.05:
            print(f"Negative: {comment}")
            sentimentMap["Negative"] += 1
        else:
            print(f"Neutral: {comment}")
            sentimentMap["Neutral"] += 1

    print(sentimentMap)

    # return "This is a good video bro, you should watch this!"


if __name__ == "__main__":
    print('inside main')
    analysis_sentiment(comments)
