import numpy as np

def fw(Matrix,Neighbors,do_print=False):
    n=Matrix.shape[0]
    D=np.zeros([n,n])+np.inf
    D1=np.zeros([n,n])
    for i in range(n):
        D.itemset((i,i),0)
        for j in Neighbors.item(i):
            D.itemset((i,j),Matrix.item((i,j)))
    while not((D1==D).all()):
        D1=np.array(D)
        for i in range(n):
            for j in range(n):
                D.itemset((i,j),np.minimum(D.item((i,j)),np.amin(D[i,:]+D[:,j])))
                #D.itemset((j,i),D.item((i,j)))

    if do_print :
        f= open('fw.txt', 'w')
        for d in range(len(D)-1):
            f.write(" ".join(map(str, D[d])))
            f.write("\n")
        d=d+1
        f.write(" ".join(map(str, D[d])))
        f.close()
    return D


