import json

# Fungsi untuk memastikan file sudah ada dan tidak kosong
def buat_file():
    # Buat file jika belum ada (mode a = append)
    file = open("data_keuangan.txt", "a")
    file.close()

    # Baca isi file
    file = open("data_keuangan.txt", "r")
    isi = file.read()
    file.close()

    # Kalau file kosong, isi dengan list kosong []
    if isi == "":
        file = open("data_keuangan.txt", "w")
        file.write("[]")
        file.close()

# Fungsi untuk membaca data dari file
def baca_data():
    file = open("data_keuangan.txt", "r")
    isi = file.read()
    file.close()
    data = json.loads(isi)
    return data

# Fungsi untuk menyimpan data ke file
def simpan_data(data):
    teks = json.dumps(data, indent=4)
    file = open("data_keuangan.txt", "w")
    file.write(teks)
    file.close()

# Fungsi untuk menampilkan menu
def tampilkan_menu():
    print("\n=== APLIKASI CATATAN KEUANGAN ===")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Semua Data")
    print("4. Keluar")

# Fungsi untuk menambahkan data
def tambah_data(data):
    print("--- Tambah Data Keuangan ---")
    tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
    keterangan = input("Masukkan keterangan: ")
    jumlah = input("Masukkan jumlah uang: ")
    tipe = input("Tipe (pemasukan/pengeluaran): ")

    if tipe != "pemasukan" and tipe != "pengeluaran":
        print("Tipe harus 'pemasukan' atau 'pengeluaran'")
        return

    if not jumlah.isdigit():
        print("Jumlah harus angka!")
        return

    item = {
        "tanggal": tanggal,
        "keterangan": keterangan,
        "jumlah": int(jumlah),
        "tipe": tipe
    }

    data.append(item)
    simpan_data(data)
    print("Data berhasil ditambahkan!")

# Fungsi untuk menghapus data
def hapus_data(data):
    tampilkan_data(data)
    if len(data) == 0:
        return

    print("--- Hapus Data Keuangan ---")
    nomor = input("Masukkan nomor data yang ingin dihapus: ")
    if not nomor.isdigit():
        print("Masukkan angka yang benar!")
        return

    nomor = int(nomor)
    if nomor < 1 or nomor > len(data):
        print("Nomor tidak ada!")
        return

    data.pop(nomor - 1)
    simpan_data(data)
    print("Data berhasil dihapus!")

# Fungsi untuk menampilkan semua data
def tampilkan_data(data):
    if len(data) == 0:
        print("Belum ada data.")
    else:
        print("=============== Daftar Data Keuangan ===============")
        print("No  | Tanggal     | Tipe         | Jumlah     | Keterangan")
        print("----+-------------+--------------+------------+----------------------")
        for i, d in enumerate(data):
            no = str(i + 1).ljust(3)
            tanggal = d["tanggal"].ljust(11)
            tipe = d["tipe"].ljust(12)
            jumlah = ("Rp" + str(d["jumlah"])).ljust(10)
            keterangan = d["keterangan"].ljust(20)
            print(f"{no} | {tanggal} | {tipe} | {jumlah} | {keterangan}")

# Program utama
def main():
    buat_file()
    data = baca_data()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambah_data(data)
        elif pilihan == "2":
            hapus_data(data)
        elif pilihan == "3":
            tampilkan_data(data)
        elif pilihan == "4":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")
            
main()
