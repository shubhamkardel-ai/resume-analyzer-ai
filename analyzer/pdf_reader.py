import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_file):
    """
    Extract text from an uploaded PDF file.
    """

    text = ""

    try:
        document = fitz.open(pdf_file.name)

        for page in document:
            text += page.get_text()

        document.close()

    except Exception as e:
        return f"Error: {str(e)}"

    return text