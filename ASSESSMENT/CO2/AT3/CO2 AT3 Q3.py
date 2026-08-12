words = [
    "organization",
    "organizer",
    "organizing",
    "organized",
    "organization's"
]

def stem_word(word):
    if word == "organization":
        return "organ"
    elif word == "organizer":
        return "organ"
    elif word == "organizing":
        return "organ"
    elif word == "organized":
        return "organ"
    elif word == "organization's":
        return "organ"
    else:
        return word

print("Word\t\t\tStem")
print("--------------------------------")

for word in words:
    print(word, "\t\t", stem_word(word))
