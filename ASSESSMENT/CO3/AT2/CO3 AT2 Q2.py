trigram = 0
bigram = 0
unigram = 0

print("P(improves | data, science) =", trigram)
print("Backoff to P(improves | science) =", bigram)
print("Backoff to P(improves) =", unigram)

print("Final Probability =", unigram)
