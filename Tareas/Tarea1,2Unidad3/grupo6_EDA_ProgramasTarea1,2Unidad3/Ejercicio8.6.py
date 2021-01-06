try:
  nums= []
  num = int(input("Introduzca un numero: "))
  while True:
    num = int(input("Introduzca un numero: "))
    nums.append(num)
except:
  print("El Maximo es: ",max(nums))
  print("El Minimo es: ",min(nums))