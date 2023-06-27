import nltk
import re


class NounsProcessor:
	def __init__(self):
		try:
			nltk.data.find('tokenizers/punkt')
		except LookupError:
			print("Punkt not installed. Downloading..")
			nltk.download('punkt')

	def extract_entities(self, text):
		tokens = nltk.word_tokenize(text)
		tagged_words = nltk.pos_tag(tokens)
		nouns = [word for word, pos in tagged_words if pos.startswith('N') and len(
			word) > 2 and not word.startswith(("https", "http://", "https://", "//t.co"))]
		return nouns

	def get_nouns_from_tweets(self, tweets):
		nouns = []
		for tweet_text in tweets:
			nouns += self.extract_entities(tweet_text)
		return nouns





