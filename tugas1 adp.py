#TAMPILAN 1
print("================DAFTAR PAKET MAKANAN===================")
print("paket a:katsu + jus mangga                  : Rp.25.000")
print("paket b:ayam geprek + nasi putih + es jeruk : Rp.30.000")
print("paket c:mie rebus + nasi putih + es teh     : Rp.25.000")
print("paket d:nasi goreng + es jeruk              : Rp.15.000")
print("paket e:mie goreng + nasi putih + es teh    : Rp.20.000")


#TAMPILAN 2
print("======================DATA DIRI========================")
nama = input("masukkan nama                                 : ")
no_telepon = input("masukkan no telepon                     : ")
jenis_alamat_pengiriman = input("masukkan alamat pengiriman : ")
Paket_makanan = input("pilih paket makanan                  : ")
#menentukan harga sesuai pilihan
if Paket_makanan == "paket a" :
    isi_paket = print("katsu + jus mangga")
    harga         = 25000
elif Paket_makanan == "paket b" :
    isi_paket = print("ayam geprek + nasi putih + es jeruk")
    harga         = 30000
elif Paket_makanan == "paket c" :
    isi_paket = print("mie rebus + nasi putih + es teh")
    harga         = 25000
elif Paket_makanan == "paket d" :
    isi_paket = print("nasi goreng + es jeruk")
    harga         = 15000
elif Paket_makanan == "paket e" :
    isi_paket = print("mie goreng + nasi putih + es teh")
    harga         = 20000
else :
    print("paket makanan tidak tersedia")

#menghitung total harga
print("total harga                                       :", harga) 
jumlah_pesanan      = int(input("jumlah paket yang dibeli: "))
pajak               = (harga * 0.1)
harga_total         = (harga * jumlah_pesanan) + pajak   #harga sudah termasuk pajak
print("total harga yang dibayar                          :" , harga_total)

#biaya pengiriman
if harga_total < 150000 :
   biaya_pengiriman = 25000
else:
   biaya_pengiriman = 0
   
total_akhir = harga_total + biaya_pengiriman


#TAMPILAN 3
#menampilkan struk pemesanan
print("===============STRUK PESANAN==================")
print(f"nama                      :" ,nama)
print(f"no_telepon                :" ,no_telepon)
print(f"jenis_alamat_pengiriman   :" ,jenis_alamat_pengiriman)
print(f"harga_paket_makanan       :" ,harga)
print(f"jumlah_pesanan            :" ,jumlah_pesanan)
print(f"pajak                     :" ,pajak)
print(f"harga_total               :" ,harga_total)
print(f"biaya_pengiriman          :" ,biaya_pengiriman)
print(f"total_akhir               :" ,total_akhir)

