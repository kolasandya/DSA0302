lambda1 = 0.5
lambda2 = 0.3
lambda3 = 0.2

trigram = 1 / 3
bigram = 2 / 3
unigram = 2 / 15

probability = (
    lambda1 * trigram +
    lambda2 * bigram +
    lambda3 * unigram
)

print("Trigram probability =", round(trigram, 4))
print("Bigram probability =", round(bigram, 4))
print("Unigram probability =", round(unigram, 4))
print("Interpolated probability =", round(probability, 4))
print("Percentage =", round(probability * 100, 2), "%")
