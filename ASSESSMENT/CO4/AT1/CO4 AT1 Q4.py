sentences = {
    "Doctor prescribed medicine to patient":
        {"Doctor": "Agent", "Medicine": "Instrument", "Patient": "Recipient"},

    "Patient reported severe headache":
        {"Patient": "Agent", "Headache": "Symptom"},

    "Nurse monitored patient":
        {"Nurse": "Agent", "Patient": "Object"},

    "Medicine reduced blood pressure":
        {"Medicine": "Instrument", "Blood Pressure": "Object"}
}

for sentence, roles in sentences.items():
    print("\nSentence:", sentence)

    for entity, role in roles.items():
        print(entity, "->", role)
