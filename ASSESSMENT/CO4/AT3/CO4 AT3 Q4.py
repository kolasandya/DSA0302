# Feature structure
subject = {
    "word": "She",
    "number": "singular",
    "person": "third"
}

verb = {
    "word": "runs",
    "number": "singular",
    "person": "third"
}

# Subcategorization frame
frames = {
    "eat": "Verb + Object",
    "give": "Verb + Object + Recipient",
    "sleep": "Verb"
}

print("Feature Structure:")
print("Subject:", subject)
print("Verb:", verb)

if subject["number"] == verb["number"] and \
   subject["person"] == verb["person"]:
    print("Agreement: Correct")

print("\nSubcategorization Frames:")
for verb, frame in frames.items():
    print(verb, "->", frame)
