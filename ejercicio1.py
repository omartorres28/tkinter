# se importa la libreria tkinter con todas sus funciones 
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
ventana_pricipal.geometry ("800x300")

# establecer titulo de la ventana 
ventana_pricipal.title ("Alexander")

# Icono de la ventana principal


# Deshabilitar boton de maximizar
ventana_pricipal.resizable(0,0)

# Agregamos un widget a la ventna principal 
letrero = Label(text="\n\n Sistemas la mejor!!\n\n", bg="LightBlue1")
letrero.pack()

# color de fondo
ventana_pricipal.config(bg="medium spring green")

# Agregamos un widget a la ventna principal 
letrero2 = Label(text="\n\n Alexander !!\n\n", bg="blue")
letrero2.pack()

# Agregamos un widget a la ventna principal 
letrero3 = Label(text="\n\n Colegio San Jose De Guanenta!\n\n", bg="DeepSkyBlue2")
letrero3.pack()

#

ventana_pricipal.mainloop ()