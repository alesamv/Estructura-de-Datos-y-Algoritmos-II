#!/usr/bin/env python
#-*- coding: utf-8 -*-

from Tkinter import *
import tkFont
import tkMessageBox

"""Función ingresar crea la ventana principal, donde despliega primero los datos del alumno, nombre, cuenta y promedio, con los 
botones de Consulta horarios, Registra Materias, y Cerrar Sesión"""
def ingresar():
	val = validaAcesso() #Llama a la funcion valida acceso, para poder ingresar al sistema
	if val == True:
		font=tkFont.Font(family="times new roman")
		global opcion1,opcion2,opcion3,opcion4,ventana2
		opcion1 = IntVar()
		opcion2 = IntVar()
		opcion3 = IntVar()
		opcion4 = IntVar()
		ventana.destroy()
		ventana2 = Tk()
		ventana2.title("Menú principal")
		ventana2.geometry("600x400")
		ventana2.config(bg="#ffffcc")
		EtiquetaEncontrado = Label(ventana2,text="Usuario Encontrado",bg="#ffffcc",font=font).pack()
		NombreLa = Label(ventana2,text="Nombre del Alumno: "+alumno_encontrado[0],bg="#ffffcc",font=font).place(x=10,y=20)
		NumCLa = Label(ventana2,text="Numero de Cuenta: "+str(Numero_Cuenta.get()),bg="#ffffcc",font=font).place(x=10,y=40)
		PromLa = Label(ventana2,text="Promedio: "+str(alumno_encontrado[2]),bg="#ffffcc",font=font).place(x=10,y=60)
		ConsultaHorBu = Button(ventana2,text="Consulta Horarios",bg="#ff9966",command=Consulta_Horario,borderwidth=2,padx=20,cursor="hand2",textvariable=opcion1,font=font).place(x=200,y=150,anchor=W)
		RegisMatBu = Button(ventana2,text="Registra Materias",command=Registra_Materia,bg="#ff9966",borderwidth=2,padx=20,textvariable=opcion2,font=font,cursor="hand2").place(x=200,y=190,anchor=W)
		RegresarBu = Button(ventana2,text="Cerrar Sesion",bg="#ff9966",command=Regresar_Login,borderwidth=2,padx=20,textvariable=opcion3,font=font,cursor="hand2").place(x=215,y=230,anchor=W)
		SalirBu = Button(ventana2,text="Salir",borderwidth=2,padx=20,command=Salir,bg="#ff9966",textvariable=opcion4,font=font,cursor="hand2").place(x=255,y=270)
		
	else:
		tkMessageBox.showerror("AVISO","No. de Cuenta o Clave inválidas") #Si es falso arroja una ventana con la leyenda correspondiente

"""Función hash para generar la clave unica de cada usuario para ingresar al sistema; le aplica el modulo de 3 al numero de cuenta
y despues lo concatena con los ultimos tres digitos de su numero de cuenta"""
def hash(Numero_Cuenta):
	nc=[] 
	p1=str(Numero_Cuenta) 
	p2=str(Numero_Cuenta%3)
	nc=str(p1[len(p1)-4:len(p1)])
	con= p2+nc
	clave=int(con)
	return clave

"""Función Salir, es un comando para destruir la ventana"""
def Salir():
	ventana2.destroy()

"""Funcion Registra_Materia, abre una ventana para dar de alta la materia, contiene una etiqueta "Registro" y 
cuadros texto para ingresa el grupo y clave a dar de alta"""
def Registra_Materia():  
	global ventana_Registra,grupo,clave_grupo,nuevo_grupo,nueva_clave
	grupo = IntVar()
	clave_grupo = IntVar()
	nuevo_grupo = IntVar()
	nueva_clave = IntVar()
	ventana_Registra = Tk()
	ventana_Registra.title("Registro")
	ventana_Registra.geometry("600x400")
	GrupoLabe = Label(ventana_Registra,text="Grupo: ").place(x=65,y=40)
	GrupoEn = Entry(ventana_Registra,textvariable=grupo).place(x=115,y=40)
	ClaveMaLa = Label(ventana_Registra,text="Clave de Grupo:").place(x=10,y=60)
	ClaveMaEn = Entry(ventana_Registra,textvariable=clave_grupo).place(x=115,y=60)
	AltaBu = Button(ventana_Registra,text="Alta",command=alta,borderwidth=3,cursor="hand2").place(x=30,y=350)

"""Función alta, es un comando utilizado en la interfaz grafica para dar de alta la matera"""
def alta(grupo,clave_grupo):
	print("Se dio de alta: "+grupo+""+clave_grupo)

"""Funcion Regresar_Login, al momento de cerrar la sesion se muestra el aviso de sesión cerrada, se destruye la ventana y se 
regresa a la pantalla del Login"""
def Regresar_Login():
	tkMessageBox.showinfo("AVISO","Sesión Cerrada")
	ventana2.destroy()
	main()

"""Esta funcion solo cierra o destruye la ventana de la consulta de horarios"""
def Cerrar_Horario():
	ventana_Horario.destroy()

"""Funcion Consulta_Horario, abre el documento de texto Materias.txt, y lo lee linea a linea para imprimirlo en la ventana"""
def Consulta_Horario():
	global ventana_Horario
	i=30
	manf = open("Materias.txt")
	ventana_Horario = Tk()
	ventana_Horario.title("Horarios")
	ventana_Horario.geometry("600x400")
	NomProfe = Label(ventana_Horario,text="Profesor").place(x=80,y=30)
	NomMate = Label(ventana_Horario,text="Materia").place(x=250,y=30)
	NomHora = Label(ventana_Horario,text="Horario").place(x=350,y=30)
	NomVacan = Label(ventana_Horario,text="Vacantes").place(x=460,y=30)
	for linea in manf:
		HorarioLa = Label(ventana_Horario,text=linea).place(x=20,y=i)
		i+=20
	RegresaBu = Button(ventana_Horario,text="Cerrar",command=Cerrar_Horario,borderwidth=3,cursor="hand2").place(x=270,y=350)

def validaAcesso():
	global alumno_encontrado
	clave = hash(Numero_Cuenta.get())
	print(clave)
	for i in a:
		#Dentro de toda la lista de alumnos busca la coincidencia del número de cuenta.
		if i.numCuenta==str(Numero_Cuenta.get()) and clave == Clave_Alumno.get():
			alumno_encontrado = i.GetAlumno()
			#Una vez encontrada la cuenta se comprueba si la cuenta es correcta.
			return True 
	return False

#Al dar enter, llama a la función ingresar()
def onEnter(event):
	ingresar()

"""Función Login, crea la ventana principal con las etiquetas correspondientes a Numero de cuenta y Clave, con sus respectivos cuadros de texto"""
def Login(ventana,Numero_Cuenta,Clave_Alumno):
	font = tkFont.Font(family="times new roman",size="36")
	font2= tkFont.Font(family="times new roman")
	LoginLabel = Label(ventana,text="LOGIN",bg = "#caad00",font=font).place(x=215,y=50)
	NumCuen = Label(ventana,text="No. de Cuenta: ",bg="#caad00",font=font2).place(x=100,y=150)
	NumCuenEn = Entry(ventana,textvariable = Numero_Cuenta)
	NumCuenEn.delete(0,END)
	NumCuenEn.bind('<Return>',onEnter)
	NumCuenEn.place(x=210,y=150)
	ClaveAlu = Label(ventana,text="Clave de Alumno: ",bg="#caad00",font=font2).place(x=85,y=170)
	ClaveAluEn = Entry(ventana,textvariable = Clave_Alumno)
	ClaveAluEn.delete(0,END)
	ClaveAluEn.bind('<Return>',onEnter) #Se llama a la función onEnter, para capturar los datos al dar enter
	ClaveAluEn.place(x=210,y=170)
	IngresarB = Button(ventana,text="Ingresar",command=ingresar,bg="#FFCC66",borderwidth=3,activebackground="#FFCC00",cursor="hand2",font=font2).place(x=250,y=200)

class Alumno:
	nombre=''
	numCuenta=''
	claveAcceso=''
	materias=[]
	calficaciones=[]
	promedio=0
	#Constructor de la clase Alumno.
	"""Recibe nombre,número de cuenta y las materias con sus calificaciones"""
	def __init__(self,n,nu,ma,cal):
		self.nombre=n
		self.numCuenta=nu
		self.materias=ma
		self.calficaciones=cal

	#Agrega una materia al arreglo de materias del alumno
	def addMaterias(self,mat):
		self.materias.append(mat)

	#Recibe el arreglo de calificaciones y déspues de calcularlo retorna el promedio.
	def getPromedio(self,mat):
		p=0
		if len(mat)!=0:
			for i in range(len(mat)):
				p+=float(mat[i])
			p=p/(len(mat))
		return p

	#Muestra la información del alumno-->nombre, número de cuenta y su promedio.
	def GetAlumno(self):
		lista_alumno = []
		
		lista_alumno.append(self.nombre)
		lista_alumno.append(self.numCuenta)
		lista_alumno.append(self.getPromedio(self.calficaciones))
		return lista_alumno

def Capturar():
	total=[]
	#Abre el archivo(al estar terminado será el registro de alumnos)
	doc=open("Prueba.txt")
	#Iguala linea a la lectura de una linea del documento.
	linea=doc.readline()
	#Mientras linea contenga algo dentro se ejecutara todo el codigo.
	while linea!='':
		if linea!=None:
			#Convierte linea en un arreglo de cadenas llamado "palabras"
			palabras = linea.split()
			#Si el tamaño de la lista "palabras" es mayor a 0 accede al if. 
			if len(palabras)>0:
				"""Aquí busca que el primer elemento de la lista sea "Nombre:" si es así 
				comienza a conseguir valores para crear un alumno el cual se gaurdara en 
				otra lista llamada "total" la cual contendra todos los alumnos que estan
				dentro del documento que contiene a los alumnos"""
				if palabras[0]=='Nombre:':
					nom=''
					mat=[]
					cal=[]
					for i in range(1,len(palabras)):
						#Se guarda el nombre del alumno sacado del documento en una cadena 'nom'
						nom+=palabras[i]
						nom+=" "
					linea=doc.readline()
					palabras=linea.split()
					#Guarda el numero decuenta sacado del documento en una variable 'cuenta'
					cuenta=palabras[1]
					linea=doc.readline()
					palabras=linea.split()
					#Guarda todas las materias sacadas del documento y las gaurda en una lista 'mat'
					for i in range(1,len(palabras)):
						mat.append(palabras[i])
					linea=doc.readline()
					palabras=linea.split()
					#Guarda todas las calificaciones sacadas del documento y las guarda en 
					#una lista 'cal'
					for i in range(1,len(palabras)):
						cal.append(palabras[i])
					#Crea un alumno con los parametros obtenidos anteriormente y los guarda en 
					#una lista 'total'
					total.append(Alumno(nom,cuenta,mat,cal))
		#Continua leyendo liena a linea
		linea=doc.readline()
	#Retorna la lista con todos los alumnos localizados en el documento.
	return total


def main():
	global ventana,Numero_Cuenta,Clave_Alumno,a
	a=Capturar()
	ventana = Tk()
	ventana.title("Registro")
	ventana.geometry("600x400")
	ventana.config(bg="#caad00")
	Numero_Cuenta = IntVar()
	Clave_Alumno = IntVar()
	Login(ventana,Numero_Cuenta,Clave_Alumno)
	ventana.mainloop()

main()