import math
print("=== Program Hitung Jarak Antar Titik ===")
# Input jumlah titik
print("Masukkan jumlah titik (minimal 2):")
n = int(input())
# Buat array 2 dimensi untuk simpan titik
titik = []
# Input koordinat tiap titik
i = 0
while i < n:
    print("Titik ke-", i+1)
    print("Masukkan koordinat x:")
    x = float(input())
    print("Masukkan koordinat y:")
    y = float(input())
    # Tambah ke array 2 dimensi
    titik.append([x, y])
    i = i + 1
# Tampilkan semua titik
print("\n--- Daftar Titik ---")
i = 0
while i < n:
    print("O" + str(i+1) + " = (" + str(titik[i][0]) + ", " + str(titik[i][1]) + ")")
    i = i + 1
# Hitung jarak antar semua pasangan titik
print("\n--- Jarak Antar Titik ---")
i = 0
while i < n:
    j = i + 1
    while j < n:
        dx = titik[i][0] - titik[j][0]
        dy = titik[i][1] - titik[j][1]
        jarak = math.sqrt(dx*dx + dy*dy)
        print("Jarak O" + str(i+1) + " ke O" + str(j+1) + " = %.2f" % jarak)
        j = j + 1
    i = i + 1