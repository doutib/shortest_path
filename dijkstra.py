import numpy as np

def dijkstra(s,Matrix,Neighbors,do_print=False):
	if do_print:
		n=Matrix.shape[0]
		inf=np.inf
		d=np.zeros(n)+inf
		d.itemset(s,0)
		U=np.zeros(n)
		U0=np.zeros(n)+inf
		u=s
		f= open('dijkstra'+str(s)+'.txt', 'w')
		while not((U == U0).all()) :
			f.write(" ".join(map(str, d)))
			f.write("\n")
			u = np.argmin(U+d)
			for v in Neighbors.item(u):
				d.itemset(v,np.minimum(d.item(v),d.item(u)+ Matrix.item((u,v))))
			U[u]= np.inf
		f.write(" ".join(map(str, d)))
		return d
	else :
		n=Matrix.shape[0]
		inf=np.inf
		d=np.zeros(n)+inf
		d.itemset(s,0)
		U=np.zeros(n)
		U0=np.zeros(n)+inf
		u=s
		while not((U == U0).all()) :
			u = np.argmin(U+d)
			for v in Neighbors.item(u):
				d.itemset(v,np.minimum(d.item(v),d.item(u)+ Matrix.item((u,v))))
			U[u]= np.inf
		return d


