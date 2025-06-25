import fitz  # PyMuPDF

def extract_text_from_pdf(path, max_pages=None):
    """
    Extracts text from a PDF file.

    Args:
        path (str): Path to the PDF file.
        max_pages (int, optional): Max number of pages to extract (for large PDFs).

    Returns:
        str: Extracted text.
    """
    text = ""
    try:
        with fitz.open(path) as doc:
            for i, page in enumerate(doc):
                if max_pages and i >= max_pages:
                    break
                text += page.get_text()
    except Exception as e:
        print(f"[ERROR] Failed to extract from {path}: {e}")
    return text.strip()
