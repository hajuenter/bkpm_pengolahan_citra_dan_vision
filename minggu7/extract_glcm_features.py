import os
import cv2
import pandas as pd
from skimage.feature import graycomatrix, graycoprops

# Path ke folder gambar
folder_path = "data/image/"
output_dir = "minggu7/output/"
output_path = os.path.join(output_dir, "glcm_features_output.xlsx")

# Pastikan folder output ada
os.makedirs(output_dir, exist_ok=True)

# Buat list untuk menyimpan hasil
data = []


# Fungsi untuk menghitung fitur GLCM dengan scikit-image
def extract_glcm_features(image_gray):
    # Hitung GLCM (Gray Level Co-occurrence Matrix)
    glcm = graycomatrix(image_gray, [1], [0], symmetric=True, normed=True)

    contrast = graycoprops(glcm, "contrast")[0, 0]
    homogeneity = graycoprops(glcm, "homogeneity")[0, 0]
    energy = graycoprops(glcm, "energy")[0, 0]
    correlation = graycoprops(glcm, "correlation")[0, 0]

    return contrast, homogeneity, energy, correlation


# Iterasi semua gambar
for index, filename in enumerate(os.listdir(folder_path)):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(folder_path, filename)
        img = cv2.imread(img_path)
        if img is None:
            print(f"Gagal membaca gambar: {filename}")
            continue

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Ekstraksi fitur
        contrast, homogeneity, energy, correlation = extract_glcm_features(img_gray)

        data.append([index + 1, filename, contrast, homogeneity, energy, correlation])

# Simpan ke Excel
df = pd.DataFrame(
    data, columns=["No", "Nama", "Kontras", "Homogenitas", "Energi", "Korelasi"]
)
df.to_excel(output_path, index=False)

print(f"✅ Hasil ekstraksi fitur GLCM telah disimpan di: {output_path}")
