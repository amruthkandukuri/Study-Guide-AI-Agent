📚 Study Guide AI Agent — Project Overview

This repository contains a lightweight Generative AI project that ingests study material, stores semantic embeddings, and provides an interactive UI to generate:

📝 Study summaries

❓ Q&A practice questions

🧠 Flashcards

The application uses Streamlit, LangChain, ChromaDB, and Local LLMs (Ollama) to process study content and assist learners.

📁 Project layout
File	Responsibility
agent_tools.py	AI helper utilities — wraps LangChain calls to create summaries, QA pairs, and flashcards.
ingest.py	Data ingestion + embedding generator — chunks text, creates embeddings, and stores vectors in ChromaDB.
app.py	Streamlit application — uploads files, runs inference, and displays outputs.
requirements.txt	Python dependencies.

These roles are inferred from current functionality — update if module responsibilities evolve.

🔄 Flow of development

A typical workflow follows these stages:

1. Data ingestion

Modify ingest.py for text preprocessing rules, chunk logic, or embedding models

Re-run ingestion when new learning data is added

2. Agent tools / LLM logic

Enhance agent_tools.py with new AI utilities

Keep functions modular and documented

Maintain clear separation between retrieval logic and UI layer

3. Application UI

Extend app.py to expose new features in the Streamlit interface

Avoid embedding business logic in the UI — delegate to helper modules

4. Test & refine

Unit test summaries, QA, and flashcard generation

Optionally build integration tests for ingestion + inference workflow

⚡ Quick start (Windows PowerShell)

Create a virtual environment, install dependencies, and run the Streamlit app:

# (Recommended) create venv (Windows PowerShell)
python -m venv .venv
. .venv\Scripts\Activate.ps1

# install dependencies
pip install -r requirements.txt

# start the Streamlit app
streamlit run app.py

(Optional) Refresh embeddings
python .\ingest.py

Alternatively, you can run the project without creating a Python virtual environment. This runs the package installs into your active Python environment (system or other). Use this if you intentionally manage packages globally or with another environment manager.

```powershell
# install dependencies into the active Python environment
pip install -r requirements.txt

# start Streamlit app without a venv
streamlit run app.py

# refresh embeddings without a venv
python .\ingest.py
```

✅ Next steps / TODOs

Add tests/ directory and unit tests

Add .env support for model paths / env variables

Optionally introduce:

Makefile / scripts/ folder for easy commands

Docker build (for reproducible deployments)

Export features (to PDF / flashcard app format)

Support PDFs / Web pages as input