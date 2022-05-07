import estructuras,BaseDatos

class Menu:
    decision=0

    def __init__(self,escogida) -> None:
        self.decision=escogida
    @staticmethod
    def mostrarMenu()->None:
        print("_____________________Bienvenidx a tu biblioteca virtual!!_______________________")
        print("________________________________________________________________________________")
        print("Al equipo de BiblioVirtual nos alegra que nos escojas para organizar tus libros.")
        print("********************************************************************************")
        print("¿Que desea hacer?")
        print("1. Ver los libros guardados")
        print("2. Agregar un libro")
        print("3. Eliminar un libro")
        desicion=int(input().strip())
        if desicion == 1:
            Menu.mostrarLibros()

    @staticmethod
    def mostrarLibros()->None:
        baseLibros=BaseDatos.BD()
        baseLibros.descargarLibros()
        listaLibros= baseLibros.getLibros()
        recorrido:estructuras.Nodo =listaLibros.cabeza
        while recorrido!=None:
            print(recorrido.verDato())
            recorrido=recorrido.siguiente


