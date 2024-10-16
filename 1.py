def evaluasi_performa(persen):
    if persen >= 90:
        return "Performa Luar Biasa :)"
    elif persen >= 80:
        return "Performa Sangat Baik ;)"
    elif persen >= 70:
        return "Performa Baik :)"
    elif persen >= 60:
        return "Performa Rata-Rata :|"
    else:
        return "Perlu Peningkatan :("


persen = float(input("Masukkan persentase nilai siswa tersebut: "))
print(evaluasi_performa(persen))
