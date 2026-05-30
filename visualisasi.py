import pandas as pd
import matplotlib.pyplot as plt

# baca data csv
data = pd.read_csv("jobs.csv")

# hitung jumlah lokasi
lokasi = data["location"].value_counts().head(10)

# buat grafik
lokasi.plot(kind="bar")

# judul grafik
plt.title("Top 10 Lokasi Lowongan Kerja")

# nama sumbu X
plt.xlabel("Lokasi")

# nama sumbu Y
plt.ylabel("Jumlah Job")

# tampilkan grafik
plt.show()