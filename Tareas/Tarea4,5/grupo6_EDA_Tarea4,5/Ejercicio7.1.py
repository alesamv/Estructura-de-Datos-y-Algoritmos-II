name=input("Introduzca el nombre del archivo: ")
try:
	manf=open(name)
except:
	print("No se pudo abrir el fichero: ",name)
	exit()

print("\n>>\n\n")
for linea in manf:
	linea = linea.rstrip()
	print (linea.upper())
manf.close()
print("\n<<")

