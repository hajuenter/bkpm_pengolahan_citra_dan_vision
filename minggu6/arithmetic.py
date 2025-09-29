import cv2
import matplotlib.pyplot as plt
import numpy as np

# Path citra
image1_path = "data/image/anggur.png"
image2_path = "data/image/jeruk.png"

# Baca citra grayscale
image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)

# Resize citra kedua agar sama dengan citra pertama
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Operasi aritmatika & logika
addition_result = cv2.add(image1, image2)
subtraction_result = cv2.subtract(image1, image2)
multiplication_result = cv2.multiply(image1, image2)

with np.errstate(divide="ignore", invalid="ignore"):
    division_result = cv2.divide(image1.astype("float"), image2.astype("float"))
    division_result = np.nan_to_num(division_result).astype("uint8")

or_result = cv2.bitwise_or(image1, image2)
and_result = cv2.bitwise_and(image1, image2)
xor_result = cv2.bitwise_xor(image1, image2)

# ==== VISUALISASI ====
plt.figure(figsize=(8, 5))  # lebih pendek

titles = [
    "Citra 1",
    "Citra 2",
    "Penjumlahan",
    "Pengurangan",
    "Perkalian",
    "Pembagian",
    "OR",
    "AND",
    "XOR",
]

images = [
    image1,
    image2,
    addition_result,
    subtraction_result,
    multiplication_result,
    division_result,
    or_result,
    and_result,
    xor_result,
]

# Tampilkan 9 gambar dalam grid 3x3
for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.title(titles[i], fontsize=9)
    plt.imshow(images[i], cmap="gray", vmin=0, vmax=255)
    plt.axis("off")

# Atur jarak biar rapat
plt.subplots_adjust(wspace=0.1, hspace=0.25)

plt.show()
