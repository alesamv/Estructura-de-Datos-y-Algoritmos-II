def operaciones(n):
  sum = 0
  prom = 0
  while n != -1 :
    num.append(n)
    sum = sum + n
    n = int(input("Ingresa un numero: "))
  prom = sum/len(num)
  print("La cantidad de numeros fue: ",len(num), ",y son: ",num)
  print("La suma es: ",sum)
  print("El promedio es: ", prom)
  
n = 0
num =[]
n = int(input("Ingresa un numero: "))
if n == -1:
  print("No hay numeros introducidos")
else:
  operaciones(n)