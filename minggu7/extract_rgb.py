import cv2
import os
import pandas as pd

# Path ke folder gambar (sama seperti GLCM)
folder_path = "data/image/"
output_path = "minggu7/output/rgb_features_output.xlsx"

# Buat list untuk menyimpan hasil
data = []

# Pastikan foldernya benar
if not os.path.exists(folder_path):
    raise FileNotFoundError(f"Folder tidak ditemukan: {folder_path}")

# Iterasi melalui semua file dalam folder
for index, filename in enumerate(os.listdir(folder_path)):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):  # case-insensitive
        img_path = os.path.join(folder_path, filename)
        img = cv2.imread(img_path)

        if img is None:
            print(f"⚠️ Gagal membaca gambar: {filename}")
            continue

        # Ekstraksi nilai rata-rata RGB
        avg_color_per_row = cv2.mean(img)[:3]  # Ambil 3 komponen pertama (B, G, R)
        B, G, R = avg_color_per_row  # urutan dari OpenCV adalah BGR

        # Tambahkan data ke list
        data.append({"No": index + 1, "Nama": filename, "R": R, "G": G, "B": B})

# Buat DataFrame menggunakan pandas
df = pd.DataFrame(data, columns=["No", "Nama", "R", "G", "B"])

# Simpan hasil ke file Excel
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_excel(output_path, index=False)

print(f"✅ Hasil ekstraksi warna telah disimpan di: {output_path}")
