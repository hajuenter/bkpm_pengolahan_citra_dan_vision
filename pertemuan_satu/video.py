import cv2

cap = cv2.VideoCapture("data/video/video.mkv")

if not cap.isOpened():
    print("Error: Tidak bisa membuka video")
    exit()

win_name = "VIDEO"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)

cv2.resizeWindow(win_name, 700, 500)

print("Tekan 'q' untuk keluar")
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow(win_name, frame)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
