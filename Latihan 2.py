modal_awal = 100000000

total_laba = 0

for bulan in range(1, 9):
    if bulan == 1 or bulan == 2:
        laba = 0
    elif bulan == 3 or bulan == 4:
        laba = modal_awal * 0.01
    elif bulan == 5 or bulan == 6 or bulan == 7:
        laba = modal_awal * 0.05
    elif bulan == 8:
        laba = modal_awal * 0.03
    else:
        laba = 0

    print(f"Laba bulan ke-{bulan} sebesar: {int(laba)}")

    total_laba += laba

print(f"Total laba adalah: {int(total_laba)}")
