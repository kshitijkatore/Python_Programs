from pdf2docx import Converter

pdf_file = input("Enter PDf file:")
docx_file = input("Enter Docx file:")

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close