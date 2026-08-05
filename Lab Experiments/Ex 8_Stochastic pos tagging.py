import nltk
from nltk import word_tokenize, pos_tag

# Download required resources (run only once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Input sentence
text = "The cat is sleeping on the mat."

# Tokenize the sentence
words = word_tokenize(text)

# Perform POS tagging
tags = pos_tag(words)

# Display the output
print("Stochastic POS Tagging:")
for word, tag in tags:
    print(f"{word} --> {tag}")