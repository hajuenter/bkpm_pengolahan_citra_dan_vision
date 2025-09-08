import cv2
import numpy as np

# Membuat matriks kosong untuk menggambar persegi
persegi = np.zeros((400, 400), dtype="uint8")
cv2.rectangle(persegi, (60, 60), (340, 340), 255, -1)

# Membuat matriks kosong untuk menggambar lingkaran
lingkaran = np.zeros((400, 400), dtype="uint8")
cv2.circle(lingkaran, (200, 200), 150, 255, -1)

# Operasi OR
operasiOR = cv2.bitwise_or(persegi, lingkaran)

# Tampilkan hasil
cv2.imshow("Persegi", persegi)
cv2.imshow("Lingkaran", lingkaran)
cv2.imshow("Operasi OR", operasiOR)
cv2.waitKey(0)
cv2.destroyAllWindows()
