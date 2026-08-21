from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Natural language processing is a branch of artificial intelligence.",
    "Machine learning is used in artificial intelligence.",
    "Natural language processing deals with text and language."
]

query = ["natural language processing"]

vectorizer = TfidfVectorizer()

# Convert documents and query into TF-IDF vectors
doc_vectors = vectorizer.fit_transform(documents)
query_vector = vectorizer.transform(query)

# Calculate similarity
similarity = cosine_similarity(query_vector, doc_vectors)[0]

print("Document Ranking:")

for i, score in enumerate(similarity):
    print("Document", i + 1, ":", round(score, 3))

# Find most relevant document
best_doc = similarity.argmax() + 1

print("\nMost Relevant Document:", best_doc)