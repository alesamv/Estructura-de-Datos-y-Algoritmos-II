def vocales(cadena):
  print("Las vocales contenidas son: ", end = '')
  for i in range(0,len(cadena)):
    if cadena[i]=='a' or cadena[i] == 'e' or cadena[i] == 'i' or cadena [i] == 'o' or   cadena[i] == 'u':
      print(cadena[i], end = '')
      
def consonantes(cadena):
  print("\nLas consonantes contenidas son: ", end = '')
  for i in range(0,len(cadena)):
    if cadena[i] == 'b' or cadena[i] == 'c' or cadena[i] == 'd' or cadena [i] == 'f' or  cadena[i] == 'g' or cadena[i] == 'h' or cadena[i] == 'j' or cadena [i] == 'k'or cadena[i] == 'l'or cadena[i] == 'm' or cadena[i] == 'n'or cadena[i] == 'ñ' or cadena [i] == 'p' or cadena[i] == 'q' or cadena[i] == 'r' or cadena[i] == 's'or cadena [i] == 't'or  cadena[i] == 'v'or cadena[i] == 'w' or cadena[i] == 'x' or cadena[i] == 'y' or cadena [i] == 'z':
      print(cadena[i], end = '')
      
c = input("Ingresa cadena: ")
vocales(c)
consonantes(c)
