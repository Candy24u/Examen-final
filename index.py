from tkinter import *
from datetime import date
from datetime import datetime

root = Tk()
#Ancho y alto de ventana
ancho = 450
alto = 300

#Ventana
root.geometry(str(ancho)+'x'+str(alto))
root.title('Examen Final by Candy Méndez')
        

#Etiquetas para ingresar los datos 

#Título principal
Saludo = Label(text="Bienvenido",font=("Arial",18))
Saludo.grid(row=1, column=1, columnspan=6)

#Nombre
Nombre = Label(text="Nombre:",font=("Arial", 13))
Nombre.grid(row=2, column=1, columnspan=2)
#Entrada de texto de Nombre
txtUsuarioN = Entry(root)
txtUsuarioN.grid(row=2, column=3, columnspan=4, sticky= W + E)

#Apellido
Apellido= Label(text="Apellido:",font=("Arial", 13))
Apellido.grid(row=3, column=1, columnspan=2)
#Entrada de texto de Apellido
txtUsuarioA = Entry(root)
txtUsuarioA.grid(row=3, column=3, columnspan=4, sticky= W + E)

#Día
Dia = Label(text="Día:",font=("Arial", 13))
Dia.grid(row=4, column=1, columnspan=2)
#Entrada de texto de Día
txtUsuarioD = Entry(root)
txtUsuarioD.grid(row=4, column=3, columnspan=4, sticky= W + E)

#Mes
Dia = Label(text="Mes:",font=("Arial", 13))
Dia.grid(row=5, column=1, columnspan=2)
#Entrada de texto de mes
txtUsuarioM = Entry(root)
txtUsuarioM.grid(row=5, column=3, columnspan=4, sticky= W + E)

#año
año = Label(text="Año:",font=("Arial", 13))
año.grid(row=6, column=1, columnspan=2)
#Entrada de texto de año
txtUsuarioE = Entry(root)
txtUsuarioE.grid(row=6, column=3, columnspan=4, sticky= W + E)

#Funciones del examen
#1
#Función que muestra la fecha ingresada en código hexadecimal
def hexadecimal():
    Dia=hex(int(txtUsuarioD.get()))
    Mes=hex(int(txtUsuarioM.get()))
    Año=hex(int(txtUsuarioE.get())) 
    
    salida = f"{txtUsuarioD.get()}/{txtUsuarioM.get()}/{txtUsuarioE.get()}={Dia}/{Mes}/{Año}  "
    Resultado["text"] = salida

#2
#Función que muestra las horas que ha vivido desde que nació hasta el día actual
def horasdevida():
    fechaString = f"{txtUsuarioE.get()}-{txtUsuarioM.get()}-{txtUsuarioD.get()}"
    dato = datetime.strptime(fechaString, '%Y-%m-%d')

    today= datetime.today()
    
    c1 = today
    c2 = dato
    dias = abs(c1-c2).days 
    salida1 = abs(dias*24)
    Salida = f"Usted nació el {dato} y ha vivido {salida1} horas."

    Resultado["text"] = Salida

#3
#Función que muetra si el número de letras de su nombre y apellido es par o impar
def NyA():
    
    Nombre= f"{txtUsuarioN.get()}"
    Apellido = f"{txtUsuarioA.get()}"

    NumerosofA = len(Nombre)
    Numerosofb = len(Apellido)
    
    if NumerosofA % 2 == 0 & Numerosofb % 2 == 0:
        c3 = f"{Nombre}{Apellido} su nombre junto a su apellido es par"
    else:
        c3 = f"{Nombre}{Apellido} su nombre junto a su apellido es impar"

    Salida = f"{c3} "
    Resultado["text"] = Salida

#4
#Función que mustre cuántas vocales y cuantas consonantes tiene su nombre y su apellido
def vocalesconsonantes():
    Nombre=str(txtUsuarioN.get())
    Apellido=str(txtUsuarioA.get())
    Suma = 0
    for vccn in Nombre:
        if vccn == 'a' or vccn =='A' or vccn =='e' or vccn =='E' or vccn =='i' or vccn =='I' or vccn =='o' or vccn =="O" or vccn =="u" or vccn =="U":
            Suma += 1
    for vccn in Apellido:
        if vccn == 'a' or vccn =='A' or vccn =='e' or vccn =='E' or vccn =='i' or vccn =='I' or vccn =='o' or vccn =="O" or vccn =="u" or vccn =="U":
            Suma += 1
    sse=len(Nombre)
    sse2=len(Apellido)
    SalidaConso=sse+sse2-Suma

    Resultado['text'] = Nombre + " " + Apellido + ' tiene {} vocales y {} consonantes.'.format(Suma,SalidaConso) 

#5
#Función que muestre su nombre y apellido al revés 
def revés():
    text20 = txtUsuarioN.get()+" "+txtUsuarioA.get()
    text20 = text20[::-1]
    Resultado["text"] = txtUsuarioN.get() + " " + txtUsuarioA.get() + " al revés es: " + text20

#Botones de las funciones
Funcion1 = Button(root, text = "Función 1",command=hexadecimal,font=("Arial", 9), width=10)
Funcion1.grid(row=7, column=1)

Funcion2 = Button(root, text = "Función 2",command=horasdevida,font=("Arial", 9), width=10)
Funcion2.grid(row=7, column=2)

Funcion3 = Button(root, text = "Función 3",command=NyA,font=("Arial", 9), width=10)
Funcion3.grid(row=7, column=3)

Funcion4 = Button(root, text = "Función 4",command=vocalesconsonantes,font=("Arial", 9), width=10)
Funcion4.grid(row=7, column=4)

Funcion5 = Button(root, text = "Función 5",command=revés,font=("Arial", 9), width=10)
Funcion5.grid(row=7, column=5)

#Salida de las funciones
Resultado = Label(root, text="Aca se verá el resultado de las funciones", font=("Arial", 12))
Resultado.grid(row=8, column=1, columnspan=6)
#ventana
root.mainloop()