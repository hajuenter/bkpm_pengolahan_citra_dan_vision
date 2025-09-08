import glob

images = glob.glob("data/image/*.[jp][pn]g")

for image in images:
    print(image.replace("\\", "/"))
