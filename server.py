import zerorpc
import func

class Kalkulator(object):
 	
 	def tambah(self, x , y):
 		return x + y
 	def perkalian(self, a, b):
 		return a*b



s = zerorpc.Server(Kalkulator())
s.bind("tcp://0.0.0.0:4242")
s.run()