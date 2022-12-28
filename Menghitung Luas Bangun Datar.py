

print('''NAMA  : NURUL HIDAYAH
NIM   : D0221374
KELAS : INFORMATIKA H
________________________\n''')
print('''===== MENGHITUNG LUAS BANGUN RUANG =====''')
while True:
    print('''

Silahkan pilih perintah dibawah ini :
1. Luas Persegi
2. Luas Lingkaran
3. Luas segitiga\n''')
    perintah = int(input('Masukkan : '))
    if perintah == 1:              
        class Persegi:
            def __init__(self, panjang, lebar):
                self.panjang = panjang
                self.lebar = lebar
            def get_luas(self):
                return self.panjang * self.lebar
        LuasPersegi = Persegi(15,2)
        print('Luas persegi : ',LuasPersegi.panjang, ' x ',LuasPersegi.lebar,' = ',LuasPersegi.get_luas(),'cm')
        
    elif perintah == 2 :
        class Lingkaran:
              def __init__(self, phi, r):
                self.phi = phi
                self.r = r
              def get_luas(self):
                return self.phi * self.r * self.r
        LuasLingkaran = Lingkaran(3.14, 10)
        print('Luas lingkaran:',LuasLingkaran.phi, ' x ', LuasLingkaran.r, ' x ',LuasLingkaran.r, ' = ', LuasLingkaran.get_luas(),'cm')

    elif perintah == 3 :
        class Segitiga:
              def __init__(self, alas, tinggi):
                self.alas = alas
                self.tinggi = tinggi
              def get_luas(self):
                return 0.5 * self.alas * self.tinggi
        LuasSegitiga = Segitiga(5, 10)
        print('luas segitiga:','0.5 ',LuasSegitiga.alas, ' x ', LuasSegitiga.tinggi,' = ', LuasSegitiga.get_luas(),'cm')

    else:
        print('Perintah tidak sesuai')
        break







   
