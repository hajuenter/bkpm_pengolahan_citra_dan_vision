import cv2

# Baca gambar
image = cv2.imread("data/image/img.png")

# Konversi ke grayscale
imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Simpan hasil grayscale ke folder yang sama
filename = "acara3/output/CitraGrey.png"
cv2.imwrite(filename, imgGray)

# Tampilkan hasil
cv2.imshow("Gray Image", imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()
