# se importa la libreria tkinter con todas sus funciones 

from cProfile import label
from calendar import c
from logging import root
from os import pread
from tkinter import *
from tkinter import messagebox
from turtle import bgcolor

from click import command

#------------
#funciones de la app
#------------

def sumar():
    messagebox.showinfo("Suma 1.0", "Hizo click en el boton sumar...")
    c = int(a.get()) + int(b.get())
    t_resultados.insert(INSERT, "La suma de " + str(a.get()) + " + " + str(b.get()) + " es " + str(c)+"\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos seran borrados...")
    a.set(0)
    b.set(0)
    t_resultados.delete("1.0", "end")

def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrara...")
    ventana_principal.destroy()



#----------
#ventana principal
#--------------

#se declara una variable llamada ventana principal y que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

#titulo de la ventana 
ventana_principal.title("Paises bajos ")

# Establecer tamaño a la ventana
ventana_principal.geometry("800x500")

#Icono de la ventana principal


#Desahabilitar boton de maximizar
ventana_principal.resizable(0,0)

#color de fondo de la pantalla principal
ventana_principal.config(bg="black")

#-----------
#variable globales
#-----------

a = StringVar()
b = StringVar()
c = StringVar()


#---------
#frame entrada
#-------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=780, height=240)
frame_entrada.place(x=10, y=10)

#Etiqueta para el titulo de la app
titulo = Label(frame_entrada, text= "Colegio San jose de guanenta")
titulo.config(bg="yellow", fg="blue" , font=("Arial", 20))
titulo.place(x=390, y=10)

#Etiqueta para el subtitulo de la app
subtitulo = Label(frame_entrada,  text='Especialidad en Sistemas')
subtitulo.config(bg="blue", fg="white" , font=("Arial", 13))
subtitulo.place(x=390, y=50)

#Etiqueta para subtitulo2 de la app
subtitulo2 = Label(frame_entrada,  text= 'SUMA DE ENTEROS')
subtitulo2.config(bg="blue", fg="black" , font=("Arial", 15))
subtitulo2.place(x=390, y=80)

# Imagen logo de la app
logo = PhotoImage(file="png-clip (2).png" )
etiq_logo = Label(frame_entrada, image=logo)
etiq_logo.place(x=10, y=10)

#etiqueta para valor a
etiq_a = Label (frame_entrada,  text="a =")
etiq_a.config(bg="yellow", fg="black", font=("Arial", 20), anchor=CENTER)
etiq_a.place(x=350, y=120)

# entry para el valor a
entry_a = Entry (frame_entrada, width=4, textvariable=a)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=487,  y=120)

#etiqueta para valor b
etiq_b = Label (frame_entrada,  text="b =")
etiq_b.config(bg="yellow", fg="black", font=("Arial", 20), anchor=CENTER)
etiq_b.place(x=585, y=120)

# entry para el valor b
entry_b = Entry (frame_entrada, width=4, textvariable=b)
entry_b.config(font=("Arial", 20), )
entry_b.focus_set()
entry_b.place(x=682,  y=120)

#frame operaciones
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=780, height=120)
frame_operaciones.place(x=10, y=260)

# Boton para sumar los numeros - texto
bt_sum = PhotoImage(file="sumaaa.png")
#bt_sumar= Button(frame_operaciones, text= "sumar", width=10)
bt_sumar = Button(frame_operaciones, image=bt_sum, width=105, height=105, command=sumar)
bt_sumar.place(x=116, y=7)


#Boton para borrar entradas y resultados
bt_bor = PhotoImage(file="eliminar1.png")
# bt_borrar = Button (frame_operaciones, text="Borrar", width=10)
bt_borrar = Button (frame_operaciones, image=bt_bor, width=105, height=105, command=borrar)
bt_borrar.place(x=337, y=7)


#Boton para salir - cerrar la app
bt_sal = PhotoImage(file="exit u.png")
# bt_salir= Button (frame_operaciones, text ="salir", width=10)
bt_salir = Button(frame_operaciones, image=bt_sal, width=105, height=105, command=salir)
bt_salir.place (x=558, y=7)


#frame resultado
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=780, height=100)
frame_resultados.place(x=10, y=390)

# area de texto de resultados
t_resultados = Text(frame_resultados, width=50, height=3)
t_resultados.config(bg="green", fg="white", font=("Arial", 20))
t_resultados.pack()










#Se ejecuta el metodo mainloop() de la clase Tk() a traves de la instancia ventana principal.
#Este metodo despliega una ventana simple en la pantalla y queda a la espera de lo que el
#usuario haga, por ejemplo, click en boton, escribir en caja de texto, etc.
#cada accion del usuariose conoce como un evento.El metodo mainloop es un bucle infinito.








ventana_principal.mainloop()