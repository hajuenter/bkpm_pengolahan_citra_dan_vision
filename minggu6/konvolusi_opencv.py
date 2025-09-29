import cv2
import numpy as np
import matplotlib.pyplot as plt

# Contoh citra 5x5
image = np.array(
    [
        [100, 120, 130, 140, 150],
        [110, 130, 150, 170, 160],
        [120, 140, 160, 180, 170],
        [130, 150, 170, 190, 180],
        [140, 160, 180, 200, 190],
    ],
    dtype=np.float32,
)

# Kernel rata-rata (Average filter) 3x3
kernel = np.ones((3, 3), np.float32) / 9

# Lakukan konvolusi menggunakan OpenCV
output_image = cv2.filter2D(image, -1, kernel)

print("Citra asli:")
print(image)
print("\nHasil konvolusi dengan OpenCV:")
print(output_image)

# Tampilkan citra dengan matplotlib
plt.subplot(1, 2, 1)
plt.title("Citra Asli")
plt.imshow(image, cmap="gray")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Hasil Konvolusi")
plt.imshow(output_image, cmap="gray")
plt.axis("off")

plt.show()
