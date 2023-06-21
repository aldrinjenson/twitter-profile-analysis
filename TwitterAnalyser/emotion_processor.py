from transformers import pipeline


class EmotionProcessor:
	emotion_classifier = None 

	def __init__(self):
		if not EmotionProcessor.emotion_classifier:
			print("Loading emotion classifier")
			EmotionProcessor.emotion_classifier = pipeline(
				"text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")


	def get_emotions_from_text_array(self, text_array):
		predictions = self.emotion_classifier(text_array)

		top_emotions = []
		for prediction in predictions:
			top_label = prediction['label']
			confidence_score = prediction['score']
			top_emotions.append(top_label)
			# print(top_label, confidence_score)

		return top_emotions



