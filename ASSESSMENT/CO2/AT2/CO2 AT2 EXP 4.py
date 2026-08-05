words = {
    "activate": {"prefix": "-", "root": "activate", "suffix": "-", "sequence": "Base"},
    "activation": {"prefix": "-", "root": "activate", "suffix": "-ion", "sequence": "activate + ion"},
    "reactivation": {"prefix": "re-", "root": "activate", "suffix": "-ion", "sequence": "re + activate + ion"}
}

print("Word\t\tPrefix\tRoot\t\tSuffix\tSequence\t\tNormalized")

for word, data in words.items():
    print(f"{word}\t{data['prefix']}\t{data['root']}\t{data['suffix']}\t{data['sequence']}\t{data['root']}")
