import sys
import os
from PyPDF2 import PdfMerger

# Agar terminal se PDFs di hain to unhe lo
if len(sys.argv) > 1:
    inputs = sys.argv[1:]

# Warna default PDFs use karo
else:
    inputs = ["dummy.pdf", "two_page.pdf", "tilt.pdf"]


# PDF merge karne ka function
def pdf_combiner(pdf_list):

    # Merger object banao
    merger = PdfMerger()

    # Sabhi PDFs ko ek-ek karke add karo
    for pdf in pdf_list:
        merger.append(pdf)

    # Merged PDF save karo
    merger.write("super.pdf")

    # Merger close karo
    merger.close()

    print("✅ PDFs merged successfully!")


# Function call
pdf_combiner(inputs)

# Final PDF automatically open karo (Windows)
os.startfile("super.pdf")