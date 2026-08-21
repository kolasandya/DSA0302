import nltk
from nltk.corpus import wordnet

# Download WordNet
nltk.download('wordnet')

word = "computer"

# Get synsets
synsets = wordnet.synsets(word)

print("Word:", word)
print("\nSynsets and Meanings:")

for syn in synsets[:5]:
    print(syn.name(), "->", syn.definition())