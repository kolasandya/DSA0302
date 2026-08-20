from nltk import CFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> DET N
VP -> V NP
DET -> 'the'
N -> 'student' | 'book'
V -> 'reads'
""")

sentence = "the student reads".split()

parser = EarleyChartParser(grammar)

print("Input:", " ".join(sentence))
print("\nEarley Parser Result:")

trees = list(parser.parse(sentence))

if trees:
    trees[0].pretty_print()
else:
    print("Incomplete sentence detected")
