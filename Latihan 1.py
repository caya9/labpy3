from random import random

n = int(input("Masukkan nilai n: "))

i = 1
while i <= n:
    a = random()
    if a < 0.5:
        print(f"data ke-{i} => {a}")
        i += 1

print("Selesai")

