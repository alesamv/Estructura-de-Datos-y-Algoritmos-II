from time import clock

def bubblesort(A):
	for i in range(1,len(A)):
		for j in range (len(A)-1):
			if A[j]>A[j+1]:
				aux= A[j]
				A[j]=A[j+1]
				A[j+1]=aux


a=[]
b=[]
c=[]
for i in range(500,-1,-1):
	a.append(i)
for i in range(200,-1,-1):
	b.append(i)
for i in range(100,-1,-1):
	c.append(i)

print("Lista desordenada: {0} ".format(a))
tiempoi=clock()
bubblesort(a)
tiempof=clock()

print("\n\nLa lista arreglada: {0} ".format(a))
t=tiempof-tiempoi
print("\n\nEl tiempo de la Burbuja es: {0} seg".format(t))