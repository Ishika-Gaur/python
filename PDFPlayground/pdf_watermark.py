import os
from PyPDF2 import PdfReader, PdfWriter

# Main PDF open karo
template = PdfReader(open("super.pdf", "rb"))

# Watermark PDF open karo
watermark = PdfReader(open("watermark.pdf", "rb"))

# Writer object
output = PdfWriter()

# Watermark ka first page
watermark_page = watermark.pages[0]

# Main PDF ke sabhi pages par loop
for page in template.pages:

    # Watermark add karo
    page.merge_page(watermark_page)

    # Writer me page add karo
    output.add_page(page)

# New PDF save karo
with open("watermarked_output.pdf", "wb") as new_file:
    output.write(new_file)

print("✅ Watermark added successfully!")

# PDF automatically open karo (Windows)
os.startfile("watermarked_output.pdf")