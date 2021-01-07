from time import clock

def radixsort(aList):
	RADIX=len(aList)
	maxLength= False
	tmp, placement = -1,1
	while not maxLength:
		maxLength=True
		buckets=[list() for _ in range(RADIX)]
	for i in aList:
		tmp=i/placement
		buckets[int(tmp%RADIX)].append(i)
		if maxLength and tmp > 0:
			maxLength=False
	a=0
	for b in range(RADIX):
		buck=buckets[b]
		for i in buck:
			aList[a]=i
			a+=1
	placement*=RADIX

def radixsortInverso(aList):
	RADIX=len(aList)
	maxLength= False
	tmp, placement = -1,1
	while not maxLength:
		maxLength=True
		buckets=[list() for _ in range(RADIX)]
	for i in aList:
		tmp=i/placement
		buckets[int(tmp%RADIX)].append(i)
		if maxLength and tmp > 0:
			maxLength=False
	a=0
	for b in range(RADIX):
		buck=buckets[b]
		for i in buck:
			aList[a]=i
			a-=1
	placement*=RADIX
   	

a=[]
b=[]
c=[]
for i in range(500,-1,-1):
	a.append(i)
for i in range(200,-1,-1):
	b.append(i)
for i in range(100,-1,-1):
	c.append(i)
print("Lista desordenada: {0} ".format(a))
tiempoi=clock()
radixsort(a)
tiempof=clock()		
print("\nLista ordenada: {0} ".format(a))
print("Tiempo de Radixsort es: {0} seg".format((tiempof-tiempoi)))