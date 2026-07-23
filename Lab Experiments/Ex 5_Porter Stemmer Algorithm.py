from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "played", "running", "studies", "happiness"]

print("Stemmed Words:")
for word in words:
    print(word, "->", ps.stem(word))