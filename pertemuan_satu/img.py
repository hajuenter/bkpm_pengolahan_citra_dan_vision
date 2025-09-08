import cv2

# Baca gambar
img = cv2.imread("data/image/img.png")

win_name = "IMAGE"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

cv2.resizeWindow(win_name, 700, 500)

cv2.imshow(win_name, img)

print("Tekan 'q' untuk keluar")
while True:
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
