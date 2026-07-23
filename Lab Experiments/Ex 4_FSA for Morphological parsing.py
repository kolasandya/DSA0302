def plural(noun):
    if noun.endswith("y"):
        return noun[:-1] + "ies"
    elif noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"
    else:
        return noun + "s"

words = ["cat", "bus", "box", "baby", "dish"]

print("Plural Forms:")
for word in words:
    print(word, "->", plural(word))