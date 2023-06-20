from transformers import pipeline


class EmotionProcessor:
	emotion_classifier = None 

	def __init__(self):
		if not EmotionProcessor.emotion_classifier:
			print("Loading emotion classifier")
			EmotionProcessor.emotion_classifier = pipeline(
				"text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion")

	def _get_emotion_in_string(self, text_sting):
		emotion_scores = self.emotion_classifier(string)
		total_score = sum(emotion['score'] for emotion in emotion_scores[0])
		normalized_scores = [{'label': emotion['label'],
							  'score': emotion['score'] / total_score} for emotion in emotion_scores[0]]

		top_emotion_in_string = max(
			normalized_scores, key=lambda x: x['score'])
		top_label = top_emotion_in_string['label']
		confidence_score = top_emotion['score']
		print(string, confidence_score)

		return top_label

	def get_emotions_from_text_array(self, text_array):
		predictions = self.emotion_classifier(text_array)

		top_emotions = []
		for prediction in predictions:
			top_label = prediction['label']
			confidence_score = prediction['score']
			top_emotions.append(top_label)
			print(top_label, confidence_score)

		return top_emotions



