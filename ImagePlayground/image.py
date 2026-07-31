# Import Image class and ImageFilter module
from PIL import Image, ImageFilter

# Open image from folder
img = Image.open("./Pokedex/pikachu.png")

# -------------------------
# Image Information
# -------------------------

# Print Image Object
print("Image Object :", img)

# Print Image Format
print("Format :", img.format)

# Print Image Size
print("Size :", img.size)

# Print Image Mode
print("Mode :", img.mode)

# -------------------------
# Apply BLUR Filter
# -------------------------

blur_img = img.filter(ImageFilter.BLUR)
blur_img.save("blur.png")
print("Blur image saved!")

# -------------------------
# Apply SMOOTH Filter
# -------------------------

smooth_img = img.filter(ImageFilter.SMOOTH)
smooth_img.save("smooth.png")
print("Smooth image saved!")

# -------------------------
# Apply SHARPEN Filter
# -------------------------

sharp_img = img.filter(ImageFilter.SHARPEN)
sharp_img.save("sharp.png")
print("Sharpen image saved!")

# -------------------------
# Convert Image to Grayscale
# -------------------------

gray_img = img.convert("L")
gray_img.save("gray.png")
print("Grayscale image saved!")

print("\nAll image processing completed successfully!")