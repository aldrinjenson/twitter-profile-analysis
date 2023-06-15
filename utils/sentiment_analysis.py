from transformers import pipeline
import pickle
from utils.trainer import train_test_vectorizer_split

print("Loading classifier pipeline")
# emotion_classifier = pipeline(
#     "text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", return_all_scores=True)
print("Classifier pipeline loaded")
def emotion_classifier ():
    pass


def get_top_sentiment(text_array=[]):

    X_train_vec, X_test_vec, X_train,X_test,y_train,y_test = train_test_vectorizer_split(None,None)
    with open("../model.mdl", "rb") as file:
        model = pickle.load(file)
        print("model loaded")

        print("Predicting sentiments")
        y_pred = model.predict(X_test_vec)

        print(y_pred)




def getTopEmotion(string):
    emotion_scores = emotion_classifier(string)
    total_score = sum(emotion['score'] for emotion in emotion_scores[0])
    normalized_scores = [{'label': emotion['label'],
                          'score': emotion['score'] / total_score} for emotion in emotion_scores[0]]

    top_emotion = max(normalized_scores, key=lambda x: x['score'])
    top_label = top_emotion['label']
    confidence_score = top_emotion['score']

    return top_label, confidence_score

# preds = emotion_classifier(['I love you','I hate you', 'You suck bro','You dumb alla'])
# print(max(preds[0], key=lambda x: x['score']))
# print(max(preds[1], key=lambda x: x['score']))
# print(max(preds[2], key=lambda x: x['score']))
# print(max(preds[3], key=lambda x: x['score']))



if __name__ == "__main__":
    # getTopEmotion("Hello I love you!")
    get_top_sentiment()
