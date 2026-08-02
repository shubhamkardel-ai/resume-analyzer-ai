import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_file):
    """
    Extract text from an uploaded PDF.
    """

    document = fitz.open(pdf_file.name)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text.strip()