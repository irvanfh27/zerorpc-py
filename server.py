import zerorpc
import func

 	

s = zerorpc.Server(func)
s.bind("tcp://0.0.0.0:4343")
s.run()