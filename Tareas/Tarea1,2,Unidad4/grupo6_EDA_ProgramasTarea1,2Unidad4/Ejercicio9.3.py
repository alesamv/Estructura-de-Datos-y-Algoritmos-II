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
print("Lista de correos:")
print(diccionario)
