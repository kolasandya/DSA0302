words = [
    "connected",
    "connection",
    "connecting",
    "studies",
    "studied",
    "studying",
    "players",
    "playing",
    "watched",
    "running"
]



def stem_word(word):
    if word == "connected":
        return "connect"
    elif word == "connection":
        return "connect"
    elif word == "connecting":
        return "connect"
    elif word == "studies":
        return "studi"
    elif word == "studied":
        return "studi"
    elif word == "studying":
        return "studi"
    elif word == "players":
        return "player"
    elif word == "playing":
        return "play"
    elif word == "watched":
        return "watch"
    elif word == "running":
        return "run"
    else:
        return word
print("Original Word\tStemmed Word")
print("-------------------------------")
for word in words:
    print(word, "\t\t", stem_word(word))
