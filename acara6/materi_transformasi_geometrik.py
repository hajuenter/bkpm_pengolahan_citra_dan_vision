from PIL import Image, ImageOps

# Load image
image_path = "data/image/img.png"  # Ganti dengan path gambar Anda
image = Image.open(image_path)


# 1. Translasi (Translation)
def translate_image(image, x_shift, y_shift):
    width, height = image.size
    translation_matrix = (1, 0, x_shift, 0, 1, y_shift)
    translated_image = image.transform(
        (width, height), Image.AFFINE, translation_matrix
    )
    return translated_image


# 2. Rotasi (Rotation)
def rotate_image(image, angle):
    rotated_image = image.rotate(angle, expand=True)
    return rotated_image


# 3. Flipping (Refleksi)
def flip_image(image, mode="horizontal"):
    if mode == "horizontal":
        flipped_image = ImageOps.mirror(image)
    elif mode == "vertical":
        flipped_image = ImageOps.flip(image)
    return flipped_image


# 4. Zooming (Scaling)
def zoom_image(image, zoom_factor):
    width, height = image.size
    zoomed_image = image.resize((int(width * zoom_factor), int(height * zoom_factor)))
    return zoomed_image


# Contoh Penggunaan:
# Translasi gambar sejauh 50 piksel ke kanan dan 30 piksel ke bawah
translated = translate_image(image, 50, 30)

# Rotasi gambar sebesar 90 derajat
rotated = rotate_image(image, 90)

# Flipping gambar secara horizontal
flipped_horizontal = flip_image(image, "horizontal")

# Zooming gambar dengan faktor skala 1.5
zoomed = zoom_image(image, 1.5)

# Menyimpan hasil transformasi
translated.convert("RGB").save("acara6/output/translated_image.jpg")
rotated.convert("RGB").save("acara6/output/rotated_image.jpg")
flipped_horizontal.convert("RGB").save("acara6/output/flipped_horizontal_image.jpg")
zoomed.convert("RGB").save("acara6/output/zoomed_image.jpg")
