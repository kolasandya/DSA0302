queries = {
    "Q1": ("Activate", "Roaming"),
    "Q2": ("Deactivate", "CallerTune"),
    "Q3": ("Query", "DataBalance"),
    "Q4": ("Activate", "5GService")
}

for q, (action, obj) in queries.items():
    print(q, ":", action, "(", obj, ", Customer )")

# Check prediction
actual = "Deactivate"
predicted = "Activate"

if actual != predicted:
    print("Q2: Incorrect semantic interpretation")
else:
    print("Correct")
