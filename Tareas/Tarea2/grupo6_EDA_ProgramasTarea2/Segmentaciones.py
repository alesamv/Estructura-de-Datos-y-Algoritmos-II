def Segmentar(listaA,p,r):
  if r - p > 0:
    q = int((p+r)/2)
    print("-")
    print(listaA[p:r+1])
    if(len(listaA[p:r+1]) == 2):
      print("[",listaA[p],"]")
      print("[",listaA[r],"]")
    Segmentar(listaA,p,q)
    Segmentar(listaA,q+1,r)
    

listaA = [6,4,7,1,3,8,2,5]
print("La lista contiene los siguientes elementos: ",listaA)
Segmentar(listaA, 0, 7)
