import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> VP
VP -> V NP
NP -> Det N PP PP
NP -> Det Adj N
NP -> N
PP -> P NP
V -> 'Book'
Det -> 'a'
Adj -> 'window'
N -> 'flight' | 'Delhi' | 'seat'
P -> 'to' | 'with'
""")

sentence = "Book a flight to Delhi with a window seat".split()

parser = EarleyChartParser(grammar)

trees = list(parser.parse(sentence))

print("Number of Parse Trees:", len(trees))

if trees:
    print("\nParse Tree:\n")
    trees[0].pretty_print()
