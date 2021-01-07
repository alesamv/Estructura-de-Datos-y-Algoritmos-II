from time import clock
def CreaLista(k):
	L = []
	for i in range (k+1):
		L.append(0)
	return L
def CountingSort(A,k):
	C = CreaLista(k)
	B = CreaLista(len(A)-1)
	for j in range(1,len(A)):
		C[A[j]] = C[A[j]]+1
	for i in range(1,k+1):
		C[i] = C[i]+C[i-1]
	for j in range(len(A)-1,0,-1):
		B[C[A[j]]] = A[j]
		C[A[j]] = C[A[j]]-1
	return B
def Cambia(B):
  for i in range(len(B)):
    B[i] = B[i]*(-1)
  return B
def CountingSortN(A,k):
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
def Negativos(A):
  for i in range(1,len(A)):
    if A[i] < 0:
      B.append(A[i])
    else:
      C.append(A[i])
  Cambia(B)
  return B
 
A=[]
B=[]
C=[]
for i in range(501,-1,-1):
	A.append(i)
for i in range(201,-1,-1):
	B.append(i)
for i in range(101,-1,-1):
	C.append(i)
print("Lista inicial: {0} ".format(A[1:]))
tiempoi=clock()
A=CountingSort(A,len(A))
tiempof=clock()
tiempo=(tiempof-tiempoi)
print("Lista ordenada: {0} ".format(A[1:]))
print("El tiempo de CountingSort es: {0} seg".format(tiempo))