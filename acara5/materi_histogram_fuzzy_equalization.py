import numpy as np
import cv2
import matplotlib.pyplot as plt


def fuzzy_membership_function(x, mean, stddev):
    return np.exp(-((x - mean) ** 2) / (2 * (stddev**2)))


def fuzzy_histogram_equalization(image, block_size=16):
    # Konversi gambar ke grayscale jika diperlukan
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Dapatkan dimensi gambar
    height, width = image.shape

    # Buat gambar yang telah di-equalize
    equalized_image = np.zeros_like(image, dtype=np.uint8)

    # Ukuran blok
    block_height = block_size
    block_width = block_size

    for y in range(0, height, block_height):
        for x in range(0, width, block_width):
            block = image[y : y + block_height, x : x + block_width]
            if block.size == 0:
                continue

            # Hitung histogram lokal
            hist, bins = np.histogram(block.flatten(), bins=256, range=[0, 256])
            cdf = hist.cumsum()
            cdf_normalized = cdf * 255 / cdf[-1]
            equalized_block = np.interp(
                block.flatten(), bins[:-1], cdf_normalized
            ).reshape(block.shape)

            # Hitung keanggotaan fuzzy
            mean = np.mean(equalized_block)
            stddev = np.std(equalized_block)
            membership = fuzzy_membership_function(equalized_block, mean, stddev)

            # Terapkan penyesuaian kontras fuzzy
            equalized_image[y : y + block_height, x : x + block_width] = np.clip(
                equalized_block * membership, 0, 255
            )

    return equalized_image


img = cv2.imread("data/image/img.png", cv2.IMREAD_COLOR)

# Panggil fungsi fuzzy histogram equalization
equalized = fuzzy_histogram_equalization(img)

# Tampilkan hasil
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Fuzzy Histogram Equalization")
plt.imshow(equalized, cmap="gray")
plt.axis("off")

plt.show()
