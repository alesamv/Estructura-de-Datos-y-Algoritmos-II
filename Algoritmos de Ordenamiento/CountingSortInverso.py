def CreaLista(k):
	L=[]
	for i in range(k+1):
		L.append(0)
	return L

def CountingSort(A,k):
	C=CreaLista(k)
	B=CreaLista(len(A)-1)
	for j in range(1,len(A)):
		C[A[j]]=C[A[j]]+1
	for i in range(k-1,0,-1):
		C[i]=C[i]+C[i+1]
	for j in range (len(A)-1,0,-1):
		B[C[A[j]]]=A[j]
		C[A[j]]=C[A[j]]-1
	return B
A=[0,9,21,4,40,10,35]
print("Lista desordenada: ",A[1:])
A=CountingSort(A,40)
print("Lista ordenada: ",A[1:])