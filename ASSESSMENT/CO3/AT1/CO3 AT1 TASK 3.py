from collections import Counter
import math

train = "the student studies computer the student likes computer"
test = "the student studies computer"

w = train.split()

uni = Counter(w)
bi = Counter(zip(w, w[1:]))
tri = Counter(zip(w, w[1:], w[2:]))

def entropy(n):

    total = 0
    count = 0

    for i, word in enumerate(test.split()):

        if n == 1:
            p = uni[word] / len(w)

        elif n == 2:
            if i == 0:
                continue
            p = bi[(test.split()[i-1], word)] / uni[test.split()[i-1]]

        else:
            if i < 2:
                continue
            a = test.split()[i-2]
            b = test.split()[i-1]
            p = tri[(a, b, word)] / bi[(a, b)] if bi[(a,b)] else 0

        if p == 0:
            return float("inf")

        total += -math.log2(p)
        count += 1

    return total / count


for n in [1, 2, 3]:
    print("N =", n, "Entropy =", entropy(n))
