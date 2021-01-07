import math

#Algoritmo de ordenamiento
def intercambia(A,x,y):
	temp = A[x]
	A[x] = A[y]
	A[y] = temp

def particionar(A,p,r):
	x = A[r]
	i = p - 1
	for j in range(p,r):
		if(A[j] <= x):
			i = i + 1
			intercambia(A,i,j)
	intercambia(A,i+1,r)
	return i + 1

def QuickSort(A,p,r):
	if(p < r):
		q = particionar(A,p,r)
		QuickSort(A,p,q-1)
		QuickSort(A,q+1,r)

#Algoritmo de Busqueda Binaria
def BusquedaBinaria(A,x,izquierda,derecha):
	if izquierda > derecha:
		return -1
	medio = math.floor((izquierda + derecha)/2)

	if A[medio] == x:
		print("Se encontro en el indice: ",medio)

	elif A[medio] < x:
		return BusquedaBinaria(A,x,medio +1, derecha)
	else:
		return BusquedaBinaria(A,x,izquierda, medio-1)

print("-->Ejercicio 12<--\n")
lista = [5,4,3,2,6,9,8,1,7]
print("Lista desordenada: ",lista)
QuickSort(lista,0,8)
print("Lista ordenada: ",lista)
x = int(input("\nIngresa el valor a buscar en la lista: "))
BusquedaBinaria(lista,x,0,8)

