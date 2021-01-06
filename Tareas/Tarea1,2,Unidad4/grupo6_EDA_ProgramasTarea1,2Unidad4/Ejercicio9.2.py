file=open("mail.txt")
diccionario=dict()
cont=0
for linea in file:
	cadena=linea.split()
	if cadena[0]=='From:':
		if cadena[2] not in diccionario:
			diccionario[cadena[2]]=1
		else:
			diccionario[cadena[2]]+=1
print("Lista de correos:")
print(diccionario)
