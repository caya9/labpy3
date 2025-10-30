# LAPORAN PRAKTIKUM 3 - PERULANGAN (LOOPING)
Nama        : Chaya Aulia

NIM         : 312510197

Kelas       : TI.25.A2

Mata Kuliah : Pengantar Pemrograman
## Tujuan Praktikum :
Mempelajari dan memahami cara kerja perulangan (loop) dalam bahasa Python menggunakan: -for loop (counted loop) -while loop (uncounted loop)

# Latihan 1 - Menampilkan Bilangan Acak Kurang dari 0.5
Alur Algoritma

Import modul random untuk menghasilkan bilangan acak.
Input jumlah bilangan (n) dari user.
Gunakan perulangan for sebanyak n kali.
Tampilkan hanya bilangan acak yang lebih kecil dari 0.5.

```python
from random import random

print("=== Program Menampilkan n Bilangan Acak yang Lebih Kecil dari 0.5 ===")

n = int(input("Masukkan jumlah bilangan acak: "))

for i in range(n):
    a = random()
    if a < 0.5:
        print(f"Data ke-{i+1} -> {a}")
```
```python
Masukkan jumlah bilangan acak: 5
Data ke-1 -> 0.4321
Data ke-3 -> 0.2214
```
# Latihan 2 - Menghitung Keuntungan Investasi
Alur Algoritma

Modal awal Rp 100.000.000.
Gunakan perulangan for selama 8 bulan.
Tentukan persentase laba tiap bulan: Bulan 1–2 = 0% Bulan 3–4 = 1% Bulan 5–7 = 5% Bulan 8 = 3%
Hitung laba setiap bulan, tampilkan, dan jumlahkan totalnya.

```python
print("=== Program Menghitung Total Keuntungan Investasi ===")

modal_awal = 100000000
laba = 0
total = 0

for bulan in range(1, 9):
    if bulan in [1, 2]:
        laba = 0
    elif bulan in [3, 4]:
        laba = 0.01 * modal_awal
    elif bulan in [5, 6, 7]:
        laba = 0.05 * modal_awal
    elif bulan == 8:
        laba = 0.03 * modal_awal
    total += laba
    print(f"Bulan ke-{bulan} laba = {laba:.0f}")

print(f"\nTotal laba selama 8 bulan = Rp {total:.0f}")
```
# Contoh Hasil
```python
Bulan ke-1 laba = 0
Bulan ke-2 laba = 0
Bulan ke-3 laba = 1000000
Bulan ke-4 laba = 1000000
Bulan ke-5 laba = 5000000
Bulan ke-6 laba = 5000000
Bulan ke-7 laba = 5000000
Bulan ke-8 laba = 3000000

Total laba selama 8 bulan = Rp 21000000
```
# Latihan 3 - Simulasi Mesin ATM
Alur Algoritma

Tentukan saldo awal = Rp 1.000.000.
Tampilkan menu utama:
Cek saldo, Tarik uang, Keluar
Gunakan perulangan while agar program terus berjalan.
Saat user memilih tarik uang:
Cek apakah saldo cukup.
Jika cukup, kurangi saldo. Jika tidak, tampilkan pesan “Saldo tidak cukup!”.
Jika memilih keluar, hentikan perulangan.
```python
print("=== Program Simulasi ATM Sederhana ===")

saldo = 1000000

while True:
    print("\nMenu:")
    print("1. Cek Saldo")
    print("2. Tarik Uang")
    print("3. Keluar")
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        print(f"Saldo Anda sekarang: Rp {saldo}")
    elif pilihan == "2":
        tarik = int(input("Masukkan jumlah uang yang ingin ditarik: "))
        if tarik <= saldo:
            saldo -= tarik
            print(f"Anda menarik Rp {tarik}. Sisa saldo: Rp {saldo}")
        else:
            print("Saldo tidak cukup!")
    elif pilihan == "3":
        print("Terima kasih telah menggunakan ATM.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
```
# Contoh Hasil
```python
Menu:
1. Cek Saldo
2. Tarik Uang
3. Keluar
Pilih menu (1/2/3): 2
Masukkan jumlah uang yang ingin ditarik: 500000
Anda menarik Rp 500000. Sisa saldo: Rp 500000
```
