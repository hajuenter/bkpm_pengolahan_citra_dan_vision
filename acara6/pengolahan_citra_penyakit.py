import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

output_dir = "acara6/output"
os.makedirs(output_dir, exist_ok=True)

# === Baca gambar input ===
img = cv2.imread("data/image/img.png")


# === Proses citra ===
daun = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
M = np.ones(daun.shape, dtype="uint8") * 75
cerah = cv2.add(daun, M)
gelap = cv2.subtract(daun, M)

# === Simpan hasil ke folder output ===
cv2.imwrite(os.path.join(output_dir, "CitraAsliPenyakit.png"), img)
cv2.imwrite(os.path.join(output_dir, "CitraGrayPenyakit.png"), daun)
cv2.imwrite(os.path.join(output_dir, "CitraCerahPenyakit.png"), cerah)
cv2.imwrite(os.path.join(output_dir, "CitraGelapPenyakit.png"), gelap)

print(f"✅ Semua file berhasil disimpan di folder: {output_dir}")
