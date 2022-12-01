print("Operasi Matematika")
print("1. Jumlah [+]")
print("2. Kurang [+]")
print("3. Kali [+]")
print("4. Bagi [/]")

menu = input("Pilih Operasi 1/2/3/4: ")
nilai_pertama = int(input("Masukan nilai_pertama"))
nilai_kedua = int(input("Masukan nilai_kedua"))


def penjumlahan(nilai_pertama, nilai_kedua):
Tambah = nilai_pertama + nilai_kedua
return Tambah

def pengurangan(nilai pertama, nilai kedua):
 Kurang = nilai_pertama - nilai_kedua
 return Kurang

def perkalian(nilai pertama, nilai kedua):
 Kali = nilai_pertama * nilai_kedua
 return Kali

def pembagian(nilai_pertama, nilai_kedua):
 Bagi = nilai pertama / nilai_kedua
return Bagi

if menu == ("1"):
    print("Hasil operasi dari, nilai_pertama", nilai_pertama, "+", nilai_kedua, "=",penjumlahan(nilai_pertama, nilai_kedua))
elif menu == ("2"):
    print("Hasil operasi dari, nilai_pertama", nilai_pertama, "-", nilai_kedua, "=",pengurangan(nilai pertama, nilai kedua))
elif menu == ("3"):
    print("Hasil operasi dari, nilai_pertama", nilai_pertama, "*", nilai_kedua, "=",perkalian(nilai pertama, nilai kedua))
else menu == ("4"):
    print("Hasil operasi dari, nilai_pertama", nilai_pertama, "*", nilai_kedua, "=",pembagian(nilai_pertama, nilai_kedua))

