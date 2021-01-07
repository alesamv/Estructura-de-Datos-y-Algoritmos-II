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
        

A=[]
B=[]
C=[]
for i in range(501,-1,-1):
    A.append(i)
for i in range(201,-1,-1):
    B.append(i)
for i in range(101,-1,-1):
    C.append(i)

print ("Lista desordenada: {0} ".format(A[1:]))
tiempoi = clock()
QuickSort(A,1,len(A)-1)
tiempof = clock()
print("\n\nLa lista arreglada: {0} ".format(A[1:]))
print("\n\nEl tiempo de QuickSort es: {0} seg ".format((tiempof - tiempoi)))