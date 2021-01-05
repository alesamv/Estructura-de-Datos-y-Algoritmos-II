horas = float(input("Introduzca las horas: "))
tarifa = float(input("Introduzca la tarifa por hora: "))
if horas >= 40:
  vecesh = horas * 1.5
  vecest = tarifa * 1.5
  salario = (horas * tarifa) + (vecesh + vecest)
  print("Salario = ",salario)
else: 
  salario = horas * tarifa
  print("Salario = ",salario)