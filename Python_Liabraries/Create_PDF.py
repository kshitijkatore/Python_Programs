# Creating a New PDF 
from reportlab.pdfgen import canvas
# Create a new PDF file
c = canvas.Canvas('xitij.pdf')

# Add text and shape to the PDF file

c.drawString(100, 750, 'Hello World!')
c.line(100, 740, 300, 740)

# Save the PDF file
c.save()
