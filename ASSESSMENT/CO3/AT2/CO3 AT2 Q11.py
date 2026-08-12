words = {
    "economic": 120,
    "growth": 450,
    "increases": 210,
    "employment": 380
}

total = sum(words.values())

print("Total frequency =", total)
print("\nWord\t\tCount\tProbability\tPercentage")

for word, count in words.items():
    probability = count / total
    percentage = probability * 100

    print(
        word,
        "\t",
        count,
        "\t",
        round(probability, 4),
        "\t\t",
        round(percentage, 2), "%"
    )
