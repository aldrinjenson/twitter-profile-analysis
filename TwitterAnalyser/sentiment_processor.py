from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import pandas as pd


class SentimentProcessor:
	model = None
	vectorizer = None

	def __init__(self):
		if not SentimentProcessor.model:
			print("Loading Sentiment Processor Model")
			with open('model.mdl', 'rb') as file:
				SentimentProcessor.model = pickle.load(file)
		if not SentimentProcessor.vectorizer:
			print("Reading tweets from csv")
			df = pd.read_csv("./tweets_data.csv", encoding="latin-1", header=None)
			df.columns = ["target", "ids", "date", "flag", "user", "text"]
			vectorizer = TfidfVectorizer(max_features=5000)
			X = df["text"]
			y = df["target"]
			X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
			print("Vectorizing X_train tweets")
			vectorizer.fit_transform(X_train)
			SentimentProcessor.vectorizer = vectorizer



	def get_sentiment_in_text_array(self, text_array):
		print("Predicting Sentiment")
		vectorized_test_array = self.vectorizer.transform(text_array)
		predictions = self.model.predict(vectorized_test_array)
		return predictions
