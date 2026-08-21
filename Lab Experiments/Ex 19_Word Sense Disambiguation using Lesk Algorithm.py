import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

nltk.download('wordnet')
nltk.download('punkt')

sentence = "I went to the bank to deposit money."

words = word_tokenize(sentence)

sense = lesk(words, "bank")

print("Sentence:", sentence)
print("Word: bank")

if sense:
    print("Selected Sense:", sense.name())
    print("Meaning:", sense.definition())
else:
    print("No sense found.")