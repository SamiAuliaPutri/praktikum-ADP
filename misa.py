daftar_nim = []
daftar_nama = []
daftar_nilai = []

while True:
    print('''
PROGRAM MANAJEMEN NILAI MAHASISWA

1. Tambah Data
2. Hapus Data
3. Tampilkan Data
4. Keluar
''')

    pilihan = input("Pilih opsi (1/2/3/4): ")

    if pilihan == '1':
        nim = input("Masukkan NIM Mahasiswa: ")
        nama = input("Masukkan Nama Mahasiswa: ")
        nilai = float(input("Masukkan Nilai Mahasiswa: "))
        daftar_nim.append(nim)
        daftar_nama.append(nama)
        daftar_nilai.append(nilai)
        print("Data berhasil ditambahkan.")
        
    elif pilihan == '2':
        nim_hapus = input("Masukkan NIM Mahasiswa yang ingin dihapus: ")
        for i in range(len(daftar_nim)):
            if daftar_nim[i] == nim_hapus:
                for j in range(i, len(daftar_nim) - 1):
                    daftar_nim[j] = daftar_nim[j + 1]
                    daftar_nama[j] = daftar_nama[j + 1]
                    daftar_nilai[j] = daftar_nilai[j + 1]
                daftar_nim.pop()
                daftar_nama.pop()
                daftar_nilai.pop()
                print("Data berhasil dihapus.")
                break
        else:
            print("Data tidak ditemukan")

    elif pilihan == '3':
        if len(daftar_nim) == 0:
            print("Belum ada data mahasiswa.")
        else:
            # Urutkan dari nilai tertinggi
            n = len(daftar_nilai)
            for i in range(n):
                for j in range(i + 1, n):
                    if daftar_nilai[i] < daftar_nilai[j]:
                        daftar_nim[i], daftar_nim[j] = daftar_nim[j], daftar_nim[i]
                        daftar_nama[i], daftar_nama[j] = daftar_nama[j], daftar_nama[i]
                        daftar_nilai[i], daftar_nilai[j] = daftar_nilai[j], daftar_nilai[i]

            print("DATA MAHASISWA (DARI NILAI TERTINGGI):")
            print("..............................................")
            print("NIM       Nama               Nilai")
            print("..............................................")
            for i in range(len(daftar_nim)):
                print(f"{daftar_nim[i]:<10}{daftar_nama[i]:<18}{daftar_nilai[i]}")
            print("..............................................")

    elif pilihan == '4':
        print("Terima kasih telah menggunakan program ini.")
        break

    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

