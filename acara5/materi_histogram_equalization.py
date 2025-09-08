import cv2
import matplotlib.pyplot as plt

# Path ke gambar
image_path = "data/image/img.png"

# Memuat gambar
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Melakukan histogram equalization
equalized_image = cv2.equalizeHist(image)

# Menampilkan gambar asli dan gambar yang telah di-equalize
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Gambar Asli")
plt.imshow(image, cmap="gray")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Gambar setelah Equalization")
plt.imshow(equalized_image, cmap="gray")
plt.axis("off")

plt.show()
