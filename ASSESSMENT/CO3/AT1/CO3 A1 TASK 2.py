from collections import Counter

text = "the student is intelligent the student is hardworking the teacher is helpful"

w = text.lower().split()

uni = Counter(w)
bi = Counter(zip(w, w[1:]))
tri = Counter(zip(w, w[1:], w[2:]))

total = len(w)

def uni_p(x):
    return uni[x] / total

def bi_p(a, b):
    return bi[(a, b)] / uni[a] if uni[a] else 0

def tri_p(a, b, c):
    return tri[(a, b, c)] / bi[(a, b)] if bi[(a, b)] else 0

word = input("Enter previous two words: ").lower().split()
a, b = word[-2], word[-1]

print("\nPredictions:")

for c in uni:
    # Backoff
    p3 = tri_p(a, b, c)

    if p3 > 0:
        backoff = p3
    else:
        backoff = bi_p(b, c)

    if backoff == 0:
        backoff = uni_p(c)

    # Deleted Interpolation
    interp = (0.2 * uni_p(c) +
              0.3 * bi_p(b, c) +
              0.5 * tri_p(a, b, c))

    if backoff > 0:
        print(c,
              "Backoff:", round(backoff, 3),
              "Interpolation:", round(interp, 3))
