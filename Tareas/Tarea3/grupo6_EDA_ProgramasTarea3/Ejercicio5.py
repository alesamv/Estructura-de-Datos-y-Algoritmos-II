def imprimedos(cadena):
  print ("\nLos dos primeros caracteres son: ",cadena[0],cadena[1])
  
def ultimostres(cadena):
  print("\nLos ultimos tres caracteres son: ",cadena[-3],cadena[-2],cadena[-1])
  
def cddos(cadena):
  print("\nImprimiendo cada dos caracteres: ")
  for i in range(0,len(cadena)):
    if i%2 == 0:
      print(cadena[i],end=' ')
  
def invertir(cadena):
  print("\nLa cadena invertida es: ", cadena[::-1])

def dossentidos(cadena):
  print("\nLa cadena en dos sentidos: ",cadena+cadena[::-1])
  


cadena = (input("Ingresa una cadena: "))
imprimedos(cadena)
ultimostres(cadena)
cddos(cadena)
invertir(cadena)
dossentidos(cadena)