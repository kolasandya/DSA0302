words = ["infect", "infection", "infected", "infectious"]

stems = {
    "infect": "infect",
    "infection": "infect",
    "infected": "infect",
    "infectious": "infect"
}

print("Word\t\tStem")

for word in words:
    print(word, "\t\t", stems[word])
