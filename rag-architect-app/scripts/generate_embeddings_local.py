import os
import json
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# Config
INDEX_NAME = "architect-knowledge"
EMBEDDING_DIM = 384
EMBEDDING_FILE = "data/embeddings/embeddings_local.json"

# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

# Check if index exists
if INDEX_NAME not in pc.list_indexes().names():
    pc.indexes().create(
        name=INDEX_NAME,
        dimension=EMBEDDING_DIM,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",       # Or "gcp" if your dashboard shows that
            region="us-west-2" # Or your chosen region
        )
    )

# Connect to the index
index = pc.Index(INDEX_NAME)

# Load embeddings
with open(EMBEDDING_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# Upload in batches
batch = []
for i, item in enumerate(data):
    vector_id = f"chunk-{i}"
    vector = item["embedding"]
    metadata = {
        "filename": item["filename"],
        "text": item["text"][:300]
    }

    batch.append({
        "id": vector_id,
        "values": vector,
        "metadata": metadata
    })

    if len(batch) == 100 or i == len(data) - 1:
        index.upsert(vectors=batch)
        print(f"✅ Uploaded {len(batch)} vectors")
        batch = []

print("\n🎉 Done! All vectors uploaded to Pinecone.")
