import cv2
import numpy as np

# Membuat matriks kosong untuk menggambar persegi
persegi = np.zeros((400, 400), dtype="uint8")
cv2.rectangle(persegi, (80, 80), (320, 320), 255, -1)

# Membuat matriks kosong untuk menggambar lingkaran
lingkaran = np.zeros((400, 400), dtype="uint8")
cv2.circle(lingkaran, (200, 200), 120, 255, -1)

# Operasi XOR
operasiXOR = cv2.bitwise_xor(persegi, lingkaran)

# Tampilkan hasil
cv2.imshow("Persegi", persegi)
cv2.imshow("Lingkaran", lingkaran)
cv2.imshow("Operasi XOR", operasiXOR)
cv2.waitKey(0)
cv2.destroyAllWindows()
