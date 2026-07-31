import sys
import os
from PIL import Image

source_folder = sys.argv[1]
destination_folder = sys.argv[2]

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for filename in os.listdir(source_folder):

    # PNG files lo
    if filename.endswith(".png"):

        img_path = os.path.join(source_folder, filename)

        # JPEG transparency support nahi karta
        img = Image.open(img_path).convert("RGB")

        clean_name = os.path.splitext(filename)[0]

        img.save(
            os.path.join(destination_folder, f"{clean_name}.jpeg"),
            "JPEG"
        )

        print(f"{filename} converted successfully!")

print("✅ All images converted successfully.")