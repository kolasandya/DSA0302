import nltk

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*ly$', 'RB'),
    (r'.*ness$', 'NN'),
    (r'.*', 'NN')
]

tagger = nltk.RegexpTagger(patterns)

words = ["playing", "walked", "quickly", "happiness", "dog"]

print(tagger.tag(words))