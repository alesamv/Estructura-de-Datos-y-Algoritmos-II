listao =[1,2,3,3,3,4,5,5,5,6,6,6,7,8,9,9,9]
listan=[]
for i in listao:
   if i not in listan:
    listan.append(i)
print("-->Ejercicio 11<--\n")
print("Lista original: ",listao)
print("Nueva lista: ",listan)