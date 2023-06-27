import nltk
import re


class NounsProcessor:
	def __init__(self):
		try:
			nltk.data.find('tokenizers/punkt')
			nltk.data.find('taggers/averaged_perceptron_tagger')
		except LookupError:
			# Download the missing resources
			nltk.download('punkt')
			nltk.download('averaged_perceptron_tagger')

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





