numeros = []
suma = 0
op = input("Introducir numero?: ")
while op != 'fin':
  try:
    num = int(input("Introduce un numero: "))
    suma = suma + num
    numeros.append(num)
    op = input("Seguir? ")
    if op != 'si':
      print("Entrada invalida")
    else:
      pass
  except:
    print("Entrada invalida")

promedio = suma/len(numeros)  
print(suma, end='')
print(" ",len(numeros), end = " ")
print(" ",promedio)