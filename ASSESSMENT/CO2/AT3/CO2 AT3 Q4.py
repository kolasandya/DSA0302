words = ["watches", "watching", "washable", "washer", "washed"]

def analyze(word):
    if word == "watches":
        return "watch + es", "Inflectional"
    elif word == "watching":
        return "watch + ing", "Inflectional"
    elif word == "washable":
        return "wash + able", "Derivational"
    elif word == "washer":
        return "wash + er", "Derivational"
    elif word == "washed":
        return "wash + ed", "Inflectional"
    else:
        return word, "Unknown"
print("Word\t\tAnalysis\t\tType")
print("-----------------------------------------------")

for word in words:
    analysis, morph_type = analyze(word)
    print(word, "\t", analysis, "\t", morph_type)
