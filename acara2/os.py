import os

directory = "data/image"

for filename in os.listdir(directory):
    if filename.endswith((".jpg", ".png")):
        file_path = os.path.join(directory, filename)
        print(file_path.replace("\\", "/"))
