import os
from PIL import Image

directory = "data/image"
output_directory = "acara2/output"

os.makedirs(output_directory, exist_ok=True)

# Loop semua file dalam folder
for filename in os.listdir(directory):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(directory, filename)
        img = Image.open(img_path)

        img_resized = img.resize((200, 200), Image.LANCZOS)

        save_path = os.path.join(output_directory, filename).replace("\\", "/")

        img_resized.save(save_path)

        print(f"Berhasil resize: {save_path}")
