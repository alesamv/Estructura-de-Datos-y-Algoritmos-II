from time import clock
def intercambia (A,x,y):
    temp=A[x]
    A[x]=A[y]
    A[y]=temp
def particionar(A,p,r):
    x=A[r]
    i=p-1
    for j in range (p,r):
        if (A[j]<=x):
            i=i+1
            intercambia(A,i,j)
    intercambia(A,i+1,r)
    return i+1
def QuickSort(A,p,r):
    if(p<r):
        q=particionar(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)
        
A=[0,9,21,4,40,10,35]
print ("Lista desordenada: ",A)
tiempoi = clock()
QuickSort(A,1,6)
tiempof = clock()
print("\n\nLa lista arreglada: ",A)
print("\n\nEl tiempo de QuickSort es:",(tiempof - tiempoi))