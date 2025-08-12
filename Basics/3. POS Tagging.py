#Part-of-Speech (POS) tagging is the process of marking up a word in a text as corresponding to a particular part of speech.
from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "Hello, how are you? I hope you are doing well. NLP is fun!"
words = word_tokenize(text)

# POS Tagging
pos_tags = pos_tag(words)
print("POS Tags:", pos_tags)
