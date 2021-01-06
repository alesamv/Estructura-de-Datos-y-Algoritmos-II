def millares(cadena):
  str(cadena)
  cadena = cadena[::-1]
  ncadena = [cadena[i:i+3][::-1] for i in range(0,len(cadena),3) if (cadena[i:i+3])]
  ncadena = ncadena[::-1]
  cadena = str.join(",", ncadena)
  print("La cadena es: ",cadena)
  
num = input("Ingrese una cadena de numeros: ")
millares(num)