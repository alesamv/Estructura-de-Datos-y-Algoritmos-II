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
	for i in range(math.ceil(tamanoHeap/2) -1,0,-1):
		MaxHeapify(A,i,tamanoHeap)
		
def OrdemacioHeapSort(A,tamanoHeap):
	construirHeapMaxIni(A,tamanoHeap)
	for i in range(len(A[1:]),1,-1):
		intercambia(A,1,i)
		tamanoHeap=tamanoHeap-1
		MaxHeapify(A,1,tamanoHeap)

A =[0,9,21,4,40,10,35]
print("Arreglo desordenado: ",A[1:])
tiempoi = clock()
OrdemacioHeapSort(A,len(A)-1)
tiempof = clock()
print("Arreglo ordenado: ",A[1:])
print("Tiempo de ejecucion: " ,(tiempof - tiempoi))