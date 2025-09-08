import cv2
import numpy as np

# Baca gambar
image = cv2.imread("data/image/img.png")

# Konversi ke grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Buat matriks konstanta 100 dengan ukuran sama seperti citra grayscale
MatriksSatu = np.ones(gray.shape, dtype=np.uint8) * 100

# Operasi perkalian citra dengan matriks
citraPerkalian = cv2.multiply(gray, MatriksSatu)

# Simpan hasil
filename = "acara4/output/citraPerkalian.jpg"
cv2.imwrite(filename, citraPerkalian)

# Tampilkan hasil
cv2.imshow("Citra Grayscale", gray)
cv2.imshow("Hasil Perkalian", citraPerkalian)
cv2.waitKey(0)
cv2.destroyAllWindows()
