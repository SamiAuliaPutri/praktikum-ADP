#buat struktur untuk menyimpan informasi kursi
m = 12  #baris kursi
n = 7  #kolom kursi

#buat layout kursi
kursi = [[i + 1 + j * n
    for i in range(n)] 
         for j in range(m)]

#tampilkan Layout Kursi
print("Selamat datang di sistem reservasi tiket konser!")
print("Tampilan Layout Kursi:")
for i in range(m):
    for j in range(n):
        print(kursi[i][j], end=" ")
    print()
    
# Harga Tiket
print("Harga Tiket")
print("VVIP   : Rp1,500,000")
print("VIP    : Rp1,000,000")
print("Reguler: Rp750,000")
print("Ekonomi: Rp500,000")

# Input jumlah tiket yang ingin dipesan
jumlah_pemesanan = int(input("Masukkan jumlah tiket yang ingin dipesan: "))

# Proses pemesanan tiket
for pemesanan_ke in range(1, jumlah_pemesanan + 1):
    print(f"Pemesanan ke{pemesanan_ke}:")
    nama = input("Masukkan nama Anda: ")
    no_kursi = int(input("Masukkan nomor kursi yang ingin dipesan: "))
    
    # Validasi kursi yang sudah dipesan
    while True:
        kursi_tersedia = False
        for i in range(m):
            for j in range(n):
                if kursi[i][j] == no_kursi:
                    kursi_tersedia = True
                    break
            if kursi_tersedia:
                break

        if kursi_tersedia:
            kursi[i][j] = 0  # Kursi yang sudah dipesan diberi nilai 0
            break
        else:
            print("Kursi sudah dipesan! Pilih nomor kursi yang lain.")
            no_kursi = int(input("Masukkan nomor kursi yang ingin dipesan: "))

    password = input("Buat password untuk akses konser: ")

    # Menentukan kategori kursi
    if no_kursi <= 2 * n:  # VVIP
        kategori = "VVIP"
        harga = 1500000
    elif no_kursi <= 5 * n:  # VIP
        kategori = "VIP"
        harga = 1000000
    elif no_kursi <= 15 * n:  # Reguler
        kategori = "Reguler"
        harga = 750000
    else:  # Ekonomi
        kategori = "Ekonomi"
        harga = 500000

    # Tampilkan struk pemesanan
    print("===== Struk Pemesanan Tiket =====")
    print(f"Nama: {nama}")
    print(f"Nomor Kursi: {no_kursi}")
    print(f"Kategori: {kategori}")
    print(f"Harga: Rp{harga:,}")
    print(f"Password: {password}")
    print("-----------------------------------------")

# Menampilkan sisa kursi per kategori
kategori_sisa = {"VVIP": 0, "VIP": 0, "Reguler": 0, "Ekonomi": 0}
for i in range(m):
    for j in range(n):
        if kursi[i][j] != 0:
            if kursi[i][j] <= 2 * n:
                kategori_sisa["VVIP"] += 1
            elif kursi[i][j] <= 5 * n:
                kategori_sisa["VIP"] += 1
            elif kursi[i][j] <= 15 * n:
                kategori_sisa["Reguler"] += 1
            else:
                kategori_sisa["Ekonomi"] += 1

# Menampilkan sisa kursi per kategori
print("Sisa kursi per kategori:")
for kat, sisa in kategori_sisa.items():
    print(f"{kat}: {sisa}")

# Menampilkan Layout Kursi Setelah Pemesanan
print("Layout Kursi Setelah Pemesanan:")
for i in range(m):
    for j in range(n):
        print(kursi[i][j], end=" ")
    print()

print("Terima kasih telah melakukan reservasi!")