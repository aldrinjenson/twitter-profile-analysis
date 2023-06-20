from transformers import pipeline
import pickle
from utils.trainer import train_test_vectorizer_split


def load_model():
    with open('model.mdl', 'rb') as file:
        return pickle.load(file)


global_model = None


def get_model():
    global global_model
    if global_model is None:
        global_model = load_model()
    return global_model


# Access the model
print('loading model')
model = get_model()
print("model loaded")

emotion_classifier_loaded = False
emotion_classifier = None

if not emotion_classifier:
    print("Loading classifier pipeline")
    emotion_classifier = pipeline(
        "text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", return_all_scores=True)
    print("Classifier pipeline loaded")




def get_top_sentiment(text_array=None):
    X_train_vec, X_test_vec, X_train, X_test, y_train, y_test = train_test_vectorizer_split(
        None, text_array)
    print("Predicting sentiments")
    y_pred = model.predict(X_test_vec)

    return y_pred


def getTopEmotion(string):
    print(string)
    emotion_scores = emotion_classifier(string)
    total_score = sum(emotion['score'] for emotion in emotion_scores[0])
    normalized_scores = [{'label': emotion['label'],
                          'score': emotion['score'] / total_score} for emotion in emotion_scores[0]]

    top_emotion = max(normalized_scores, key=lambda x: x['score'])
    top_label = top_emotion['label']
    confidence_score = top_emotion['score']

    return top_label, confidence_score

