def main():
	n=0
	suma=0
	cuenta=0
	acumula=0
	
	op=input("Desea ingresar calificacion (s/n): ")

	while (op != 'n'):
		n=float(input("Ingrese calificacion: "))
		cuenta=cuenta+1
		acumula=acumula+n
		op=input("Desea ingresar calificacion (s/n): ")
		pass
	promedio=acumula/cuenta
	print("El promedio es: {0} ".format(promedio))

main()
