notas = []
sum = 0
prom = 0
op = int(input("1.Ingresar nota \nPresione cualquier numero para salir...\n"))

while op == 1:
  n = int(input("Ingrese nota: "))
  notas.append(n)
  sum = sum + n
  prom = sum/len(notas)
  print("El promedio es: ",prom)
  op = int(input("1.Ingresar nota \nPresione cualquier numero para salir...\n"))