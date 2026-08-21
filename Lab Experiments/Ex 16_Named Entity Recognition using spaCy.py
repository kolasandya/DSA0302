import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "Apple was founded by Steve Jobs in California."

# Process the text
doc = nlp(text)

# Display named entities
print("Named Entities:")

for ent in doc.ents:
    print(ent.text, "->", ent.label_)