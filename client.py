import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")

x = int(input("Masukkan angka pertama: "))
y = int(input("Masukkan angka kedua: "))
print("1.tambah\n2.kurang\n3.Pembagian\n4.Perkalian")
op = int(input("Pilih Perhitungan: "))

print(c.calc(x, y, op))
