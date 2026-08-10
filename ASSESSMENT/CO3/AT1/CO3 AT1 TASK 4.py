import re
from collections import Counter

tags = {
    "i":"PRP", "you":"PRP", "he":"PRP", "she":"PRP",
    "the":"DT", "a":"DT",
    "is":"VBZ", "am":"VBP", "are":"VBP",
    "like":"VB", "likes":"VBZ",
    "play":"VB", "plays":"VBZ",
    "good":"JJ", "beautiful":"JJ",
    "quickly":"RB",
    "in":"IN", "on":"IN", "at":"IN",
    "and":"CC", "but":"CC"
}

def rule_based(sentence):
    words = sentence.lower().split()
    result = []

    for w in words:
        if w in tags:
            t = tags[w]
        elif w.endswith("ly"):
            t = "RB"
        elif w.endswith("ing"):
            t = "VBG"
        else:
            t = "NN"

        result.append((w, t))

    return result


def stochastic(sentence):
    # Simple tag-frequency model
    train = [
        ("she","PRP"), ("likes","VBZ"),
        ("good","JJ"), ("books","NNS")
    ]

    freq = Counter(t for w, t in train)

    result = []

    for w, t in rule_based(sentence):
        if w in dict(train):
            t = dict(train)[w]
        else:
            t = max(freq, key=freq.get)

        result.append((w, t))

    return result


def transformation(sentence):
    result = rule_based(sentence)

    for i in range(1, len(result)):
        word, tag = result[i]
        prev_word, prev_tag = result[i-1]

        if prev_tag == "PRP" and tag == "NN":
            tag = "VB"

        if word.endswith("ly"):
            tag = "RB"

        result[i] = (word, tag)

    return result


sentence = input("Enter sentence: ")

print("\nRule Based:")
print(rule_based(sentence))

print("\nStochastic:")
print(stochastic(sentence))

print("\nTransformation Based:")
print(transformation(sentence))
