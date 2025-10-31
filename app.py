import streamlit as st
import os
from ingest import ingest_data
from agent_tools import summarize_text, create_qa_pairs, create_flashcards
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings


st.title("🎓 Generative AI Study Guide Agent")

uploaded_file = st.file_uploader("Upload educational text file (TXT/CSV)")
output_option = st.selectbox("Choose an output type:", ["Summary", "Q&A", "Flashcards"])

if st.button("Generate Study Guide"):
    if uploaded_file:
        os.makedirs("data", exist_ok=True)

        try:
            file_bytes = uploaded_file.read().decode('utf-8')
        except UnicodeDecodeError:
            st.error("File encoding must be UTF-8.")
            st.stop()

        # Save file for ingestion
        with open("data/temp.txt", "w", encoding="utf-8") as f:
            f.write(file_bytes)

        # Ingest into ChromaDB
        collection = ingest_data("data/temp.txt")

        # ✅ Define the same embedding function used in ingest.py
        embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

        # ✅ Attach the embedding function when creating the retriever
        retriever = Chroma(
            persist_directory="chroma_db",
            collection_name="study_materials",
            embedding_function=embedding_function
        ).as_retriever()

        # Generate output
        if output_option == "Summary":
            output = summarize_text(retriever, file_bytes)
        elif output_option == "Q&A":
            output = create_qa_pairs(retriever, file_bytes)
        else:
            output = create_flashcards(retriever, file_bytes)

        st.subheader("🧠 Generated Output:")
        st.write(output)

    else:
        st.error("Please upload a file first.")
