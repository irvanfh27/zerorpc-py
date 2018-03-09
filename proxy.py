import zerorpc


s1 = zerorpc.Client()
s1.connect("tcp://127.0.0.1:4343")
# server1

s2 = zerorpc.Client()
s2.connect("tcp://127.0.0.1:4445")
# server2

class Hitung(object):
    def calc(self, x, y, op): 
        if (op == 1): #tambah
            print "Memproses Penjumlahan -> Di Server 1"
            return s1.tambah(x,y)
        elif (op == 2): #kurang
            print "Memproses Pengurangan -> Di Server 1"
            return s1.kurang(x,y)
        elif (op == 3): #bagi
            print "Memproses Pembagian -> Di Server 2"
            return s2.pembagian(x,y)
        elif (op == 4): #kali
            print "Memproses Perkalian -> Di Server 2"
            return s2.perkalian(x,y)
        else:
            return 0     

s = zerorpc.Server(Hitung())
s.bind("tcp://0.0.0.0:4242")
s.run()
