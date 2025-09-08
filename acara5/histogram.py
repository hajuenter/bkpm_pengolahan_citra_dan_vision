import cv2
import numpy as np
from matplotlib import pyplot as plt
import os

# --- Buat folder output kalau belum ada ---
output_dir = "acara5/output"
os.makedirs(output_dir, exist_ok=True)

# --- Baca gambar ---
img = cv2.imread("data/image/img.png")

# --- Operasi citra ---
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Grayscale
Matriks = np.ones(img.shape[:2], img.dtype) * 255
negasi = Matriks - gray  # Negatif

# --- Histogram gambar awal ---
plt.hist(img.ravel(), 256, [0, 256])
plt.title("Histogram Gambar Asli")
plt.xlabel("Intensitas")
plt.ylabel("Frekuensi")
plt.savefig(os.path.join(output_dir, "CitraHistPython.jpg"))
plt.clf()
cv2.imwrite(os.path.join(output_dir, "CitraHistPythonImg.jpg"), img)

# --- Histogram grayscale ---
plt.hist(gray.ravel(), 256, [0, 256])
plt.title("Histogram Grayscale")
plt.xlabel("Intensitas")
plt.ylabel("Frekuensi")
plt.savefig(os.path.join(output_dir, "CitraHistGray.jpg"))
plt.clf()
cv2.imwrite(os.path.join(output_dir, "CitraHistGrayImg.jpg"), gray)

# --- Histogram negatif ---
plt.hist(negasi.ravel(), 256, [0, 256])
plt.title("Histogram Negatif")
plt.xlabel("Intensitas")
plt.ylabel("Frekuensi")
plt.savefig(os.path.join(output_dir, "CitraHistNegasi.jpg"))
plt.clf()
cv2.imwrite(os.path.join(output_dir, "CitraHistNegasiImg.jpg"), negasi)

