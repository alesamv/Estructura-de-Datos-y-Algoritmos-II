def calculo_salario(horas, tarifa):
  if horas >= 40:
    horasext = horas - 40
    tarifaext = tarifa/2
    salario = (horas * tarifa)+(horasext*tarifaext)
    print("El salario es: ",salario)
  else:  
    salario = horas * tarifa
    print("El salario es: ",salario)
  
horas = float (input("Introduzca las horas: "))
tarifa = float(input("Introduzca la tarifa por hora: "))
calculo_salario(horas,tarifa)