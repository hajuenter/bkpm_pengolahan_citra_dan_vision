import cv2
import numpy as np

image = cv2.imread("data/image/img.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Buat matriks konstanta (100) dengan ukuran sama
MatriksSatu = np.ones(gray.shape, gray.dtype) * 100

# Operasi penjumlahan
citraPenjumlahan = cv2.add(gray, MatriksSatu)

# Simpan hasil
filename1 = "acara3/output/CitraGreyPenjumlahan.png"
filename2 = "acara3/output/MatriksSatuPenjumlahan.png"
filename3 = "acara3/output/CitraPenjumlahan.png"

cv2.imwrite(filename1, gray)
cv2.imwrite(filename2, MatriksSatu)
cv2.imwrite(filename3, citraPenjumlahan)

cv2.imshow("Citra Grayscale", gray)
cv2.imshow("Matriks 100", MatriksSatu)
cv2.imshow("Citra Hasil Penjumlahan", citraPenjumlahan)

cv2.waitKey(0)
cv2.destroyAllWindows()
