import numpy as np

#Loading Data
with open("metroEdgeDist.txt", "r") as file:
    data = np.loadtxt(file, delimiter="\n",skiprows=1)
    n=304
    inf=np.inf
    Matrix = np.zeros([n,n])+inf
    d=0
    i=0
    while i < n :
    	for son in range(int(data.item(d))):
    		d=d+1
    		j=int(data.item(d))
    		d=d+1
    		dd=data.item(d)
    		Matrix[i][j]=dd
    	i=i+1
    	d=d+1


#Neighbors
Neighbors=[[] for i in range(n)]
for i in range(n):
    for j in range(n):
        if Matrix[i][j]<np.inf:
            Neighbors[i]=Neighbors[i]+[j]
Neighbors=np.array(Neighbors)
