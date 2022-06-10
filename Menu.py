import Opciones as op
import estructuraPila
import Usuario
import IntMenu
import IntBoton

global display
display=estructuraPila.Pila()
class Menu:
    # decision=0
    global baseLibros

    def __init__(self,user:Usuario.usuario) -> None:
        self.usuario=user
    def mostrarMenu(self)->None:
        IntMenu.createIntMenu()
        # display.push("menu")
        # print('''
        #         _____________________Bienvenidx a tu biblioteca virtual!!_______________________
        #         ________________________________________________________________________________
        #         Al equipo de BiblioVirtual nos alegra que nos escojas para organizar tus libros.
        #         ********************************************************************************
        #                                          ¿Que desea hacer?
        #         1. Ver los libros guardados
        #         2. Agregar un libro
        #         3. Eliminar un libro
        #         4. Actualizar estado libro
        #         5. Mis libros por leer
        #         6. Salir.
        #         0. Eliminar usuario y salir
        #         ''')
        # desicion=IntBoton.variableMenu
        opciones=op.Opciones(self.usuario)
        print(IntBoton.variableMenu)
        if  IntBoton.variableMenu == 1:
            opciones.mostrarLibros()
            display.push(1)
        elif IntBoton.variableMenu == 2:
            opciones.agregarLibros()
            display.push(2)
        elif IntBoton.variableMenu == 3:
            opciones.eliminarLibro()
            display.push(3)
        elif IntBoton.variableMenu == 4:
            opciones.actualizarLibro()
            display.push(4)
        elif IntBoton.variableMenu == 5:
            opciones.librosPorLeer()
            display.push(5)
        elif IntBoton.variableMenu == 6:
            self.usuario.salirSesion()
            display.push(6)
            print("Hasta la proxima :) "+ self.usuario.username)
        elif IntBoton.variableMenu == 0:
            opciones.eliminarUsuario()
        # else:
        #     print("\nDebe elegir una de las opciones enumeradas\n")

    


        
