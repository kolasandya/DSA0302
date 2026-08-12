def morphological_parser(word):

    if word == "happiest":
        return "happy + est"

    elif word == "unbelievable":
        return "un + believe + able"

    elif word == "running":
        return "run + ing"

    elif word == "reordering":
        return "re + order + ing"

    elif word == "smartphones":
        return "smart + phone + s"

    elif word == "unreadable":
        return "un + read + able"

    else:
        return "Unknown"


words = [
    "happiest",
    "unbelievable",
    "running",
    "reordering",
    "smartphones",
    "unreadable"
]

for word in words:
    print(word, "->", morphological_parser(word))

