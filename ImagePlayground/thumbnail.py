from PIL import Image

# Open image
img = Image.open("./pokedex/astro.png")

# Print original size
print("Original Size :", img.size)

# Create thumbnail
img.thumbnail((400,400))

# Save thumbnail
img.save("thumbnail.jpg")

# Print new size
print("Thumbnail Size :", img.size)


# Yaad rakhne ki Trick

# 👉 resize() = "Mujhe bas exact size chahiye."

# 👉 thumbnail() = "Mujhe image ki shape (Aspect Ratio) bhi bachani hai."

# Example:

# Original Image: 6240 × 4160

# img.resize((400, 400))

# ➡️ Output: 400 × 400 (Image squish ho sakti hai.)

# img.thumbnail((400, 400))

# ➡️ Output: 400 × 267 (Aspect Ratio maintain rahega.)