import zerorpc
import func2


s = zerorpc.Server(func2)
s.bind("tcp://0.0.0.0:4445")
s.run()