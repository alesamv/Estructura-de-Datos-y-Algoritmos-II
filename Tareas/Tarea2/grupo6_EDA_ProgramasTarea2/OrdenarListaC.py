from time import clock
def CrearSubArreglo(listaC, indIzq, indDer):
  return listaC[indIzq:indDer+1]

def Merge(listaC,p,q,r):
  Izq = CrearSubArreglo(listaC,p,q)
  Der = CrearSubArreglo(listaC,q+1,r)
  i = 0
  j = 0
  for k in range(p,r+1):
    if (j >= len(Der)) or (i < len(Izq) and Izq[i] < Der[j]):
      listaC[k] = Izq[i]
      i = i + 1
    else:
      listaC[k] = Der[j]
      j = j + 1

def MergeSort(listaC,p,r):
  if r - p > 0:
    q = int((p+r)/2)
    MergeSort(listaC,p,q)
    MergeSort(listaC,q+1,r)
    Merge(listaC,p,q,r)

listaA = []
listaB = []
listaC = []
for i in range(11):
  n = int(input("Inserte un elemento: "))
  listaA.append(n)
print("La lista 1 contiene los siguientes elementos: ",listaA)
for i in range(11):
  n= int(input("Inserte un elemento: "))
  listaB.append(n)
print("La lista 2 contiene los siguientes elementos: ",listaB)
listaC = listaA + listaB
print("La nueva lista contiene los siguientes elementos: ",listaC)
tiempoi = clock()
MergeSort(listaC, 0, 21)
tiempof = clock()
print("La lista ordenada es: ",listaC)
print("Tiempo de ejecución: ",(tiempof-tiempoi))
