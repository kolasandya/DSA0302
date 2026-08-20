import nltk
from nltk import CFG
from nltk.parse import ChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> PRON | DET N
VP -> V NP
PRON -> 'She'
DET -> 'the'
N -> 'book'
V -> 'read'
""")

sentence = "She read the book".split()

parser = ChartParser(grammar)

for tree in parser.parse(sentence):
    print("CFG Parse Tree:")
    tree.pretty_print()
    break

print("\nDependency Relations:")
print("read -> She   (subject)")
print("read -> book  (object)")
