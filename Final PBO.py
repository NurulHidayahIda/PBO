print('''NAMA  : NURUL HIDAYAH
NIM   : D0221374
KELAS : INFORMATIKA H
________________________\n
===== MENGHITUNG LUAS BANGUN DATAR & VOLUME BANGUN RUANG =====\n''')
x = 'Y'
while x == 'Y' :
    perintah = int(input('''Masukkan pilihan :
1. Luas Bangun Datar
2. Volume Bangun Ruang
=> '''))
    
    if perintah == 1:
        class Luas :
            def __init__(self,panjang,lebar,r,alas,tinggi):
                self.panjang = panjang
                self.lebar = lebar
                self.r = r
                self.alas = alas
                self.tinggi = tinggi

            def LuasPersegi(self):
                return self.panjang * self.lebar
            def LuasLingkaran(self):
                return 3.14 * self.r * self.r
            def LuasSegitiga(self):
                return 0.5 * self.alas * self.tinggi
        LuasBangunDatar = Luas(8,8,4,5,10)
        Persegi = LuasBangunDatar.LuasPersegi()
        Lingkaran = LuasBangunDatar.LuasLingkaran()
        Segitiga = LuasBangunDatar.LuasSegitiga()
        print ('Luas Persegi : ',LuasBangunDatar.panjang,' x ', LuasBangunDatar.lebar, ' = ',Persegi)
        print ('Luas Lingkaran : ','3,14', ' x ',LuasBangunDatar.r,' x ',LuasBangunDatar.r,' = ',Lingkaran)
        print ('Luas Segitiga : ','0,5 ', 'x ',LuasBangunDatar.alas, ' x ',LuasBangunDatar.tinggi,' = ',Segitiga)
        
    elif perintah == 2 :
        class Volume :
            def __init__(self,rusuk,panjang,lebar,tinggi,r):
                self.rusuk = rusuk
                self.panjang = panjang
                self.lebar = lebar
                self.tinggi = tinggi
                self.r = r

            def VolumeKubus (self):
                return self.rusuk * self.rusuk * self.rusuk
            def VolumeBalok (self):
                return self.panjang * self.lebar * self.tinggi
            def VolumeTabung (self) :
                return 3.14 * self.r * self.r * self.tinggi
        VolumeBangunRuang = Volume(10,8,15,20,5)
        Kubus = VolumeBangunRuang.VolumeKubus()
        Balok = VolumeBangunRuang.VolumeBalok()
        Tabung = VolumeBangunRuang.VolumeTabung()
        print('Volume Kubus : ',VolumeBangunRuang.rusuk,' x ',VolumeBangunRuang.rusuk,' x ',VolumeBangunRuang.rusuk, ' = ',Kubus)
        print('Volume Balok : ',VolumeBangunRuang.panjang,' x ',VolumeBangunRuang.lebar,' x ',VolumeBangunRuang.tinggi,' = ',Balok)
        print('Volume Tabung : ','3,14',' x ',VolumeBangunRuang.r,' x ',VolumeBangunRuang.r, ' x ',VolumeBangunRuang.tinggi,' = ',Tabung)

    else :
        x = input('Maaf yang anda masukkan tidak terdefenisi')
        
    x =input('\nMau menghitung lagi ? pilih Y jika Ya, dan pilih N jika Tidak (Y/N) = ')
    if x == 'N':
        print('\nTerima Kasih')
        break

            
