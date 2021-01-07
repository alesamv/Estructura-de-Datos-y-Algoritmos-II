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
 
B=[0]   
C=[0]
A = [0,-9,-21,4,40,-10,35]
print("Lista inicial: ",A[1:])
Negativos(A)
B = CountingSortN(B,21)
Cambia(B)
print("Acomodando negativos: ",B[1:])
C = CountingSort(C,40)
print("Acomodando positivos: ",C[1:])
print("Lista ordenada: ",B[1:]+C[1:])