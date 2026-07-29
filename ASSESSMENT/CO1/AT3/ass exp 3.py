import re

text = """
Meeting on 12/09/2026
Call 9876543210
#NLP
#Python
@OpenAI
@ChatGPT
natural language processing
machine learning
"""

print("Given Text:")
print(text)

# Search Patterns
date = re.findall(r"\d{2}/\d{2}/\d{4}", text)
phone = re.findall(r"[6-9]\d{9}", text)
hashtags = re.findall(r"#\w+", text)
mentions = re.findall(r"@\w+", text)

# Prefix Search (Prefix = nat)
words = re.findall(r"\b\w+\b", text)
prefix = [word for word in words if word.startswith("nat")]

# Suffix Search (Suffix = ing)
suffix = [word for word in words if word.endswith("ing")]

# Display Results
print("\n----- SEARCH RESULTS -----")
print("Date:", date)
print("Phone Number:", phone)
print("Hashtags:", hashtags)
print("Mentions:", mentions)
print("Prefix (nat):", prefix)
print("Suffix (ing):", suffix)
