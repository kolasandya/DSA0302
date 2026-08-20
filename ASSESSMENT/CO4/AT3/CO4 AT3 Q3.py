from nltk import CFG, PCFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> PRON | DET N | DET N PP
VP -> V NP | V NP PP
PP -> P NP
PRON -> 'She'
DET -> 'the' | 'a'
N -> 'man' | 'telescope'
V -> 'saw'
P -> 'with'
""")

sentence = "She saw the man with a telescope".split()

parser = EarleyChartParser(grammar)

trees = list(parser.parse(sentence))

print("Sentence:", " ".join(sentence))
print("\nNumber of possible CFG parses:", len(trees))

for i, tree in enumerate(trees, 1):
    print("\nParse", i)
    tree.pretty_print()
