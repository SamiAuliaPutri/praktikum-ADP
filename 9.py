def input_data():
    jumlah = int(input("Masukkan jumlah praktikan: "))
    data = []
    for i in range(jumlah):
        print("Praktikan", i + 1)
        nama = input("Nama: ")
        nim = input("NIM: ")
        pretest = float(input("Nilai pretest: "))
        postest = float(input("Nilai postest: "))
        tugas = float(input("Nilai tugas/makalah: "))
        bonus = float(input("Nilai bonus: "))
        praktikan = {
            "nama": nama,
            "nim": nim,
            "pretest": pretest,
            "postest": postest,
            "tugas": tugas,
            "bonus": bonus
        }
        data.append(praktikan)
    return data

def hitung_nilai_akhir(data):
    for i in range(len(data)):
        pretest = data[i]["pretest"]
        postest = data[i]["postest"]
        tugas = data[i]["tugas"]
        bonus = data[i]["bonus"]
        nilai_akhir = 0.25 * pretest + 0.25 * postest + 0.5 * tugas + bonus
        data[i]["nilai_akhir"] = nilai_akhir
    return data

def urutkan_peringkat(data):
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i]["nilai_akhir"] < data[j]["nilai_akhir"]:
                sementara = data[i]
                data[i] = data[j]
                data[j] = sementara
    for i in range(n):
        data[i]["peringkat"] = i + 1
    return data

def hitung_rata_rata(data):
    total = 0
    for i in range(len(data)):
        total = total + data[i]["nilai_akhir"]
    return total / len(data)

def tampilkan_tabel(data):
    print("+-----------------+------------+-------------+-----------+-----------+--------+--------------+-----------+")
    print("| {:^15} | {:^10} | {:^11} | {:^9} | {:^9} | {:^6} | {:^12} | {:^9} |".format(
        "Nama", "NIM", "Pretest", "Postest", "Tugas", "Bonus", "Nilai Akhir", "Peringkat"))
    print("+-----------------+------------+-------------+-----------+-----------+--------+--------------+-----------+")

    for i in range(len(data)):
        print("| {:<15} | {:^10} | {:^11.2f} | {:^9.2f} | {:^9.2f} | {:^6.2f} | {:^12.2f} | {:^9} |".format(
            data[i]["nama"],
            data[i]["nim"],
            data[i]["pretest"],
            data[i]["postest"],
            data[i]["tugas"],
            data[i]["bonus"],
            data[i]["nilai_akhir"],
            data[i]["peringkat"]
        ))

    print("+-----------------+------------+-------------+-----------+-----------+--------+--------------+-----------+")
    rata2 = hitung_rata_rata(data)
    print("|  {:<74} | {:^12.2f} | {:^10}|".format("Rata-rata nilai akhir", rata2, ""))
    print("+--------------------------------------------------------------------------------------------------------+")

data_praktikan = input_data()
data_praktikan = hitung_nilai_akhir(data_praktikan)
data_praktikan = urutkan_peringkat(data_praktikan)
tampilkan_tabel(data_praktikan)