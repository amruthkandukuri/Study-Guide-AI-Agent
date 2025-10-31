from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
import chromadb
import numpy as np
import os


def ingest_data(file_path):
    """Read a file, split text, embed chunks, and store them in ChromaDB."""
    with open(file_path, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    # Split text into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_text(raw_text)

    # Generate embeddings
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = embedder.encode(chunks)

    # Convert ndarray -> list for Chroma
    embeddings = [emb.tolist() if isinstance(emb, np.ndarray) else emb for emb in embeddings]

    # Initialize ChromaDB
    client = chromadb.PersistentClient(path="chroma_db")

    try:
        collection = client.get_collection(name="study_materials")
    except:
        collection = client.create_collection(name="study_materials")

    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            metadatas=[{"id": i}],
            ids=[str(i)],
            embeddings=[embeddings[i]]
        )

    print(f"Ingested {len(chunks)} chunks into ChromaDB.")
    return collection
