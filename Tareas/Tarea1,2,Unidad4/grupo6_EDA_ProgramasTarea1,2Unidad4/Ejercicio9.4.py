file=open("mail.txt")
diccionario=dict()
cont=0
for linea in file:
	cadena=linea.split()
	if cadena[0]=='From:':
		if cadena[1] not in diccionario:
			diccionario[cadena[1]]=1
		else:
			diccionario[cadena[1]]+=1

mayor = None
for valor in diccionario:
	if mayor is None or valor > mayor :
		mayor = valor

print ("El correo: ",mayor,"tiene ",diccionario[mayor], "mensajes")
