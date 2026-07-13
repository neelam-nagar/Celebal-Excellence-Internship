"""
Document Question Answering System (RAG)
------------------------------------------
Pipeline: PDF -> chunks -> embeddings -> FAISS vector store -> retrieve -> Groq LLM answer

Usage:
    python rag.py ingest data/your_file.pdf
    python rag.py ask "What is the main idea of the document?"
"""

import os
import sys
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA

load_dotenv()
VECTOR_STORE_PATH = "faiss_index"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
GROQ_MODEL = "llama-3.1-8b-instant"


def ingest(pdf_path: str):
    """Load a PDF, chunk it, embed it, and save a FAISS index."""
    print(f"Loading document: {pdf_path}")
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    print("Splitting into chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
    )
    chunks = splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks")

    print("Creating embeddings (this runs locally, no API needed)...")
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    print("Building FAISS vector store...")
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(VECTOR_STORE_PATH)
    print(f"Vector store saved to '{VECTOR_STORE_PATH}/'. Ingestion complete.")

def ask(question: str):
    """Load the FAISS index and answer a question using retrieved context."""
    if not os.path.exists(VECTOR_STORE_PATH):
        print("No vector store found. Run 'python rag.py ingest <pdf_path>' first.")
        return

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    vectorstore = FAISS.load_local(
        VECTOR_STORE_PATH, embeddings, allow_dangerous_deserialization=True
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    llm = ChatGroq(
        model=GROQ_MODEL,
        api_key=os.environ.get("GROQ_API_KEY"),
        temperature=0.2,
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type="stuff",
    )

    result = qa_chain.invoke({"query": question})

    print("\n--- Answer ---")
    print(result["result"])

    print("\n--- Sources (retrieved chunks) ---")
    for i, doc in enumerate(result["source_documents"], 1):
        page = doc.metadata.get("page", "?")
        preview = doc.page_content[:150].replace("\n", " ")
        print(f"[{i}] page {page}: {preview}...")
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:\n  python rag.py ingest <pdf_path>\n  python rag.py ask \"<question>\"")
        sys.exit(1)
    command = sys.argv[1]
    arg = sys.argv[2]
    if command == "ingest":
        ingest(arg)
    elif command == "ask":
        ask(arg)
    else:
        print("Unknown command. Use 'ingest' or 'ask'.")