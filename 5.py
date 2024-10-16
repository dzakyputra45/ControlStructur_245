def cetak_pola(n):
    for i in range(1, n + 1):
        print((str(i) + " ") * i)


n = int(input("Masukkan nilai n: "))
cetak_pola(n)