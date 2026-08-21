sentence = "He plays cricket"

words = sentence.split()

if words[0] == "He" and words[1].endswith("s"):
    print("Sentence is grammatically correct.")
else:
    print("Sentence is grammatically incorrect.")