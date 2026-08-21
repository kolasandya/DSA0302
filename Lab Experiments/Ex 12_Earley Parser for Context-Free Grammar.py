import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'boy' | 'girl'
V -> 'likes'
""")

parser = EarleyChartParser(grammar)

sentence = "the boy likes the girl".split()

for tree in parser.parse(sentence):
    print(tree)