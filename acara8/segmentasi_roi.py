import cv2
import numpy as np

# Read image
image = cv2.imread("data/image/jeruk.png")

# Select ROI
r = cv2.selectROI("select the area", image)

# Crop image
cropped_image = image[int(r[1]) : int(r[1] + r[3]), int(r[0]) : int(r[0] + r[2])]

# Display cropped image
cv2.imshow("Crop Gambar", cropped_image)
cv2.waitKey(0)
