import os
import streamlit as st
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
from groq import Groq
from dotenv import load_dotenv

# Load API keys
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Load models and Chroma
embedder = SentenceTransformer("all-MiniLM-L6-v2")
chroma_client = chromadb.PersistentClient(path="vector_db/chroma_store")
collection = chroma_client.get_collection("architect_knowledge")
groq_client = Groq(api_key=GROQ_API_KEY)

# Page Config
st.set_page_config(page_title="RAG Architect Assistant", page_icon="🏛️")
st.title("🏛️ Real Estate Architect Assistant")
st.caption("Take Suggestion before Buying Valuable asset of you life")

# Memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User Input
user_input = st.chat_input("Ask a question about real estate, design, rules, etc.")
if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    # Embed and search
    query_vec = embedder.encode(user_input).tolist()
    results = collection.query(query_embeddings=[query_vec], n_results=3)
    chunks = results["documents"][0]
    context = "\n\n".join(chunks)

    # Prepare messages with memory
    messages = [
        {
            "role": "system",
            "content": "You are an expert real estate architecture assistant. Answer clearly using provided context only."
        }
    ]
    for turn in st.session_state.chat_history[-5:]:
        messages.append({"role": "user", "content": turn["user"]})
        messages.append({"role": "assistant", "content": turn["bot"]})

    prompt = f"""Context:
{context}

Question: {user_input}"""
    messages.append({"role": "user", "content": prompt})

    # Call Groq
    with st.chat_message("assistant"):
        response_container = st.empty()
        full_response = ""
        response = groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            stream=True
        )

        for chunk in response:
            delta = chunk.choices[0].delta.content
            if delta:
                full_response += delta
                response_container.markdown(full_response + "▌")

        response_container.markdown(full_response)

    # Update memory
    st.session_state.chat_history.append({
        "user": user_input,
        "bot": full_response
    })

    # Show retrieved sources
    with st.expander("📄 Retrieved Chunks (Context)"):
        for doc, meta in zip(results["documents"][0], results["metadatas"][0]):
            st.markdown(f"**{meta['filename']}**\n\n{doc[:500]}...")

