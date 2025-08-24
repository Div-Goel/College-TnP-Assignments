from typing import List, Dict, Tuple

SYSTEM_INSTRUCTIONS = (
    "Answer the question strictly using the provided context. If the answer is not in the context, say 'I don't know based on the uploaded documents.'"
)

def format_context(results: List[Dict]) -> str:
    lines = []
    for r in results:
        meta = r.get("metadata", {})
        pdf = meta.get("pdf", "unknown.pdf")
        page = meta.get("page", "?")
        lines.append(f"[source: {pdf}, page {page}]\n{r['text']}")
    return "\n\n---\n\n".join(lines)

def answer_query(query: str, results: List[Dict]) -> Tuple[str, str]:
    context = format_context(results)
    if not context:
        return ("I don't know based on the uploaded documents.", "")
    # Simple rule-based answer (placeholder for a local LLM): return the most relevant snippet
    top = results[0]
    answer = top["text"]
    return answer, context
