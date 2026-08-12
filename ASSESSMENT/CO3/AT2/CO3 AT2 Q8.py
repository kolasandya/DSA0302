tags = {
    "NN": "Noun",
    "VB": "Verb",
    "JJ": "Adjective",
    "RB": "Adverb",
    "DT": "Determiner",
    "VBZ": "3rd-person singular verb"
}

for tag, meaning in tags.items():
    print(tag, "=", meaning)

print("\nPOS tagging helps in:")
print("1. Intent Detection")
print("2. Response Generation")
print("3. Ambiguity Resolution")
print("4. Better Language Understanding")
