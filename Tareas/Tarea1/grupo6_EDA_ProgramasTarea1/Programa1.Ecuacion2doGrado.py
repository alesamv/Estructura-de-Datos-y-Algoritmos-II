import math
print("Solucion a una ecuación de 2do grado")
a = int(input("Ingrese a: "))
while a == 0:
  a = int(input("a no puede ser 0, ingrese de nuevo: "))
  
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))

d = ((b*b)-(4*a*c))

if d > 0 :
  x1 = ((-b) + math.sqrt(d))/(2*a)
  x2 = ((-b) - math.sqrt(d))/(2*a)
  print("X1 = ",x1, "X2 = ", x2)

else:
  if d == 0:
    x = (-b)/(2*a)
    print ("Solo existe una solución:")
    print("x= ",x)
  else:
    d = -d
    xr = (-b)/(2*a)
    xi = math.sqrt(d)/(2*a)
    print("Existen raices imaginarias:")
    print("x1 = ", xr,"+",xi,"i")
    print("x2= ",xr,"-",xi,"i")
    