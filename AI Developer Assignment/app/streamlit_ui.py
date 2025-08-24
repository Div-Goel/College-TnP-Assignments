import streamlit as st
import requests

st.title("PDF Q&A AI System")

st.header("Upload PDFs")
uploaded_files = st.file_uploader("Choose PDF file(s)", type=["pdf"], accept_multiple_files=True)
if uploaded_files and st.button("Upload"):
    files = [("files", (uf.name, uf, "application/pdf")) for uf in uploaded_files]
    response = requests.post("http://localhost:8000/upload_pdf/", files=files)
    if response.ok:
        st.success(f"Uploaded {len(uploaded_files)} file(s). Total chunks: {response.json()['chunks']}")
    else:
        st.error("Upload failed.")

st.header("Ask a Question")
query = st.text_input("Enter your question:")
top_k = st.slider("Top K", 1, 10, 5)
if st.button("Submit Query") and query:
    response = requests.post("http://localhost:8000/query/", data={"query": query, "top_k": top_k})
    if response.ok:
        payload = response.json()
        st.subheader("Answer")
        st.write(payload["answer"])
        with st.expander("Sources"):
            for src in payload.get("sources", []):
                meta = src.get("metadata", {})
                st.markdown(f"- {meta.get('pdf', 'unknown.pdf')} (page {meta.get('page', '?')})\n\n> {src['text']}")
    else:
        st.error("Query failed.")
