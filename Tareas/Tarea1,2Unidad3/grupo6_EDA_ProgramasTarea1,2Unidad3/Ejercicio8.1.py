def recorta(A):
  A.pop(0)
  A.pop(len(A)-1)
  return None

def centro(A):
  del A[1:len(A)-1]
  return A

lista = [1,2,3,4,5,6,7,8,9]
print("--Ejercicio 8.1--\n")
print("Lista original: ",lista)
recorta(lista)
print("Borrando primer y último elemento de la lista: ", lista)
otLista = centro(lista)
print("Borrando centro de la lista ya modificada: ",otLista)