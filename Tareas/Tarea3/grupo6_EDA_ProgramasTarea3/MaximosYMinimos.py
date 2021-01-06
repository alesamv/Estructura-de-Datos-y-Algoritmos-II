def maxymin(a,b,c):
  print("\nLa forma general es: {}x^2 {}x {} ".format(a,b,c))
  ad = 2*a
  print("Primera derivada: {}x {}".format(ad,b))
  print("Igualando a 0 y despejando x: 0 = {}x {}".format(ad,b))
  x = -b/ad
  print("El valor de x es: ",x)
  print("Introduciendo x en la función original: ")
  print("f({}) = {}({})^2 {}({}) {}".format(x,a,x,b,x,c))
  temp = (a*(x**2)) + (b*x) + c
  y = x/temp
  print("El valor de y es: ",y)
  if a>0:
    print("\n------>Valor minimo<-------")
    print("x = ",x, "\ny = ",y)
  else:
    print("\n------>Valor maximo<-------")
    print("x = ",x, "\ny = ",y)

print("--Encontrando maximos y minimos de un polinomio--")
a=int(input("Ingrese el coeficiente a: "))
while a == 0:
  a = int(input("Ingrese de nuevo a: "))
b=int(input("Ingrese el coeficiente b: "))
c=int(input("Ingrese el coeficiente c: "))
maxymin(a,b,c)