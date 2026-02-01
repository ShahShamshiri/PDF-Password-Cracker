import PyPDF2
from PyPDF2 import PdfReader

pdf_file = 'file.pdf'

for i in range(1000000):
    password = f"{i:06d}"

    try:
        with open(pdf_file, 'rb') as file:
            reader = PdfReader(file, password=password)
            print(f"Password: {password}")
            break
    except PyPDF2.errors.PdfReadError:
        continue
