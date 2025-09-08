from PIL import Image

image_path = "data/image/img.png"

img = Image.open(image_path)
img.show()

img_resized = img.resize((100, 100))
img_resized.show()
