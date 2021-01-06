def buscar_con_index(xs,x):
	if x in xs:
		return(xs.index(x))
	else:
		return -1

A=[1,4,54,3,0,-1]
print("Lista: ",A)
x=int(input("Introduzca el elemento que busca saber su posicion: "))
b=buscar_con_index(A,x)
if(b>=0):
	print("El elemento se encuentra en la lista en el indice: ",b)
else:
  print("El elemento no se encuentra en la lista")
  print(b)


