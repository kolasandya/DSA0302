import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'John'
VP -> V NP
V -> 'likes'
NP -> 'apples'
""")

parser = ChartParser(grammar)

sentence = "John likes apples".split()

for tree in parser.parse(sentence):
    print(tree)