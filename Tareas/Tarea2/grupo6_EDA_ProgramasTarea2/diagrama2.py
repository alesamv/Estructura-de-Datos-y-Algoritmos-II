def main():
	op=int(input("Desea hacer un registro? \nPresione 1 para hacerlo, presione cualquier tecla para salir: "))
	if (op == 1):
		nota=int(input("Ingrese Nota: "))
		if(nota>=19 and nota<=20):
			print("Nueva nota = A")
			main()
		elif(nota>=16 and nota<=18):
			print("Nueva nota = B")
			main()
		elif(nota>=13 and nota<=15):
			print("Nueva nota = C")
			main()
		elif(nota>=10 and nota<=12):
			print("Nueva nota = D")
			main()
		elif(nota>=1 and nota<=9):
			print("Nueva nota = E")
			main()
  
main()