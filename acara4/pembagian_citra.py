import cv2
import numpy as np

# Baca gambar
image = cv2.imread("data/image/img.png")

# Konversi ke grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Buat matriks konstanta 100 dengan ukuran sama seperti citra grayscale
MatriksSatu = np.ones(gray.shape, dtype=np.float32) * 100

# Operasi pembagian citra dengan matriks
citraPembagian = cv2.divide(gray.astype(np.float32), MatriksSatu)

# Normalisasi agar hasil bisa terlihat
citraPembagian = cv2.normalize(citraPembagian, None, 0, 255, cv2.NORM_MINMAX)
citraPembagian = citraPembagian.astype(np.uint8)

# Simpan hasil
filename = "acara4/output/citraPembagian.jpg"
cv2.imwrite(filename, citraPembagian)

# Tampilkan hasil
cv2.imshow("Citra Grayscale", gray)
cv2.imshow("Hasil Pembagian", citraPembagian)
cv2.waitKey(0)
cv2.destroyAllWindows()
