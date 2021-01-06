xdspam=[]
cspam=0
cemail=0

name=input("Introduzca el nombre del archivo: ")
try:
	manf=open(name)
except:
	print("No se pudo abrir el fichero: ",name)
	exit()

for linea in manf:
	if linea.startswith('X-DSPAM-Confidence:') :
		num =float(linea[slice(linea.find('.'),len(linea),1)])
		xdspam.append(num)
		cspam+=1
	if linea.startswith('Received'):
		cemail+=1
manf.close()

if(cemail!=0):
	probabilidad=cspam/cemail
	print("\nEn la bandeja hubo {0} coincidencias en los {1} emails totales.".format(cspam,cemail))
	print("Valor medio de probabilidad de spam :",probabilidad)
else:
	print("\nLa bandeja esta vacia.")
