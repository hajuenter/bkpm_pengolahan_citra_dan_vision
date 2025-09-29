import cv2
import matplotlib.pyplot as plt
import numpy as np

# Path gambar jeruk
image_path = "data/image/jeruk.png"

# Baca gambar warna
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Gaussian blur 3x3
gaussian_3x3 = cv2.GaussianBlur(image_rgb, (3, 3), 0)

# Gaussian blur 5x5
gaussian_5x5 = cv2.GaussianBlur(image_rgb, (5, 5), 0)

# Kernel Unsharp Masking 5x5 (sesuai tabel)
unsharp_kernel = (
    np.array(
        [
            [1, 4, 6, 4, 1],
            [4, 16, 24, 16, 4],
            [6, 24, -476, 24, 6],
            [4, 16, 24, 16, 4],
            [1, 4, 6, 4, 1],
        ],
        dtype=np.float32,
    )
    / -256.0
)
# Terapkan unsharp masking
unsharp_result = cv2.filter2D(image_rgb, -1, unsharp_kernel)
# Tampilkan hasil
plt.figure(figsize=(6, 4))

plt.subplot(2, 2, 1)
plt.title("Asli")
plt.imshow(image_rgb)
plt.axis("off")

plt.subplot(2, 2, 2)
plt.title("Gaussian 3x3")
plt.imshow(gaussian_3x3)
plt.axis("off")

plt.subplot(2, 2, 3)
plt.title("Gaussian 5x5")
plt.imshow(gaussian_5x5)
plt.axis("off")

plt.subplot(2, 2, 4)
plt.title("Unsharp 5x5")
plt.imshow(unsharp_result)
plt.axis("off")

# Atur jarak antar subplot (top, bottom, left, right, wspace, hspace)
plt.subplots_adjust(wspace=0.1, hspace=0.2)

plt.show()
