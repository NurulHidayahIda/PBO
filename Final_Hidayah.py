import math
print('''NAMA  : NURUL HIDAYAH
NIM   : D0221374
KELAS : INFORMATIKA H
________________________\n
===== MENGHITUNG LUAS BANGUN DATAR & VOLUME BANGUN RUANG =====\n''')
class Menghitung :
    def Segitiga(self):
        pass
    def Persegi(self):
        pass
    def Lingkaran(self):
        pass
    def Kubus(self):
        pass
    def Balok(self):
        pass
    def Tabung(self):
        pass    
    def printSegitiga (self) :
        print('Luas Segitiga = ',self.Segitiga())
    def printPersegi (self) :
        print('Luas Persegi = ',self.Persegi())
    def printLingkaran (self) :
        print('Luas Lingkaran = ',self.Lingkaran())
    def printKubus (self) :
        print('Luas Kubus = ',self.Kubus())
    def printBalok (self) :
        print('Luas Balok = ',self.Balok())
    def printTabung (self) :
        print('Luas Tabung = ',self.Tabung())

    
class Luas(Menghitung):
    def __init__(self):
        self.panjang = 0
        self.lebar = 0
        self.r = 0
        self.alas = 0
        self.tinggi = 0
    def Segitiga(self):
        return 0.5 * self.alas * self.tinggi   
    def Persegi(self):
        return self.panjang * self.lebar
    def Lingkaran(self):
        return 3.14 * self.r * self.r
    
class Volume(Menghitung) :
    def __init__(self) :
        self.rusuk = 0
        self.panjang = 0
        self.lebar = 0
        self.tinggi = 0
        self.r = 0
    def Kubus (self):
        return self.rusuk * self.rusuk * self.rusuk
    def Balok (self):
        return self.panjang * self.lebar * self.tinggi
    def Tabung (self) :
        return 3.14 * self.r * self.r * self.tinggi

def looping() :
    print('Ingin Menghitung lagi?? (y/n)')
    x = input('=> ').lower()
    return True if x == "y" else False

luas = Luas()
volume = Volume()

while True :
    print('''\nMasukkan Pilihan
1. Luas Bangun Datar
2. Volume Bangun Ruang
3. Stop''')
    opsi = int(input('=> '))
    if opsi == 1 :
        while True :
            print('''\n1. Segitiga
2. Persegi
3. Lingkaran
4. Stop''')
            opsi1 = int(input('=> '))
            if opsi1 == 1 :
                while True :
                    luas.alas = float(input('Masukkan alas : '))
                    luas.tinggi = float(input('Masukkan tinggi : '))
                    print()
                    luas.printSegitiga()
                    if looping() != True:
                        break
            elif opsi1 == 2 :
                while True :
                    luas.panjang = float(input('Masukkan panjang : '))
                    luas.lebar = float(input('Masukkan lebar : '))
                    print()
                    luas.printPersegi()
                    if looping() != True:
                        break
            elif opsi1 == 3 :
                while True :
                    luas.r = float(input('Masukkan jari-jari : '))
                    print()
                    luas.printLingkaran()
                    if looping() != True:
                        break
            elif opsi1 == 4 :
                break
            else :
                print('Pilihanmu Salah!!')

    elif opsi == 2 :
        while True :
            opsi2 =int(input('''\n1. Kubus
2. Balok
3. Tabung
4. Stop
=>'''))
        
            if opsi2 == 1 :
                while True :
                    volume.rusuk = float(input('Masukkan rusuk : '))
                    print()
                    volume.printKubus()
                    if looping() != True:
                            break
            elif opsi2 == 2 :
                while True :
                    volume.panjang = float(input('Masukkan panjang : '))
                    volume.lebar = float(input('Masukkan lebar : '))
                    volume.tinggi = float(input('Masukkan tinggi : '))
                    print()
                    volume.printBalok()
                    if looping() != True:
                            break
            elif opsi2 == 3 :
                while True :
                    volume.r = float(input('Masukkan jari-jari : '))
                    volume.tinggi = float(input('Masukkan tinggi : '))
                    print()
                    volume.printTabung()
                    if looping() != True:
                            break
            elif opsi2 == 4 :
                break
            else :
                print('Pilihanmu Salah!!!')
    elif opsi == 3 :
            break
    else :
            print('Pilihanmu Salah!!!')

print("Program selesai. bye!")
        
        

   
    
                

                
