import docx
from PyPDF2 import PdfReader

def read_docx(file_path):
    try:
        doc = docx.Document(file_path)
        text = [para.text for para in doc.paragraphs if para.text.strip()]
        return "\n".join(text)
    except Exception as e:
        print(f"Error reading DOCX file: {e}")
        return ""

def read_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        print(f"Error reading PDF file: {e}")
        return ""