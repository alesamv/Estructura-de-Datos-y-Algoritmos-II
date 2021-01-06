def main():
  factor1 = 1
  respuesta= 'si'
  num = int(input("Ingresa un numero: "))
  while factor1<=10:
    factor2 = num * factor1
    print(factor2)
    factor1 = factor1 + 1
  op=input("¿Otro numero a generar tabla de multiplicar?")
  if op == respuesta:
    main()

main()
