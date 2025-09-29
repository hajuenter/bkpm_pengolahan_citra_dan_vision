import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage import data

# Mengambil gambar contoh dari skimage
image_example = data.camera()

# Sobel
sobel_x = cv2.Sobel(image_example, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image_example, cv2.CV_64F, 0, 1, ksize=3)
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# Prewitt
prewitt_x = cv2.filter2D(
    image_example, -1, np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
)
prewitt_y = cv2.filter2D(
    image_example, -1, np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
)
prewitt_combined = np.sqrt(np.square(prewitt_x) + np.square(prewitt_y))

# Canny
canny_edges = cv2.Canny(image_example, 100, 200)

plt.figure(figsize=(7, 5))  # lebar 8, tinggi 4 (lebih pendek)

plt.subplot(2, 2, 1)
plt.title("Gambar Asli")
plt.imshow(image_example, cmap="gray")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.title("Sobel")
plt.imshow(sobel_combined, cmap="gray")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.title("Prewitt")
plt.imshow(prewitt_combined, cmap="gray")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.title("Canny")
plt.imshow(canny_edges, cmap="gray")
plt.axis("off")

plt.tight_layout()
plt.show()
