import nltk
from nltk.tag import UnigramTagger, BigramTagger

# Training data
train_data = [
    [('The','DT'), ('dog','NN'), ('barks','VBZ')],
    [('A','DT'), ('cat','NN'), ('runs','VBZ')]
]

# Train unigram tagger
unigram = UnigramTagger(train_data)

# Train bigram tagger with unigram backoff
bigram = BigramTagger(train_data, backoff=unigram)

sentence = ["The", "cat", "barks"]

print(bigram.tag(sentence))