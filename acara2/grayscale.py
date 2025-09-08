from PIL import Image
import os

# Path input & output
input_path = "data/image/img.png"
output_dir = "acara2/output"

# Buat folder output kalau belum ada
os.makedirs(output_dir, exist_ok=True)

# 1. Buka gambar
img = Image.open(input_path)

# 2. Konversi ke grayscale
img_gray = img.convert("L")
img_gray.save(os.path.join(output_dir, "gray_image.png"))

# 3. Simpan dengan kompresi maksimal (khusus PNG)
img.save(os.path.join(output_dir, "compressed_image.png"), optimize=True)
