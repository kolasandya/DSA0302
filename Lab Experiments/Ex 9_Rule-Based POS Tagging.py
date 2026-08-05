import nltk
from nltk import word_tokenize, RegexpTagger

nltk.download('punkt')

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*es$', 'VBZ'),
    (r'.*ould$', 'MD'),
    (r'.*\'s$', 'NN$'),
    (r'.*s$', 'NNS'),
    (r'^[0-9]+$', 'CD'),
    (r'.*', 'NN')
]

tagger = RegexpTagger(patterns)

sentence = "The boys are playing football"
words = word_tokenize(sentence)

print(tagger.tag(words))