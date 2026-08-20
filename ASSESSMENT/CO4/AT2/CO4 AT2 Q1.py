import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> VP
VP -> V NP
NP -> Pronoun Det N PP PP
NP -> Det N
PP -> P NP
V -> 'Show'
Pronoun -> 'me'
Det -> 'the'
N -> 'transactions' | 'card' | 'month'
P -> 'with' | 'from'
""")

sentence = "Show me the transactions with the card from the month".split()

parser = EarleyChartParser(grammar)

trees = list(parser.parse(sentence))

print("Number of Parse Trees:", len(trees))

if trees:
    print("\nParse Tree:\n")
    trees[0].pretty_print()
