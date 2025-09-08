from PIL import Image
import os

input_path = "data/image/img.png"
output_dir = "acara2/output"

os.makedirs(output_dir, exist_ok=True)

img = Image.open(input_path)

img_resized = img.resize((800, 600))

img_resized.save(os.path.join(output_dir, "resized_image_pillow.png"))
