import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N | Det Adj N
VP -> V NP
Det -> 'the' | 'a'
Adj -> 'big'
N -> 'dog' | 'cat'
V -> 'sees'
""")

parser = ChartParser(grammar)

sentence = "the big dog sees a cat".split()

for tree in parser.parse(sentence):
    print(tree)
    print("\nNoun Phrases:")
    for subtree in tree.subtrees():
        if subtree.label() == "NP":
            print(" ".join(subtree.leaves()))