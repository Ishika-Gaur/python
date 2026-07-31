# Rotate PDF project

import os
from PyPDF2 import PdfReader, PdfWriter

# PDF ko binary read mode me open karo
with open("dummy.pdf", "rb") as file:

    # Reader aur Writer object
    reader = PdfReader(file)
    writer = PdfWriter()

    # First page lo
    page = reader.pages[0]

    # 90° rotate karo
    page.rotate(-90)

    # Writer me add karo
    writer.add_page(page)

    # New PDF save karo
    with open("tilt.pdf", "wb") as new_file:
        writer.write(new_file)

print("✅ PDF rotated successfully!")

# PDF automatically open karo
os.startfile("tilt.pdf")



# Step 1
# reader = PdfReader(file)

# 👉 Python PDF ko padhta (read) hai.

# dummy.pdf
#     │
#     ▼
# Reader

# Ab Python ko pata chal gaya ki PDF me kya hai.

# Step 2
# page = reader.pages[0]

# 👉 PDF ka pehla page uthata hai.

# PDF
#  │
#  ├── Page 1  ← Ye page variable me aa gaya

# Ab page ke andar sirf Page 1 hai.

# Step 3
# page.rotate(-90)

# 👉 Ye Page 1 ko memory (RAM) me rotate karta hai.

# Pehle:

# 📄
# Hello Ishika!

# Rotate ke baad:

# 📄
# (90° ghoom gaya)

# ⚠️ Dummy.pdf abhi bhi same hai!

# Sirf RAM me copy rotate hui hai.

# Step 4
# writer = PdfWriter()

# 👉 Ek khali PDF banayi.

# Socho tumne ek nayi notebook kholi.

# Writer

# (Empty)
# Step 5
# writer.add_page(page)

# 👉 Rotated page ko us khali PDF me daal diya.

# Writer

# Page 1 (Rotated)
# Step 6
# writer.write(new_file)

# 👉 Is nayi PDF ko save kar diya.

# Ab folder me nayi file ban gayi:

# dummy.pdf      ← Original (same)
# tilt.pdf       ← Rotated copy