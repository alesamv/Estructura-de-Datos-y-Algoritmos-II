def max(a,b):
  while a == b:
      print("Son iguales, vuelve a intentar")
      a= int(input("Primer numero: "))
      b= int(input("Segundo numero: "))
          
  if a > b:
      print("El numero mayor es:",a)
    
  else:
      print("El numero mayor es:",b)

print("Introduce dos numeros")
a= int(input("Primer numero: "))
b= int(input("Segundo numero: "))
max(a,b)
