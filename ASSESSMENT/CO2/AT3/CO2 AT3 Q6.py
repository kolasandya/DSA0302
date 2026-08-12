def parser(word):

    irregular = {
        "children": "child",
        "men": "man",
        "women": "woman",
        "mice": "mouse",
        "geese": "goose",
        "feet": "foot",
        "teeth": "tooth"
    }

    if word in irregular:
        return word, irregular[word], "Plural Noun"

    elif word.endswith("ies"):
        return word, word[:-3] + "y", "Plural Noun"

    elif word.endswith("es"):
        return word, word[:-2], "Plural Noun"

    elif word.endswith("s"):
        return word, word[:-1], "Plural Noun"

    else:
        return word, word, "Singular"

words = ["cars", "boxes", "cities", "children"]

for w in words:
    print(parser(w))

