# 🏘️ Real Estate Architect Assistant (RAG-Powered App)

This project is a **Retrieval-Augmented Generation (RAG)** application designed to assist users in understanding real estate, architecture regulations, construction norms, and design principles. It combines **ChromaDB**, **sentence-transformers**, and **Groq's Mistral API**, and is deployed using **Streamlit**.

---

## 🔧 Tech Stack

| Layer        | Technology                          |
|--------------|--------------------------------------|
| Embedding    | `sentence-transformers (MiniLM)`     |
| Vector Store | `ChromaDB` (local, persistent)       |
| LLM          | `Groq` using `llama-3.1-8b-instant`  |
| UI           | `Streamlit`                          |
| Extras       | `streamlit-extras` (UI enhancements) |

---

## 🧠 Architecture Overview

```mermaid
graph TD
    A[User Question] --> B[Embed with MiniLM]
    B --> C[ChromaDB Search]
    C --> D[Relevant Context Docs]
    D --> E[LLM via Groq API (Mistral)]
    E --> F[Final Answer]
    F --> G[Streamlit UI]




rag-architect-app/
│
├── data/
│   ├── raw/                   # Raw PDFs, TXT, CSVs
│   └── processed/
│       ├── clean_text/        # Chunked architecture docs
│       └── property_chunks/   # Top 100 property listings
│
├── vector_db/
│   └── chroma_store/          # ChromaDB persistent store
│   └── store_to_chroma.py     # Embeds + stores chunks
│
├── scripts/
│   ├── ScrapData /   # Chunk property CSV to text
│   └── preprocess.py   
|   └── preprocess.py      # Chunk PDFs and TXT files
│
├── front_end/
│   └── app.py                 # Streamlit app
│
├── requirements.txt
└── README.md



# Setup Instruction
git clone https://github.com/your-username/rag-architect-app.git
cd rag-architect-app
  
  ## Create virtual env and activate
  python -m venv v
  v\Scripts\activate  

 ## Install Requirements
 pip install -r requirements.txt

 ##Set up .env
 GROQ_API_KEY=your_groq_api_key

## Preprocess Data
python scripts/preprocess_docs.py
python scripts/convert_to_chunks.py

##Embed & Store to ChromaDB
python vector_db/store_to_chroma.py

## Run Stramlit 
streamlit run front_end/app.py


