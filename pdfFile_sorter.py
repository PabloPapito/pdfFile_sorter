import PyPDF2
import os

pdf_location = input("Please enter the path to the folder containing PDF files to verify: ")
pdf_new_location = input("Please enter the path to the folder where you want to store PDF files with the selected number of pages: ")
pdf_pages = input("Please enter the number of pages the PDF files should have: ")
pdf_pages = int(pdf_pages)

if not os.path.exists(pdf_new_location):
    os.makedirs(pdf_new_location)

for i in os.listdir(pdf_location):
    if os.path.isfile(os.path.join(pdf_location, i)):
        pdfFile = open(os.path.join(pdf_location, i), 'rb')
        reader = PyPDF2.PdfReader(pdfFile)
        length = len(reader.pages)
        pdfFile.close()
        if length != pdf_pages:
            os.replace(os.path.join(pdf_location, i), os.path.join(pdf_new_location, i))

print('Done!')

