def interseccion(m1,b1,m2,b2):
  print("Recta 1: y = {}x {}\nRecta 2: y = {}x {}".format(m1,b1,m2,b2))
  print("Igualamos ecuaciones: {}x {} = {}x {}".format(m1,b1,m2,b2))
  temp1 = m1 - m2  
  temp2 = b2 - b1  
  x = temp2/temp1
  print("El valor de x es: ",x)
  print("Reemplazando el valor de x en alguna ecuación: y = {}({}) {}".format(m1,x,b1))
  y = (m1*x) + b1
  print("El valor de y es: ",y)
  print("\n\n--->Coordenadas de intersección<---")
  print("x = {} y = {}".format(x,y))
  
print("--Encontrando el punto de intersección de una recta (y = mx+b)--\n")
m1 = int(input("Ingrese la pendiente de la primer recta: "))
b1 = int(input("Ingrese la ordenada al origen de la primer recta: "))
m2 = int(input("Ingrese la pendiente de la segunda recta: "))
b2 = int(input("Ingrese la ordenada al origen de la segunda recta: "))
if m1 == m2:
  print("Las rectas son paralelas, por lo tanto nunca se intersectan.")
else: 
  interseccion(m1,b1,m2,b2)