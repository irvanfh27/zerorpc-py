import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")

print c.tambah(4 , 5)
print c.perkalian(5 , 5)