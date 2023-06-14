from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

emotion_classifier = pipeline(
    "text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", return_all_scores=True)

vectorizer = TfidfVectorizer(max_features=5000)


def getTopEmotion(string):
    emotion_scores = emotion_classifier(string)
    total_score = sum(emotion['score'] for emotion in emotion_scores[0])
    normalized_scores = [{'label': emotion['label'],
                          'score': emotion['score'] / total_score} for emotion in emotion_scores[0]]

    top_emotion = max(normalized_scores, key=lambda x: x['score'])
    top_label = top_emotion['label']
    confidence_score = top_emotion['score']

    return top_label, confidence_score




if __name__ == "__main__":
    getTopSentiment("Hello I love you!")
