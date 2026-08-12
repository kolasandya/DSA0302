import math

# Before transformation
before = {
    "NNS": 0.5,
    "VBZ": 0.3,
    "NN": 0.2
}

# After transformation
after = {
    "VBZ": 1.0
}

def entropy(probabilities):
    h = 0
    for p in probabilities:
        if p > 0:
            h -= p * math.log2(p)
    return h

before_entropy = entropy(before.values())
after_entropy = entropy(after.values())

print("Before transformation:")
print("Entropy =", round(before_entropy, 3), "bits")

print("\nAfter transformation:")
print("Entropy =", round(after_entropy, 3), "bits")

print("\nFinal tag: increases/VBZ")
