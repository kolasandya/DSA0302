dialogue = [
    ("User", "Can you book a train ticket for me?", "Request"),
    ("Agent", "Sure, where would you like to travel?", "Question"),
    ("User", "I want to go to Chennai.", "Inform"),
    ("Agent", "Your ticket has been booked.", "Confirmation")
]

print("Dialogue Act Sequence:")
for speaker, text, act in dialogue:
    print(speaker, "->", act)

print("\nSequence:")
print("Request -> Question -> Inform -> Confirmation")
