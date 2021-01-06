print("--Ejercicio 6.1--\n")
fruta = 'banana'
print("Cadena original: ",fruta)
i = len(fruta)-1
while i >= 0:
	letra = fruta[i]
	print(letra)
	i-=1


print("\n\n--Ejercicio 6.2--\n")
print(fruta[:])
print("El significado de fruta[:] es la cadena completa.")


print("\n\n--Ejercicio 6.3--\n")
def contador(palabra,a):
	contador = 0
	for letra in palabra:
		if letra == a:
			contador = contador + 1
	print("En la cadena \"{0}\" hay: {1} {2}´s".format(palabra,contador,a))
contador(fruta,'a')


print("\n\n--Ejercicio 6.4--\n")
print("Usando el metodo count en ",fruta)
print("Count para 'a' = ",fruta.count('a'))


print("\n\n--Ejercicio 6.5--\n")
cad = 'X-DSPAM-Confidence: 0.8475'
print("Cadena original: ",cad)
num =float(cad[slice(cad.find('.'),len(cad),1)])
print("El valor floatante extraido: ", num)


print("\n\n--Ejercicio 6.6--\n")
str1 = "0000000Cadena de ejemplo0000000";
print("Strip\nCadena original: ",str1)
print("Despues de usar Strip:",str1.strip( '0' ))
str2 = "Los perros y amigos felices cantaban";
print("\nReplace\nCadena original: ",str2)
print("Despues del replace total:",str2.replace('o','a'))
print("Despues del replace parcial:",str2.replace('o','a',2))