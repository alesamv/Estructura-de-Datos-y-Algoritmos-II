def maxNum(L,j):
  if j>0:
    return max(L[j], maxNum(L, j-1))
  else:
    return L[0]

print("-->Examen1 - Ejercicio9<--\n")
lista=[1,2,-7,6,-3,9,4,5,8,0]
num =maxNum(lista,9)
print(lista)
print("\nEl numero mayor de la lista es: ",num)