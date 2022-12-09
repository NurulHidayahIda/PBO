print('''NAMA  : NURUL HIDAYAH
NIM   : D0221374
KELAS : INFORMATIKA H
________________________\n
===== MENGHITUNG VOLUME BANGUN RUANG =====\n''')
x = 'Y'
while x== 'Y':
    print('''
Silahkan pilih perintah dibawah ini :
1. Vulume Balok
2. Volume Kubus
3. Volume Tabung\n''')
    perintah = int(input('Masukkan : '))
    if perintah == 1:              
        class Balok:
            def __init__(self, panjang, lebar, tinggi):
                self.panjang = panjang
                self.lebar = lebar
                self.tinggi = tinggi 
            def Volume(self):
                return self.panjang * self.lebar * self.tinggi
        VolumeBalok = Balok(10,15,20)
        print('Volume Balok : ',VolumeBalok.panjang,' x ',VolumeBalok.lebar, ' x ',VolumeBalok.tinggi,' = ',VolumeBalok.Volume())
        
    elif perintah == 2 :
        class Kubus:
              def __init__(self, rusuk):
                self.rusuk = rusuk
              def Volume(self):
                return self.rusuk * self.rusuk * self.rusuk
        VolumeKubus = Kubus(10)
        print('Volume Balok :',VolumeKubus.rusuk, ' x ', VolumeKubus.rusuk, ' x ',VolumeKubus.rusuk, ' = ',VolumeKubus.Volume())

    elif perintah == 3 :
        class Tabung:
              def __init__(self, r, tinggi):
                self.r = r
                self.tinggi = tinggi
              def Volume(self):
                return 3.14 * self.r * self.r * self.tinggi
        VolumeTabung = Tabung(5, 10)
        print('Volume Tabung : ','3,14',' x ',VolumeTabung.r,' x ',VolumeTabung.r, ' x ',VolumeTabung.tinggi,' = ',VolumeTabung.Volume())

    else:
        x = input('Maaf yang anda masukkan tidak terdefenisi')
        
    x =input('\nMau menghitung lagi ? pilih Y jika Ya, dan pilih N jika Tidak (Y/N) = ')
    if x == 'N':
        print('\nTerima Kasih')
        break







   
