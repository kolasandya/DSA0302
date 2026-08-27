def dialog_act(sentence):
    sentence = sentence.lower()

    if sentence.endswith("?"):
        return "Question"
    elif "thank" in sentence:
        return "Thanking"
    elif "hello" in sentence or "hi" in sentence:
        return "Greeting"
    elif "bye" in sentence:
        return "Goodbye"
    else:
        return "Statement"


dialog = [
    "Hello",
    "What is your name?",
    "Thank you",
    "I am a student",
    "Bye"
]

print("Dialog Act Recognition:")

for sentence in dialog:
    print(sentence, "->", dialog_act(sentence))