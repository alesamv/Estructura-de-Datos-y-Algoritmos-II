file=open("mail.txt")
diccionario=dict()
cont=0
for linea in file:
	cadena=linea.split()
	if cadena[0]=='From:':
		dominio=cadena[1].split("@")
		if dominio[1] not in diccionario:
			diccionario[dominio[1]]=1
		else:
			diccionario[dominio[1]]+=1
print("Lista de correos:")
print(diccionario)
