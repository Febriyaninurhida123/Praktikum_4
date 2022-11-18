KoreanFood=["ramyeon", "gimbab", "kimchi", "tteokbokki", "bulgogi"]
print("Menu Makanan Korea:", KoreanFood)

print("Tampilkan menu ke 3:", KoreanFood[2])
print("ambil menu ke 2 sampai 4:", KoreanFood[1:4])
print("ambil menu terakhir:", KoreanFood[5-1])

# merubah elemen ke 4 dengan nilai lain
KoreanFood[3] = "Kue Beras Pedas"

print("merubah menu ke 4 dengan nilai lain:", KoreanFood)

# merubah elemen ke 4 sampai terakhir
KoreanFood[3:] = "Kue Beras Pedas", "Daging BBQ"
print("merubah menu ke 4 sampai menu terakhir:", KoreanFood)

# tambah elemen list
Ganjil=[1,3,5,7,9]
Genap=[2,4,6,8,10]
print("kelompok Ganjil:", Ganjil, "Kelompok Genap:", Genap)
# Ambil 2 bagian list Ganjil ke list Genap
Genap.append(Ganjil[1:3])
print("2 bagian List Ganjil dijadikan List Genap:", Genap)

# tambah list Genap dengan string
Genap.append("Habis Dibagi 2")
print("Tambah Genap dengan Sring:", Genap)

# tambah list Genap dengan 3 nilai
print("Tambah list Genap dengan 3 nilai:", Genap+[11,12,13])

#Gabungan List Genap dan Ganjil
Angka=Genap+Ganjil
print("Gabungan list Genap dan Ganjil:", Angka)
