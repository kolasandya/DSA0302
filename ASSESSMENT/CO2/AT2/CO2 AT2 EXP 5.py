words = {
    "create": {"suffix": "-", "category": "Base Form", "root": "create"},
    "creates": {"suffix": "-s", "category": "Third Person Singular", "root": "create"},
    "creating": {"suffix": "-ing", "category": "Present Participle", "root": "create"}
}

print("Word\t\tSuffix\tCategory\t\t\tRoot\tNormalized")

for word, data in words.items():
    print(f"{word}\t{data['suffix']}\t{data['category']}\t{data['root']}\t{data['root']}")
