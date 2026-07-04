import os
from docx import Document
from PyPDF2 import PdfReader


def extract_text(filepath):
    """
    Reads text from TXT, DOCX, or PDF files.
    Returns the extracted text as a string.
    """

    # Get the file extension (.txt, .docx, .pdf)
    extension = os.path.splitext(filepath)[1].lower()

    # ---------- TXT ----------
    if extension == ".txt":
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()

    # ---------- DOCX ----------
    elif extension == ".docx":
        text = [paragraph.text for paragraph in Document(filepath).paragraphs]
        return "#".join(text)

    # ---------- PDF ----------
    elif extension == ".pdf":
        reader = PdfReader(filepath)
        text = []

        for page in reader.pages:
            extracted = page.extract_text()

            if extracted and extracted.strip():
                text.append(extracted)

        return "#".join(text)

    # ---------- Unsupported ----------
    else:
        raise ValueError(
            "Unsupported file type. Please use TXT, DOCX, or PDF."
        )