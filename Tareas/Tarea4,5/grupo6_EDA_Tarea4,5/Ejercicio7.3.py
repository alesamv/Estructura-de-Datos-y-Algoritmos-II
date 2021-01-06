cont=1
name=input("Introduzca el nombre del archivo: ")

if(name=='na na boo boo'):
	print("\nNA NA BOO BOO PARA TI - ¡Te he pillado!")
	exit()
try:
	manf=open(name)
except:
	print("\nNo se pudo abrir el fichero: ",name)
	exit()

for linea in manf:
	cont+=1
manf.close()

print("\nHay {0} lineas en el fichero.".format(cont))

