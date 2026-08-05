words = {
    "disagree": {"prefix": "dis-", "root": "agree", "suffix": "-", "type": "Derivational", "meaning": "Opposite"},
    "agreement": {"prefix": "-", "root": "agree", "suffix": "-ment", "type": "Derivational", "meaning": "State"},
    "agreeable": {"prefix": "-", "root": "agree", "suffix": "-able", "type": "Derivational", "meaning": "Capable"}
}

print("Word\t\tPrefix\tRoot\tSuffix\tType\t\tMeaning\t\tNormalized")

for word, data in words.items():
    print(f"{word}\t{data['prefix']}\t{data['root']}\t{data['suffix']}\t{data['type']}\t{data['meaning']}\t{data['root']}")
