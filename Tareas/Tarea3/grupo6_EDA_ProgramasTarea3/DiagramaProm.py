indice = 1
suma = 0

while indice <= 10:
  numero = int(input("Ingresa numero: "))
  suma = suma + numero
  indice = indice + 1

prom = suma/10
print("El promedio es: ",prom)