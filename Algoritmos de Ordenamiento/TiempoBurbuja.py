from time import clock

def bubblesort(A):
	for i in range(1,len(A)):
		for j in range (len(A)-1):
			if A[j]>A[j+1]:
				aux= A[j]
				A[j]=A[j+1]
				A[j+1]=aux

A=[0,9,21,4,40,10,35]

print("Lista desordenada: ",A)
tiempoi=clock()
bubblesort(A)
tiempof=clock()

print("\n\nLa lista arreglada",A)
t=tiempof-tiempoi
print("\n\nEl tiempo de la Burbuja es: ",t)