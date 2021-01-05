def max_de_tres(a,b,c):
  if a > b  and a > c:
    print("El numero mayor es:",a)
    
  elif b > a and b >c:
    print("El numero mayor es:",b)

  else:
    print("El numero mayor es:",c)


a= int(input("Primer numero: "))
b= int(input("Segundo numero: "))
c= int(input("Tercer numero: "))
max_de_tres(a,b,c)