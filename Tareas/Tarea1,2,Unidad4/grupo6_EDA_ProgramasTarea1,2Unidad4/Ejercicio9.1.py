file=open("words.txt")
diccionario=dict()
cont=0
for linea in file:
	cadena=linea.split()
	for i in cadena:
		if i not in diccionario:
			diccionario[i]=i
print(diccionario)
bus=input("Introduce la llave a la que quieres acceder al valor: ")
if bus in diccionario:
	print("El valor es:",diccionario[bus])
else:print("No se encontro la llave")