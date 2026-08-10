from collections import Counter
import re

text = """
the student is intelligent
the student is hardworking
the student studies computer
the teacher is helpful
the teacher teaches computer
"""

words = re.findall(r'\w+', text.lower())

uni = Counter(words)
bi = Counter(zip(words, words[1:]))
tri = Counter(zip(words, words[1:], words[2:]))

print("Unigram:", uni)
print("Bigram:", bi)
print("Trigram:", tri)

n = int(input("Enter N (1/2/3): "))
sentence = input("Enter sentence: ").lower().split()

if n == 1:
    total = sum(uni.values())
    result = [(w, c/total) for w, c in uni.items()]

elif n == 2:
    last = sentence[-1]
    result = [(b, c/uni[last])
              for (a, b), c in bi.items() if a == last]

else:
    a, b = sentence[-2], sentence[-1]
    result = [(c, count/bi[(a, b)])
              for (x, y, c), count in tri.items()
              if x == a and y == b]

result.sort(key=lambda x: x[1], reverse=True)

print("\nTop 5 Predictions:")
for word, p in result[:5]:
    print(word, round(p, 3))

print("\nUnseen Bigram Probability:",
      bi[("student", "plays")])
