import estructuras,BaseDatos,Usuario,Menu,Opciones

class Operacion1:
    def __init__(self,user:Usuario.usuario) -> None:
        self.usuario=user
    def mostrarLibros(self)->None:
        
        listaLibros= Menu.baseLibros.getLibros()
        recorrido:estructuras.Nodo =listaLibros.cabeza

        while recorrido!=None:
            
            libro:estructuras.ListaEnlazada=recorrido.verDato()

            if(libro.cabeza.dato==self.usuario.username):
                recorrido2:estructuras.Nodo =libro.cabeza.siguiente
                while recorrido2!=None:
                    print(recorrido2.verDato(),end=",")
                    recorrido2=recorrido2.siguiente
                print("")
            recorrido=recorrido.siguiente
        print()
        print("¿Quisiera Buscar un libro en especifico o prefiere volver?")
        print("1. Buscar Libro.")
        print("2. Volver.")
        desicion=int(input().strip())
        opcion=Opciones.Opciones(self.usuario)
        if desicion == 1:
            
            opcion.buscarLibro()
        elif desicion == 2:
            anterior=Menu.display.pop()
            if anterior == "menu":
                menu=Menu.Menu(self.usuario)
                menu.mostrarMenu()