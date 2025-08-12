#Named Entity Recognition is the process of identifying and categorizing key information (entities) in text.
from nltk import ne_chunk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

text = "Barack Obama was born in Hawaii. He was elected president in 2008."

words = word_tokenize(text)
pos_tags = pos_tag(words)

# Named Entity Recognition
named_entities = ne_chunk(pos_tags)
print("Named Entities:", named_entities)
