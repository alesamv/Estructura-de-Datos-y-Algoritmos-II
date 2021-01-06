name=input("Introduzca el nombre del archivo: ")
try:
	manf=open(name)
except:
	print("No se pudo abrir el fichero: ",name)
	exit()

for linea in manf:
	palabras = linea.split()
	if len(palabras) != 0 and palabras[0] == 'From':
		print (palabras[2])
	


