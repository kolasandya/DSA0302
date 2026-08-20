import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N REL
REL -> Rel V NP TIME
VP -> V ACTION CONJ ACTION
ACTION -> V NP
NP -> Det N
NP -> N
TIME -> Adv N
PP -> P N
V -> 'reviewed' | 'recommends' | 'starting' | 'scheduling'
Rel -> 'who'
Det -> 'The' | 'the' | 'a'
N -> 'doctor' | 'patient' | 'medication' | 'visit' | 'week' | 'Chennai'
Adv -> 'last'
CONJ -> 'and'
""")

sentence = "The doctor who reviewed the patient last week recommends starting medication and scheduling a visit".split()

parser = EarleyChartParser(grammar)

trees = list(parser.parse(sentence))

print("Number of Parse Trees:", len(trees))

if trees:
    print("\nParse Tree:\n")
    trees[0].pretty_print()
