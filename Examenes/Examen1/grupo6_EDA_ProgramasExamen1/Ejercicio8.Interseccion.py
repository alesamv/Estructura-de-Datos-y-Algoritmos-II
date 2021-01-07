def interseccion(m1,b1,m2,b2):
  temp1 = m1 - m2  
  temp2 = b2 - b1  
  x = temp2/temp1
  y = (m1*x) + b1
  print("\n\n--->Coordenadas de intersección<---")
  print("x = {}\ny = {}".format(x,y))
  
print("-->Examen1 - Ejercicio 8<--")
print("Punto de intersección de una recta (y = mx+b)\n")
m1 = int(input("Ingrese la pendiente de la primer recta: "))
b1 = int(input("Ingrese la ordenada al origen de la primer recta: "))
m2 = int(input("\nIngrese la pendiente de la segunda recta: "))
while(m1 == m2):
  print("-->Las rectas son paralelas, por lo tanto nunca se intersectan.")
  m2 = int(input("Ingrese de nuevo la segunda pendiente: "))
b2 = int(input("Ingrese la ordenada al origen de la segunda recta: "))
interseccion(m1,b1,m2,b2)