# template.py
import os

# Define the folder structure
folders = [
    "rag-architect-app/data/raw/articles",
    "rag-architect-app/data/raw/zoning_pdfs",
    "rag-architect-app/data/raw/norms",
    "rag-architect-app/data/raw/qna_forum_text",
    "rag-architect-app/data/raw/design_guides",
    "rag-architect-app/data/raw/blueprints",
    
    "rag-architect-app/data/processed/clean_text",
    "rag-architect-app/data/processed/ocr_text",
    "rag-architect-app/scripts/scraper_articles.py",
    "rag-architect-app/scripts/scraper_zoning_laws.py",
    "rag-architect-app/scripts/ocr_converter.py",
    "rag-architect-app/scripts/ preprocess.py",
    "rag-architect-app/embeddings",
    "rag-architect-app/notebooks",
    "rag-architect-app/vector_db"
]

# Define the files to create
files = {
    "rag-architect-app/scripts/scraper.py": "# scraper.py\n# Script to scrape architectural data\n\n",
    "rag-architect-app/scripts/preprocess.py": "# preprocess.py\n# Script to clean and chunk text\n\n",
    "rag-architect-app/README.md": "# RAG Architect App\n\nProject for architectural domain-focused Retrieval-Augmented Generation (RAG) system.\n"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files with placeholder content
for path, content in files.items():
    with open(path, "w") as f:
        f.write(content)

print("Project structure created successfully.")
