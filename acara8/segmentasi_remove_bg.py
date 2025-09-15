from rembg import remove
from PIL import Image
import matplotlib.pyplot as plt

# Baca gambar input
inp = Image.open("data/image/jeruk.png")

# Hapus background (langsung tanpa save)
out = remove(inp)

# Tampilkan pakai matplotlib
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Sebelum
axes[0].imshow(inp)
axes[0].set_title("Sebelum Remove BG")
axes[0].axis("off")

# Sesudah
axes[1].imshow(out)
axes[1].set_title("Setelah Remove BG")
axes[1].axis("off")

plt.tight_layout()
plt.show()
