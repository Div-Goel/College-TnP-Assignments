import fitz  # PyMuPDF
from typing import List, Tuple, Dict

def _split_paragraphs(text: str) -> List[str]:
    paras = [p.strip() for p in text.split('\n\n') if p.strip()]
    return paras

def _chunk_with_max_len(paragraphs: List[str], max_chars: int = 1200) -> List[str]:
    chunks: List[str] = []
    buf: List[str] = []
    cur_len = 0
    for p in paragraphs:
        if cur_len + len(p) + 1 > max_chars and buf:
            chunks.append('\n'.join(buf))
            buf = []
            cur_len = 0
        buf.append(p)
        cur_len += len(p) + 1
    if buf:
        chunks.append('\n'.join(buf))
    return chunks

def extract_text_chunks(pdf_path: str) -> List[Tuple[str, Dict]]:
    doc = fitz.open(pdf_path)
    results: List[Tuple[str, Dict]] = []
    for page_idx, page in enumerate(doc, start=1):
        text = page.get_text("text")
        if not text:
            continue
        paragraphs = _split_paragraphs(text)
        page_chunks = _chunk_with_max_len(paragraphs)
        for chunk in page_chunks:
            results.append((chunk, {"page": page_idx}))
    return results
