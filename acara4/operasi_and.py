import cv2
import numpy as np

# Membuat matriks kosong untuk menggambar persegi
persegi = np.zeros((400, 400), dtype="uint8")

# Menggambar persegi (x1,y1,x2,y2)
cv2.rectangle(persegi, (60, 60), (340, 340), 255, -1)

# Membuat matriks kosong untuk menggambar lingkaran
lingkaran = np.zeros((400, 400), dtype="uint8")

# Menggambar lingkaran (titik_pusat, radius, warna, thickness=-1 untuk penuh)
cv2.circle(lingkaran, (200, 200), 150, 255, -1)

# Penggunaan operator AND
operasiAND = cv2.bitwise_and(persegi, lingkaran)

# Tampilkan hasil
cv2.imshow("Persegi", persegi)
cv2.imshow("Lingkaran", lingkaran)
cv2.imshow("Operasi AND", operasiAND)
cv2.waitKey(0)
cv2.destroyAllWindows()
