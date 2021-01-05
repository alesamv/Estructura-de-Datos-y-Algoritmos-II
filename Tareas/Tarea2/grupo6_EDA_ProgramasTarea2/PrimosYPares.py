def par(i):
  if(i%2 == 0):
    print("Es par:")

def primo(i):
  a=0
  for j in range(1,i+1):
    if(i%j==0):
      a=a+1
  if(a==2):
    print("Es primo:")

suma = 0
for i in range(300):
  print (i+1)
  suma = suma+i
  primo(i)
  par(i)
print("La suma total es: ", suma)