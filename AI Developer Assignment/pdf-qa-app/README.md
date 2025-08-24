
# PDF Q&A AI System

This project is a free, open-source AI-powered system that reads and understands PDF documents, and answers user queries based on their content. All processing is local and free—no paid APIs or billing.

## Tech Stack
- Python 3
- FastAPI (backend API)
- Streamlit (optional frontend)
- sentence-transformers (embeddings)
- PyMuPDF (PDF parsing)
- FAISS (vector database)

## Features
- Upload one or more PDF files
- Extract and chunk text by paragraph and page
- Generate embeddings for each chunk (locally, free)
- Store embeddings and metadata in FAISS (local, persistent)
- Ask natural language questions about uploaded PDFs
- Retrieve and display answers with source PDF and page number
- Simple web UI (Streamlit) or API endpoints

## How to Run
1. (Recommended) Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```
4. (Optional) Start Streamlit UI:
   ```bash
   # Make sure you are in the project root (pdf-qa-app)
   cd /Users/divyanshgoel/Documents/College/T&P assignment/AI Developer Assignment/pdf-qa-app
   streamlit run app/streamlit_ui.py
   ```
   If you see a "File does not exist" error, check your working directory and use the full relative path as above.


## How it Works
1. Upload PDFs via API or Streamlit UI
2. Text is extracted and split into chunks by paragraph and page
3. Chunks are embedded using sentence-transformers
4. Embeddings and metadata are stored in FAISS for fast search
5. When you ask a question, the system finds the most relevant chunks and returns them as context
6. The answer is generated using a simple template (not a full LLM)

## Sample PDF
Place your sample PDFs in the `data/` folder.

## Known Issues & Limitations
- Only local, free models are used (no OpenAI or paid APIs)
- Large PDFs may take time to process
- Answers may be basic: The system retrieves relevant text chunks and returns them using a simple template. It does not use a full language model for answer generation, so answers may lack deep reasoning or summarization.
- Context window for answers is limited by local model size
- PDF extraction quality depends on the source file (scanned/image-based PDFs may not work well)

## Troubleshooting & Improvements
- If answers are not appropriate, consider:
  - Ensuring PDFs are text-based and well-formatted
  - Tuning retrieval parameters in `vector_db.py`
  - Integrating a local LLM (e.g., llama.cpp, Mistral) for better answer generation

## Next Steps (Optional Enhancements)
- Swap the simple answer with a local LLM for better synthesis
- Add citation highlighting and page previews
- Containerize with Docker and add CI tests
