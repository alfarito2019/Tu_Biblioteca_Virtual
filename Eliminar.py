import BaseDatos,Usuario,Menu,time, IntEliminar

class Operacion3:
    def __init__(self,user:Usuario.usuario) -> None:
        self.usuario=user
    def eliminarLibro(self):
        eliminar=IntEliminar.Eliminar()
        eliminar.createIntEliminar()
        libroBorrado = input("Digita el nombre del libro que deseas borrar: \n")
        inicio = time.perf_counter()
        baseLibros=BaseDatos.BD(self.usuario)
        baseLibros.borrarLibro(libroBorrado)
        final  = time.perf_counter()
        print(final - inicio )
        print("Desea volver al menu o salir del programa? ")
        print("1. Volver ")
        print("2. Salir ")
        desicion=input().strip()
        if desicion=="1":
            anterior=Menu.display.pop()
            if anterior == "menu":
                menu=Menu.Menu(self.usuario)
                menu.mostrarMenu()
        elif desicion=="2":
            print("hasta pronto "+self.usuario.username)
class Operacion0:
    def __init__(self,user:Usuario.usuario) -> None:
        self.usuario=user
    def eliminarUsuario(self):
        print("¿Desea eliminar su usuario? \nEscoja una opcion valida: ")
        eliminar = input("¿si o no? \n")
        if eliminar == "si":
            username = input("Ingrese su nombre de usario: ")
            password = input("Ingrese su contraseña: ")  
            inicio = time.perf_counter()
            user1 = Usuario.usuario(username, password)            
            inicio=user1.inicioSesion()

            if inicio:
                print(".\n.\n.")
                baseUsuario=BaseDatos.BD(self.usuario)
                baseUsuario.borrarUsuario()
                inicio = time.perf_counter()

            else:
                print("El usuario o contraseña no coinciden. ")
        
        else:
            print("Entendido. ")
        
        pass
        final  = time.perf_counter()
        print(final - inicio )