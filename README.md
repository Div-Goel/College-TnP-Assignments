# College TnP Assignments

This repository contains two projects:

- **AI Developer Assignment**: PDF Q&A AI System
- **Sustainability Dashboard**: Textile Sustainability Dashboard

---

## 1. PDF Q&A AI System (AI Developer Assignment)

A free, open-source AI-powered system that reads and understands PDF documents, answering user queries based on their content. All processing is local and free—no paid APIs or billing.

### Tech Stack

- Python 3
- FastAPI (backend API)
- Streamlit (optional frontend)
- sentence-transformers (embeddings)
- PyMuPDF (PDF parsing)
- FAISS (vector database)

### Features

- Upload one or more PDF files
- Extract and chunk text by paragraph and page
- Generate embeddings for each chunk (locally, free)
- Store embeddings and metadata in FAISS (local, persistent)
- Ask natural language questions about uploaded PDFs
- Retrieve and display answers with source PDF and page number
- Simple web UI (Streamlit) or API endpoints

### How to Run

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
   streamlit run app/streamlit_ui.py
   ```

### Screenshots

- ![Model answering Screenshot](AI%20Developer%20Assignment/Model%20answering%20Screenshot.png)
- ![Uploading File Screenshot](AI%20Developer%20Assignment/Uploading%20File%20Screenshot.png)
- ![Web UI Screenshot](AI%20Developer%20Assignment/Web%20UI%20Screenshot.png)

---

## 2. Sustainability Dashboard (Textile)

A React (Vite) + Tailwind frontend and a FastAPI backend with SQLite mock data.

### Prerequisites

- Python 3.10+
- Node.js 18+ and npm

### Run Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
Backend will run at http://127.0.0.1:8000

### Run Frontend

```bash
cd frontend
npm install
npm run dev
```
Frontend will run at http://localhost:5173

### Build Frontend (optional)

```bash
npm run build
npm run preview
```

### Features

- KPI tiles (Energy, Water, Waste, Emissions) + Overall score
- Filters (date range, department/unit basic support)
- Alerts panel
- Insights page per KPI: trend, hotspots, anomalies, cost impact, goal progress
- Export CSV/PDF
- Auto refresh + manual refresh button

> Authentication, action-tracker, custom rules, email summaries, etc., are omitted to keep the assignment focused and easy to run.

### Screenshots

- ![APIs Screenshot](Sustainability%20Dashboard/APIs%20Screenshot.png)
- ![Dashboard Screenshot](Sustainability%20Dashboard/Dashboard%20Screenshot.png)

---
