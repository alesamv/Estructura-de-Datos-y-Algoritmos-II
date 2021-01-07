def MergeSort(A,p,r):
	if r-p>0:
		q=int((r-p)/3)+p
		q2=int(((r-p)/3)*2)+p
		MergeSort(A,p,q)
		MergeSort(A,q+1,q2)
		MergeSort(A,q2+1,r)
		Merge(A,p,q,q2,r)
	
def CrearSubArreglo(A, indIzq,indDer):
	return A[indIzq:indDer+1]

def Merge(A,p,q,q2,r):
	Izq=CrearSubArreglo(A,p,q)
	Cen=CrearSubArreglo(A,q+1,q2)
	Der=CrearSubArreglo(A,q2+1,r)
	i=0
	j=0
	B=Izq+Cen+Der
	print(B)
	if len(Cen)==0:	
		for k in range (p,q+2):
			if(j>=len(Der)) or (i< len(Izq) and Izq[i]< Der[j]):
				A[k]=Izq[i]
				i= i+1
			else:
				A[k]= Der[j]
				j=j+1
	else:
		for l in range(0,len(Izq)):

			for m in range(0,len(Cen)):
				if(Cen[m]<Izq[l]):
					temp=Cen[m]
					Cen[m]=Izq[l]
					Izq[l]=temp
			for m in range(0,len(Der)):
				if(Der[m]<Izq[l]):
					temp=Der[m]
					Der[m]=Izq[l]
					Izq[l]=temp
		for l in range(0,len(Cen)):
			for m in range(0,len(Der)):
				if(Der[m]<Cen[l]):
					temp=Der[m]
					Der[m]=Cen[l]
					Cen[l]=temp
		for l in range(0,len(Der)-1):
			for m in range(l,len(Der)):
				if(Der[m]<Der[l]):
					temp=Der[m]
					Der[m]=Der[l]
					Der[l]=temp

		B=Izq+Cen+Der
		j=0
		for i in range(p,r+1):

			A[i]=B[j]
			j+=1
	print("{0}    {1}    {2}\n".format(Izq,Cen,Der))

A=[10,9,8,7,6,5,4,3,2,1,0]
print("Lista original",A)
MergeSort(A,0,len(A)-1)

print("Lista ordenada: ",A)