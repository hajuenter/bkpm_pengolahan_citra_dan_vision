from PIL import Image
import os

img = Image.open("data/image/img.png")

os.makedirs("acara2/output", exist_ok=True)

img_rgb = img.convert("RGB")
img_rgb.save("acara2/output/image_converted.jpg")

img.save("acara2/output/new_image.png")

# 4. Simpan JPG dengan kualitas berbeda
img_rgb.save("acara2/output/image_quality85.jpg", quality=85)
