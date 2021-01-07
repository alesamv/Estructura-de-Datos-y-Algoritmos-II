def es_potencia(n,b):
	comp=1
	while (comp<b):
		comp*=n
	if comp==b:
		resultado=True
	else:
		resultado=False
	return resultado

print("-->Examen1 - Ejercicio5<--\n")
n=int(input("Introduce un número: "))
b=int(input("Introduce el número que se desea saber si es potencia de: {0}".format(n)))
resultado=es_potencia(n,b)
if(resultado):
	print("\n>> {0} << \nEl {1} es potencia de {2}.".format(resultado,b,n))
else:
	print("\n>> {0} << \nEl {1} no es potencia de {2}.".format(resultado,b,n))