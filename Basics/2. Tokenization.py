#Tokenization is the process of splitting text into individual words or sentences.
from nltk.tokenize import word_tokenize, sent_tokenize

text = "Hello, how are you? I hope you are doing well. NLP is fun!"

# Sentence Tokenization
sentences = sent_tokenize(text)
print("Sentences:", sentences)

# Word Tokenization
words = word_tokenize(text)
print("Words:", words)
