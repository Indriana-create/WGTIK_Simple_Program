print ("========================================\n")
print ("          ~ Program Luas 3 Bidang ~       ")
print ("========================================\n")

print ("1. Luas Layang - Layang")
print ("2. Luas Lingkaran")
print ("3. Luas Segitiga \n")

while(1):
    pilih = input("*Silahkan masukkan angka 1-3 \nLuas Bidang yang Dicari : ")
    print ("\n")

    if int(pilih) == 1 :
        print("Luas Layang - Layang \n")
        d1 = input("Diagonal 1 : ")
        d2 = input("Diagonal 2 : ")
        Luas = 0.5*float(d1)*float(d2)
        print("Luas Layang - Layang = ", Luas)

    elif int(pilih) == 2 :
        print("Luas Lingkaran \n")
        r = input("Jari - jari Lingkaran : ")
        Luas = 3.14*float(r)*float(r)
        print("Luas Lingkaran = ", Luas)

    elif int(pilih) == 3 :
        print("Luas Segitiga \n")
        a = input("Alas Segitiga : ")
        t = input("Tinggi Segitiga : ")
        Luas = 0.5*float(a)*float(t)
        print("Luas Segitiga : ", Luas)

    else :
        print ("Bidang tidak ditemukan! \nSilahkan masukkan pilihan angka 1 - 3")

    print ("========================================\n")

