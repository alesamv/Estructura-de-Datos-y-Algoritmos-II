from time import clock
import math

def hIzq(i):
	return 2*i
	
def hDer(i):
	return 2*i+1
	
def intercambia(A,x,y):
	tmp = A[x]
	A[x] = A[y]
	A[y] = tmp
	
def MaxHeapify(A,i,tamanoHeap):
	L = hIzq(i)
	R = hDer(i)
	if (L <= tamanoHeap and A[L] > A[i]):
		posMax = L
	else:
		posMax = i

	if (R <= tamanoHeap and A[R] > A[posMax] ):
		posMax = R

	if (posMax != i):
		intercambia(A,i,posMax)
		MaxHeapify(A,posMax,tamanoHeap)
		
def construirHeapMaxIni(A,tamanoHeap):
	for i in range(int(math.ceil(tamanoHeap/2)) -1,0,-1):
		MaxHeapify(A,i,tamanoHeap)
		
def OrdemacioHeapSort(A,tamanoHeap):
	construirHeapMaxIni(A,tamanoHeap)
	for i in range(len(A[1:]),1,-1):
		intercambia(A,1,i)
		tamanoHeap=tamanoHeap-1
		MaxHeapify(A,1,tamanoHeap)


A=[]
B=[]
C=[]
for i in range(501,-1,-1):
	A.append(i)
for i in range(201,-1,-1):
	B.append(i)
for i in range(101,-1,-1):
	C.append(i)

print("Arreglo desordenado: {0} ".format(A[1:]))
tiempoi = clock()
OrdemacioHeapSort(A,len(A)-1)
tiempof = clock()
print("Arreglo ordenado: {0} ".format(A[1:]))
print("Tiempo de HeapSort es: {0} seg ".format((tiempof - tiempoi)))