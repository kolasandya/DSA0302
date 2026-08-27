from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

prompt = "Write a short paragraph about Artificial Intelligence."

response = client.responses.create(
    model="gpt-4o-mini",
    input=prompt
)

print("Generated Text:")
print(response.output_text)