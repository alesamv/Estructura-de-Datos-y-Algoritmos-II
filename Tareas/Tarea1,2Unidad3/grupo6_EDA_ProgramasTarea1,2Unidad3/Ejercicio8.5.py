name=input("Introduzca el nombre del archivo: ")
try:
	manf=open(name)
except:
	print("No se pudo abrir el fichero: ",name)
	exit()

cont = 0
for linea in manf:
	if linea.startswith('From: '):
		linea = linea.split()
		print(linea[1])
		cont+=1

print("Hay {} lineas con la palabra From al inicio.".format(cont))

