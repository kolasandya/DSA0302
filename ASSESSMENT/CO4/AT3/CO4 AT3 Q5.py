sentence = ["She", "reads", "the", "book"]

# Transition-based parsing
transitions = [
    "SHIFT She",
    "SHIFT reads",
    "LEFT-ARC subject",
    "SHIFT the",
    "SHIFT book",
    "RIGHT-ARC object"
]

print("Transition-Based Parsing:")
for t in transitions:
    print(t)

# Graph-based parsing
dependencies = [
    ("reads", "She", "subject"),
    ("reads", "book", "object")
]

print("\nGraph-Based Parsing:")
for head, dependent, relation in dependencies:
    print(head, "->", dependent, "(", relation, ")")
