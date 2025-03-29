

import pdfplumber

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    return text

resume_text = extract_text_from_pdf("../data/resumes/sample_resume.pdf")
print(resume_text)
