words = {
    "analyzing": {"root": "analyze", "affix": "-ing", "type": "Inflectional"},
    "analysis": {"root": "analyze", "affix": "-sis", "type": "Derivational"},
    "analytical": {"root": "analyze", "affix": "-ical", "type": "Derivational"}
}

print("Original\tRoot\t\tAffix\tType\t\tNormalized")

for word, data in words.items():
    print(f"{word}\t{data['root']}\t{data['affix']}\t{data['type']}\t{data['root']}")
