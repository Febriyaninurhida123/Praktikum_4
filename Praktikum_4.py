i=0
Nama=[]
NIM=[]
Tugas=[]
UTS=[]
UAS=[]
NilaiAkhir=[]
while True:
    s_Nama=input("Masukan Nama  : ")
    Nama.append(s_Nama)
    s_NIM=input("Masukan NIM    : ")
    NIM.append(s_NIM)
    i_Tugas=input("Masukan Nilai Tugas  : ")
    Tugas.append(i_Tugas)
    i_UTS=input("Masukan Nilai UTS  : ")
    UTS.append(i_UTS)
    i_UAS=input("Masukan Nilai UAS    : ")
    UAS.append(i_UAS)
    i_NilaiAkhir=(int(i_Tugas)*0.30)+(int(i_UTS)*0.35)+(int(i_UAS)*0.35)
    NilaiAkhir.append(i_NilaiAkhir)

    more=""
    while more!="y" and more!="t":
        more=input("Tambah Data (y/t) ?")
    i+=1
    if more=="t":
        break

print("                                       Daftar Nilai Mahasiswa                                                                   ")
print("================================================================================================================================")
print("|       Nomor       |       Nama        |       NIM      |       Tugas      |       UTS      |      UAS       |     Akhir      |")
print("================================================================================================================================")
for n in range(i):
    print("|         ",n+1,"       |       ",Nama[n],"       |     ",NIM[n],"      |       ",Tugas[n],"     |       ",UTS[n],"     |      ",UAS[n],"      |       ",NilaiAkhir[n],"       |")
