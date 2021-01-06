name = input("Introduzca el nombre del fichero: ")
try:
	manf=open(name)
except:
	print("No se pudo abrir el fichero: ",name)
	exit()

lista = []
for linea in manf:
	palabras = linea.split()
	for i in palabras:
		if i not in lista:
			lista.append(i)
	
print("\n\nImprimiendo lista: \n",lista)
lista.sort()
print("\n\nLista ordenada: \n",lista)

