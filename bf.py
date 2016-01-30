import numpy as np

def bf(s,Matrix,Neighbors,do_print=False):
	if do_print :
		n=Matrix.shape[0]
		d=np.zeros(n)+np.inf
		d.itemset(s,0)
		d1=np.zeros(n)+np.inf
		f= open('bf'+str(s)+'.txt', 'w')
		while not((d==d1).all()) :
		#for i in range(n):
			d1=np.array(d)
			f.write(" ".join(map(str, d)))
			f.write("\n")
			for t in range(n):
				for v in Neighbors.item(t):
					d.itemset(v,np.minimum(d.item(t)+Matrix.item(t,v),d.item(v)))
		f.write(" ".join(map(str, d)))
		return d
	else :
		n=Matrix.shape[0]
		d=np.zeros(n)+np.inf
		d.itemset(s,0)
		d1=np.zeros(n)+np.inf
		if do_print :
			f= open('bf'+str(s)+'.txt', 'w')
		while not((d==d1).all()) :
			d1=np.array(d)
			for t in range(n):
				for v in Neighbors.item(t):
					d.itemset(v,np.minimum(d.item(t)+Matrix.item(t,v),d.item(v)))
		return d
