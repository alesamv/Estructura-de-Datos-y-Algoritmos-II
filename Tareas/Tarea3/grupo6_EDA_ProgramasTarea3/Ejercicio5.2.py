numeros = []
suma = 0
op = input("Introducir numero?: ")
while op != 'fin':
  try:
    num = int(input("Introduce un numero: "))
    numeros.append(num)
    op = input("Seguir? ")
    if op != 'si':
      print("Entrada invalida")
    else:
      pass
  except:
    print("Entrada invalida")

mayor = None
for i in numeros:
  if mayor is None or i > mayor :
    mayor = i
print ('Mayor:', mayor)
menor = None
for i in numeros:
  if menor is None or i < menor:
    menor = i
print ('Menor:', menor)