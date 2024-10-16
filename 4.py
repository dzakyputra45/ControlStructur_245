def cetak_bilangan_ganjil(n):
    for i in range(1, n + 1, 2):
        print(i,  end=" ")

n = int(input("Masukkan angka: "))
print("Bilangan ganjil hingga", n, ":")
cetak_bilangan_ganjil(n)