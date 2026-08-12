sentence1 = {
    "Book": "VB",
    "a": "DT",
    "flight": "NN",
    "ticket": "NN",
    "now": "RB"
}

sentence2 = {
    "This": "DT",
    "book": "NN",
    "is": "VBZ",
    "interesting": "JJ"
}

print("Sentence 1:")
for word, tag in sentence1.items():
    print(word, "/", tag)

print("\nSentence 2:")
for word, tag in sentence2.items():
    print(word, "/", tag)
