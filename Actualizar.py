import BaseDatos,Usuario,Menu

class Operacion4:
    def __init__(self,user:Usuario.usuario) -> None:
        self.usuario=user
    def actualizarLibro(self):  
        titulo=input("Que libro desea actualizar? ")
        estado=input("El libro está prestado? (1)Si, (2)No: ")
        if estado == "1":
            estado = "si"
        elif estado == "2":
            estado = "no"
        else:
            print("Debe elegir una opción valida")
            while estado != "1" and estado != "2":
                estado=input("El libro está prestado? (1)Si, (2)No: ")
        baseLibros=BaseDatos.BD(self.usuario)
        baseLibros.actualizarBaseLibro(titulo,estado)
       
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
