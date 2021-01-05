try:
  horas = float(input("Introduzca horas: "))
  try:
    tarifa = float(input("Introduzca tarifa: "))
    salario = horas * tarifa
    print("Salario = ",salario)
  except: 
    print("Error, introduzca un numero")
except:
  print("Error, introduzca un numero")