# se importa la libreria tkinter con todas sus funciones 
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
frame_operaciones = Frame (ventana_pricipal)
frame_operaciones.config(bg="blue4", width=390, height=280 )
frame_operaciones.place(x=0,y=0)

frame_entrada = Frame (ventana_pricipal)
frame_entrada.config(bg="white", width=0, height=0 )
frame_entrada.place(x=0,y=0)

frame_operaciones = Frame (ventana_pricipal)
frame_operaciones.config(bg="red3", width=800, height=280 )
frame_operaciones.place(x=0,y=270)


ventana_pricipal.mainloop ()