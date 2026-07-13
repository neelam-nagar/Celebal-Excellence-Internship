# Document Question Answering System (RAG)

A simple Retrieval-Augmented Generation system that answers questions from a custom PDF document.

## How it works
1. **Ingestion** — PDF is loaded and split into overlapping text chunks.
2. **Embedding** — Each chunk is converted to a vector using a free local embedding model (`all-MiniLM-L6-v2`, no API key needed).
3. **Vector store** — Chunks are stored in a FAISS index for fast similarity search.
4. **Retrieval** — On a question, the top-k most similar chunks are fetched.
5. **Generation** — Groq's `llama-3.1-8b-instant` model generates an answer using only the retrieved chunks as context.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Add your free Groq API key (console.groq.com/keys) to .env
```

## Usage — CLI

```bash
python rag.py ingest data/your_document.pdf
python rag.py ask "What is the main idea of the document?"
```

## Usage — Web UI

```bash
streamlit run app.py
```

Upload a PDF in the browser, then ask questions directly.

## Project structure

```
rag_project/
├── rag.py              # CLI pipeline (ingest + ask)
├── app.py              # Streamlit UI
├── requirements.txt
├── .env.example
└── data/               # put your PDFs here
```

## Possible improvements (mentioned in assignment)

- Hybrid search (keyword + vector) instead of pure vector similarity
- Re-ranking retrieved chunks before generation
- Support for multiple documents / multi-file ingestion
- Try other embedding models or LLMs
