import re

text = """Natural language processing is a field of artificial intelligence.
Natural language processing deals with text and language.
Text processing is useful in many applications."""

sentences = text.split(".")

sentences = [s.strip() for s in sentences if s.strip()]

scores = []

for i in range(len(sentences) - 1):
    words1 = set(re.findall(r'\w+', sentences[i].lower()))
    words2 = set(re.findall(r'\w+', sentences[i + 1].lower()))

    common = words1.intersection(words2)

    score = len(common)
    scores.append(score)

print("Coherence Scores:")
for i, score in enumerate(scores):
    print("Sentence", i + 1, "-> Sentence", i + 2, ":", score)

average = sum(scores) / len(scores)

print("\nAverage Coherence Score:", round(average, 2))