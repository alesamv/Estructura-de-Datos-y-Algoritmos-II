def maxymin(a,b,c):
  ad = 2*a
  x = -b/ad
  y = (a*(x**2)) + (b*x) + c
  if a>0:
    print("\n------>Valor minimo<-------")
    print("x = ",x, "\ny = ",y)
  else:
    print("\n------>Valor maximo<-------")
    print("x = ",x, "\ny = ",y)

print("-->Examen1 - Ejercicio7<--\n")
print("Encontrando maximos o minimos de un polinomio (a(x)^2+b(x)+c)")
a=int(input("Ingrese el coeficiente a: "))
while a == 0:
  a = int(input("Ingrese de nuevo a: "))
b=int(input("Ingrese el coeficiente b: "))
c=int(input("Ingrese el coeficiente c: "))
maxymin(a,b,c)