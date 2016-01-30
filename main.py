import numpy as np
import time

from data import Matrix,Neighbors,n
from dijkstra import dijkstra
from bf import bf
from fw import fw

def run(do_print):
		f = open('runtime.txt', 'w')
		print('Run dijkstra ...')
		# dijkstra
		t0=time.clock()
		for i in range(n):
			dijkstra(i,Matrix,Neighbors,do_print=do_print)
		td=time.clock() - t0
		print('Run bf ...')
		# bf
		t0=time.clock()
		for i in range(n):
			bf(i,Matrix,Neighbors,do_print=do_print)
		tf=time.clock() - t0
		print('Run fw ...')
		# fw
		t0=time.clock()
		fw(Matrix,Neighbors,do_print=do_print)
		tw=time.clock() - t0
		# print
		td=td/(n*n)
		tf=tf/(n*n)
		tw=tw/(n*n)
		f.write('Dijkstra: '+str(td)+' seconds\n')
		f.write('Bellman-Ford: '+str(tf)+' seconds\n')
		f.write('Floyd-Warshall: '+str(tw)+' seconds')
		f.close()



