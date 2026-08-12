import math

p1 = 0.66
p2 = 0.33

entropy = -(p1 * math.log2(p1) + p2 * math.log2(p2))

print("Entropy =", round(entropy, 3), "bits")
