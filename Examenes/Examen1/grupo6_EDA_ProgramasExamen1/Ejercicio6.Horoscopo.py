def Horoscopo(m,d):
	if m==1:
		if(d<=20):
			s="Capricornio."
		else:
			s="Acuario."
		
	elif m==2:
		if(d<=19):
			s="Acuario."
		else:
			s="Piscis."
	elif m==3:
		if(d<=20):
			s="Piscis."
		else:
			s="Aries."
	elif m==4:
		if(d<=20):
			s="Aries."
		else:
			s="Tauro."
	elif m==5:
		if(d<=20):
			s="Tauro."
		else:
			s="Geminis."
	elif m==6:
		if(d<=21):
			s="Geminis."
		else:
			s="Cancer."
	elif m==7:
		if(d<=23):
			s="Cancer."
		else:
			s="Leo."
	elif m==8:
		if(d<=23):
			s="Leo."
		else:
			s="Virgo."
	elif m==9:
		if(d<=23):
			s="Virgo."
		else:
			s="Libra."
	elif m==10:
		if(d<=22):
			s="Libra."
		else:
			s="Escorpio."
	elif m==11:
		if(d<=22):
			s="Escorpio."
		else:
			s="Sagitario."
	elif m==12:
		if(d<=21):
			s="Sagitario"
		else:
			s="Capricornio."
	else:
		s="No Definido."
		print("Ocurrió un error...")
	return s

M=[0,31,29,31,30,31,30,31,31,30,31,30,31]
print("-->Examen1 - Ejercicio6<--\n")
m=int(input("Introduce tu mes de nacimiento: "))
while (m<1 or m>12):
	m=int(input("Mes invalido, introduce uno valido entre 1 y 12: "))
ds=M[m]
d=int(input("Introduce tu dia de nacimiento: "))
while (d<1 or d>ds):
	d=int(input("Dia invalido, introduce uno valido entre 1 y {0}: ".format(ds)))
signo=Horoscopo(m,d)

print("\nTu signo zodiacal es: ",signo)