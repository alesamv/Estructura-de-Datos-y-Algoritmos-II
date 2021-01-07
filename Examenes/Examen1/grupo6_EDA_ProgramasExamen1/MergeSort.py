from time import clock


def CrearSubArreglo(A, indIzq,indDer):
	return A[indIzq:indDer+1]

def Merge(A,p,q,r):
	Izq=CrearSubArreglo(A,p,q)
	Der=CrearSubArreglo(A,q+1,r)
	i=0
	j=0
	for k in range (p,r+1):
		if(j>=len(Der)) or (i< len(Izq) and Izq[i]< Der[j]):
			A[k]=Izq[i]
			i= i+1
		else:
			A[k]= Der[j]
			j=j+1

def MergeSort(A,p,r):
	if r-p>0:
		q=int((p+r)/2)
		MergeSort(A,p,q)
		MergeSort(A,q+1,r)
		Merge(A,p,q,r)


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
MergeSort(a,0,len(a)-1)
tiempof=clock()

print("\n\nLa lista arreglada: {0} ".format(a))
t=tiempof-tiempoi
print("\n\nEl tiempo de MergeSort es: {0} seg ".format(t))