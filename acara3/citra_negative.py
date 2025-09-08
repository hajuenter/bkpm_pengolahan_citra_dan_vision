import cv2
import numpy as np

# citra input adalah citra RGB
image = cv2.imread("data/image/img.png")

# konversi RGB ke Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# buat matriks 255 seukuran dengan citra
Matriks = np.ones(gray.shape, gray.dtype) * 255

# operasi citra negatif
citraNegatif = Matriks - gray

# simpan hasil ke file
filename1 = "acara3/output/CitraNegatif.png"
cv2.imwrite(filename1, citraNegatif)

# tampilkan hasil (opsional)
cv2.imshow("Citra Negatif", citraNegatif)
cv2.waitKey(0)
cv2.destroyAllWindows()
