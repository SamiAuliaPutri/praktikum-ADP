import turtle
import math
import time

# Set layar
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.title("Animasi Bendera Merah Putih")

# Fungsi menggambar tiang bendera
def gambar_tiang():
    tiang = turtle.Turtle()
    tiang.hideturtle()         # Sembunyikan penunjuk turtle
    tiang.penup()
    tiang.goto(-200, -150)     # Posisi awal tiang
    tiang.pendown()
    tiang.color("gray")
    tiang.begin_fill()
    # Buat tiang persegi panjang
    for _ in range(2):
        tiang.forward(10)
        tiang.left(90)
        tiang.forward(300)
        tiang.left(90)
    tiang.end_fill()

# Fungsi menggambar satu bagian bendera (merah atau putih)
def gambar_gelombang(t, warna, atas, bawah, frame):
    t.color(warna)
    t.begin_fill()
    # Bagian atas (garis bergelombang)
    for i in range(50):
        x = -190 + i * 4
        y = atas + 10 * math.sin(math.radians(i * 10 + frame))
        t.goto(x, y)
    # Bagian bawah (kembali ke kiri)
    for i in range(49, -1, -1):
        x = -190 + i * 4
        y = bawah + 10 * math.sin(math.radians(i * 10 + frame))
        t.goto(x, y)
    t.end_fill()

# Fungsi menggambar seluruh bendera (merah dan putih)
def gambar_bendera(frame):
    bendera = turtle.Turtle()
    bendera.hideturtle()
    bendera.speed(0)
    bendera.penup()
    bendera.goto(-190, 150)
    bendera.pendown()

    # Gambar bagian merah
    gambar_gelombang(bendera, "red", 150, 130, frame)

    # Gambar bagian putih di bawah merah
    bendera.penup()
    bendera.goto(-190, 130)
    bendera.pendown()
    gambar_gelombang(bendera, "white", 130, 110, frame)

# Fungsi utama untuk menjalankan animasi
def animasi_bendera():
    frame = 0
    while True:
        turtle.clear()              # Bersihkan layar setiap frame
        gambar_tiang()              # Gambar ulang tiang
        gambar_bendera(frame)       # Gambar ulang bendera dengan frame saat ini
        frame += 2                  # Ubah nilai frame agar bendera bergelombang
        time.sleep(0.1)             # Jeda antar frame (kecepatan animasi)

# Jalankan animasi
animasi_bendera()