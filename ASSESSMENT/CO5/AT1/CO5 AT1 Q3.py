sentence = "The bank by the river flooded after the storm."

if "river" in sentence and "flooded" in sentence:
    meaning = "riverbank"
else:
    meaning = "financial bank"

print("Word: bank")
print("Meaning:", meaning)

print("\nPredicate Logic:")
print("riverbank(bank)")
print("location(bank, river)")
print("flooded(bank)")
print("storm(storm1)")
print("saved(bank, quick_action)")

print("\nRST:")
print("CONTRAST")
print(" |-- Bank flooded")
print(" |-- Quick action saved it")
