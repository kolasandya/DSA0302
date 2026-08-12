tags = ["economic/JJ", "growth/NN", "increases/NNS", "employment/NN"]

print("Before transformation:")
print(tags)

# Apply rule
tags[2] = "increases/VBZ"

print("\nAfter transformation:")
print(tags)
