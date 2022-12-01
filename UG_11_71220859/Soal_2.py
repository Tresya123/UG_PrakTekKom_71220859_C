print("Pemeriksa Kelipatan 9")
kelipatan = int(input("Masukkan kelipatana 9 yang ingin diperiksa"))

def kelipatan_sembilan():
    nilai = (kelipatan%9)
    return nilai

if kelipatan_sembilan() == 0:
    print("BENAR")
else:
    print("SALAH")