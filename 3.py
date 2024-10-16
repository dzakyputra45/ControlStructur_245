def deret_fibonacci(n):
    deret = [0, 1]
    while len (deret) < n:
        deret.append(deret[-1] + deret[-2])
    return deret

n = int(input("Masukkan angka: "))
print(deret_fibonacci(n))