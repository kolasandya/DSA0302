words = {
    "govern": {"root": "govern", "affix": "-", "level": "Base"},
    "government": {"root": "govern", "affix": "-ment", "level": "Level 1"},
    "governance": {"root": "govern", "affix": "-ance", "level": "Level 1"}
}

print("Word\t\tRoot\tAffix\tLevel\tNormalized")

for word, data in words.items():
    print(f"{word}\t{data['root']}\t{data['affix']}\t{data['level']}\t{data['root']}")
