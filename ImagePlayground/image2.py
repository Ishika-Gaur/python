from PIL import Image

# Open original image
img = Image.open("./Pokedex/pikachu.png")

# Show original image
img.show()

# Print original details
print("Original Image")
print("Size :", img.size)
print("Mode :", img.mode)
print("-" * 30)

# Convert to grayscale
gray = img.convert("L")
gray.show()
gray.save("gray.png")

print("Gray Image")
print("Size :", gray.size)
print("Mode :", gray.mode)
print("-" * 30)

# Rotate image
rotated = gray.rotate(90)
rotated.show()
rotated.save("rotated.png")

print("Rotated Image")
print("Size :", rotated.size)
print("Mode :", rotated.mode)
print("-" * 30)

# Resize image
small = rotated.resize((300, 300))
small.show()
small.save("small.png")

print("Resized Image")
print("Size :", small.size)
print("Mode :", small.mode)
print("-" * 30)

# Crop image
cropped = small.crop((50, 50, 250, 250))
cropped.show()
cropped.save("cropped.png")

print("Cropped Image")
print("Size :", cropped.size)
print("Mode :", cropped.mode)
print("-" * 30)

print("✅ All images saved successfully!")


# Mode	Meaning
# RGB	 Red, Green, Blue
# RGBA	 RGB + Alpha (Transparency)
# L	     Grayscale (Black & White)
# 1     	Black & White (sirf 2 colors: Black ya White)
# CMYK	 Printing ke liye (Cyan, Magenta, Yellow, Black)