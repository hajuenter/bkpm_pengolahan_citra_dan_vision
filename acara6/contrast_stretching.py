import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Pastikan folder output ada
os.makedirs("acara6/output", exist_ok=True)

# Baca citra asli
img = cv2.imread("data/image/img.png")

# Konversi ke grayscale
bakteri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Equalisasi histogram
equ = cv2.equalizeHist(bakteri)

# Simpan hasil citra
filename1 = "acara6/output/CitraAsliBakteri.png"
cv2.imwrite(filename1, img)

filename2 = "acara6/output/CitraGrayBakteri.png"
cv2.imwrite(filename2, bakteri)

filename3 = "acara6/output/CitraHistEqualizerBakteri.png"
cv2.imwrite(filename3, equ)
