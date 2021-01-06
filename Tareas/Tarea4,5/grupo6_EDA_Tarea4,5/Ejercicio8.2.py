def busqueda_lineal(lista,x):
	i=0
	for z in lista:
		if z==x:
			return i
		else:
			i+=1
	return -1

A=[1,4,54,3,0,-1]
print("Lista: ",A)
x=int(input("Elemento que desea buscar saber su posicion: "))
b=busqueda_lineal(A,x)
if(b>=0):
	print("El elemento se encuentra en la lista en el indice: ",b)
else:
	print("El elemento no se encuentra en la lista.")
	print(b)