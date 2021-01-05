try:
  puntuacion = float(input("Ingrese la puntuación entre 0 y 1: "))
  if puntuacion > 1 or puntuacion < 0:
    print("Puntuacion incorrecta")
  else:
    if puntuacion >= 0.9:
      print("Sobresaliente")
    elif puntuacion >= 0.8:
      print("Notable")
    elif puntuacion >= 0.7:
      print("Bien")
    elif puntuacion >= 0.6:
      print("Suficiente")
    elif puntuacion < 0.6:
      print("Insuficiente")
except:
  print("Puntuacion incorrecta")