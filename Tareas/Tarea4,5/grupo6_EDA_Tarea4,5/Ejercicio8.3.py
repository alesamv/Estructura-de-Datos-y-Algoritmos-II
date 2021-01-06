def busqueda_binaria(lista,x):
	print("Lista",lista)
	izq=0
	der=len(lista)-1
	while izq <= der:
		medio=int((izq+der)/2)
		print("DEBUG: Izq:{0} der:{1} medio:{2}".format(izq,der,medio))

		if lista[medio]==x:
			return medio
		elif lista[medio]>x:
			der=medio-1
		else: 
			izq=medio+1
	return -1

def main():
	lista=input("Dame una lista ordenada([[]] para terminar: ")
	while lista != '[[]]':
		x=input("¿Valor buscado?:")
		resultado=busqueda_binaria(lista[1:len(lista)-1:2],x)
		print("Resultado:",resultado)
		lista=input("Dame una lista ordenada([[]] para terminar: ")

main()