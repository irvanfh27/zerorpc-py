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
            return s1.tambah(x,y)
        elif (op == 2): #kurang
            return s1.kurang(x,y)
        elif (op == 3): #bagi
            return s2.pembagian(x,y)
        elif (op == 4): #kali
            return s2.perkalian(x,y)
        else:
            return 0

s = zerorpc.Server(Hitung())
s.bind("tcp://0.0.0.0:4242")
s.run()
