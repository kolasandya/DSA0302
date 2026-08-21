source = "The boy is playing football."

# Step 1: Source analysis
print("Source:", source)

# Step 2: Interlingua
interlingua = {
    "person": "boy",
    "action": "play",
    "object": "football",
    "tense": "present_progressive"
}
print("Interlingua:", interlingua)

# Step 3: Candidate translations
candidates = [
    ("The boy is playing football.", 0.92),
    ("The boy plays football.", 0.70)
]

# Step 4: Statistical scoring
best = max(candidates, key=lambda x: x[1])

print("\nCandidates:")
for sentence, score in candidates:
    print(sentence, "Score:", score)

# Step 5: Final translation
print("\nFinal Translation:", best[0])
