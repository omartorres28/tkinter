# se importa la libreria tkinter con todas sus funciones 
from cProfile import label
from email.contentmanager import raw_data_manager
from tkinter import *

#------------
#ventana principal
#------------

# se declara una variable llamda ventana principa y que adquiere las caracteristicas de un objeto Tk()
ventana_pricipal = Tk ()

# Se ejecuta el metodo mainloop() de la clase TK() a traves de la instancia ventana principal.
# Este metodod despliega una ventana simple en la pantalla y que queda a la espera de lo que es 
# usuario haga, por ejemplo, click en boton, escribir en la caja de texto, etc.
# cada accion del usuario se conoce como un evento. El metodo mainloop es un bucle infinito
 
# establecer tamaño a la ventana 
ventana_pricipal.geometry ("800x500")

# establecer titulo de la ventana 
ventana_pricipal.title ("Alexander")

# Icono de la ventana principal


# Deshabilitar boton de maximizar
ventana_pricipal.resizable(0,0)


# color de fondo
ventana_pricipal.config(bg="white")

#----------
# frame entrada
#----------

frame_entrada = Frame (ventana_pricipal)
frame_entrada.config(bg="yellow", width=780, height=240 )
frame_entrada.place(x=10,y=10)

#Etiqueta para el titulo de la app
titulo = Label(frame_entrada , text="Colegio San Jose De Guanenta")
titulo.config(big="yellow", fg="blue", font=("Arail", 16) )
titulo.place (x=240 , y=(10))

#Etiqueta para el subtitulo de la app
subtitulo = Label(frame_entrada, text="especilalidad en sistemas")
subtitulo.config(bg="red", fg="black", font=("Arial",13))
subtitulo.place(x=240, y=40)

#Etiqueta para el subtitulo2 de la app
subtitulo2 = Label(frame_entrada, text="Suma de enteros")
subtitulo2.config(bg="orange", fg="pink", font=("Arial",13))
subtitulo2.place(x=240, y=40)

# Imagen - Logo de app
logo =PhotoImage(file="png-clip.png")
etiq_logo = label(frame_entrada,image =logo)
etiq_logo.place(x=10,y=10)

frame_entrada = Frame (ventana_pricipal)
frame_entrada.config(bg="blue", width=780, height=240 )
frame_entrada.place(x=10,y=250)

frame_operaciones = Frame (ventana_pricipal)
frame_operaciones.config(bg="red", width=780, height=240 )
frame_operaciones.place(x=10,y=370)


ventana_pricipal.mainloop ()