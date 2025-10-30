saldo = 1000000

while True:
    print(f"\nSaldo saat ini: Rp {saldo}")
    print("1. Tarik Uang")
    print("2. Keluar")
    menu = input("Pilih menu (1/2): ")

    if menu == "1":
        tarik = int(input("Masukkan jumlah penarikan: "))
        if tarik > saldo:
            print("Saldo tidak cukup!")
        elif tarik <= 0:
            print("Jumlah penarikan harus lebih dari 0!")
        else:
            saldo -= tarik
            print("Penarikan berhasil!")
    elif menu == "2":
        print("Terima kasih telah menggunakan ATM!")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")

    if saldo <= 0:
        print("Saldo Anda telah habis. Terima kasih telah menggunakan ATM!")
        break
