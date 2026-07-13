"""
Streamlit UI for the RAG Document Question Answering System.
Run with: streamlit run app.py
"""

import os
import tempfile
import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_classic.chains import RetrievalQA
load_dotenv()
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
GROQ_MODEL = "llama-3.1-8b-instant"
st.set_page_config(page_title="RAG Document Q&A", page_icon="📄")
st.title("📄 Document Question Answering (RAG)")
st.caption("Upload a PDF, then ask questions grounded in its content.")
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
if uploaded_file and st.button("Process Document"):
    with st.spinner("Reading and indexing document..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name
        loader = PyPDFLoader(tmp_path)
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
        chunks = splitter.split_documents(documents)

        embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
        st.session_state.vectorstore = FAISS.from_documents(chunks, embeddings)

        os.remove(tmp_path)
    st.success(f"Document indexed into {len(chunks)} chunks. Ask away!")

question = st.text_input("Ask a question about the document")

if question and st.session_state.vectorstore:
    with st.spinner("Retrieving context and generating answer..."):
        retriever = st.session_state.vectorstore.as_retriever(search_kwargs={"k": 4})

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

    st.subheader("Answer")
    st.write(result["result"])

    with st.expander("Sources (retrieved chunks)"):
        for i, doc in enumerate(result["source_documents"], 1):
            page = doc.metadata.get("page", "?")
            st.markdown(f"**[{i}] page {page}**")
            st.write(doc.page_content[:400] + "...")
elif question and not st.session_state.vectorstore:
    st.warning("Upload and process a PDF first.")