import cv2
from matplotlib import pyplot as plt


# Fungsi untuk menampilkan histogram citra
def tampilkan_histogram_citra(image_path):
    # Membaca citra dari path direktori
    image = cv2.imread(image_path)

    # Konversi citra dari BGR (format default OpenCV) ke RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Memisahkan kanal warna
    channels = ("r", "g", "b")
    colors = ("red", "green", "blue")

    plt.figure(figsize=(10, 5))

    for i, color in enumerate(colors):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color)
        plt.xlim([0, 256])

    plt.title("Histogram untuk setiap kanal warna")
    plt.xlabel("Intensitas Pixel")
    plt.ylabel("Jumlah Pixel")
    plt.show()


# Path ke citra
path = "data/image/img.png"

# Menampilkan histogram
tampilkan_histogram_citra(path)
