import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')

text = "Machine learning is very useful"

words = nltk.word_tokenize(text)
tags = nltk.pos_tag(words)

print(tags)