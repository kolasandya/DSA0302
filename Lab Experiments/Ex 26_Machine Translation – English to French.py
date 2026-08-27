from transformers import pipeline

translator = pipeline(
    "translation_en_to_fr",
    model="Helsinki-NLP/opus-mt-en-fr"
)

text = "I love natural language processing."

result = translator(text)

print("English:", text)
print("French:", result[0]["translation_text"])