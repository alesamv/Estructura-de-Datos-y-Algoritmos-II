def replica(li, r):
    if not li:
        return li
    inicio = li[0:1]
    fin = li[1:]
    return (inicio * r) + replica(fin, r)

print("-->Examen1 - Ejercicio10<--\n")
lista = [1,3,3,7]
print("Lista original: ",lista)

newlist = replica(lista,2)
print("Nueva lista: ",newlist)