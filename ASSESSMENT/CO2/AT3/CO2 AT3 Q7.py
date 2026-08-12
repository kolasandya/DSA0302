documents = [
    "running runners runs",
    "studies studied studying",
    "organization organized organizer"
]
def stem_word(word):
    if word == "running":
        return "run"
    elif word == "runners":
        return "runner"
    elif word == "runs":
        return "run"
    elif word == "studies":
        return "studi"
    elif word == "studied":
        return "studi"
    elif word == "studying":
        return "studi"
    elif word == "organization":
        return "organ"
    elif word == "organized":
        return "organ"
    elif word == "organizer":
        return "organ"
    else:
        return word
stemmed_documents = []
for document in documents:
    words = document.split()
    stemmed_words = []
    for word in words:
        stemmed_words.append(stem_word(word))
    stemmed_documents.append(stemmed_words)
print("Original Documents:")
for document in documents:
    print(document)
print("\nStemmed Documents:")
for words in stemmed_documents:
  

  print(" ".join(words))
vocabulary = set()
for words in stemmed_documents:
    for word in words:
        vocabulary.add(word)
print("\nVocabulary:")
print(sorted(vocabulary))
print("\nVocabulary Size:")
print(len(vocabulary))

