#Sentiment analysis is the process of determining the sentiment or emotion expressed in a text.
from nltk.sentiment import SentimentIntensityAnalyzer

text = "I love this product! It's amazing."

sia = SentimentIntensityAnalyzer()
sentiment = sia.polarity_scores(text)
print("Sentiment:", sentiment)
