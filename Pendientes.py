import estructuras,BaseDatos,Usuario,Menu,estructuraCola,IntPendientes

class Operacion5:
    def __init__(self,user:Usuario.usuario) -> None:
        self.usuario=user
    def librosPorLeer(self):
        librosPorLeer=IntPendientes.librosPorLeer()
        librosPorLeer.createIntlibrosPorLeer()
        # baseLibros=BaseDatos.BD(self.usuario)
        # baseLibros.descargarLibros()
        # listaLibros= baseLibros.getLibros()
        # recorrido:estructuras.Nodo =listaLibros.cabeza 
        # librosSinLeer=estructuraCola.Cola()  

        # while recorrido!=None:
            
        #     libro:estructuras.ListaEnlazada=recorrido.verDato()
        #     pendiente:estructuras.Nodo=libro.cabeza.siguiente.siguiente.siguiente.siguiente.siguiente.siguiente
        #     if(libro.cabeza.dato==self.usuario.username and ((pendiente.verDato().lower())=="pendiente")):
        #         librosSinLeer.enqueue(libro.cabeza.siguiente.siguiente.verDato())  
        #     recorrido=recorrido.siguiente



        # if librosSinLeer.colaVacia()==True:
        #     print("Eres un excelente lector")
        #     print("Haz leido todos tus libros")

        # else:
        #     print("¿Leiste el siguiente libro de lista?")
        #     lib=librosSinLeer.verDequeue()
        #     print(lib)
        #     print("Si(1)  No(2)")
        #     leido = int(input("\n  ")) 
        #     if  leido == 1:
                
        #         titulo:estructuras.Nodo = lib
        #         baseLibros.actualizarBaseleido(titulo,leido)
        #         librosSinLeer.dequeue()
                
        #         print("Excelente")


        #     else : 
        #         print ("¿Que esperas para leerlo?")    


        # print("Desea volver al menu o salir del programa? ")
        # print("1. Volver ")
        # print("2. Salir ")
        # desicion=input().strip()
        # if desicion=="1":
        #     anterior=Menu.display.pop()
        #     if anterior == "menu":
        #         menu=Menu.Menu(self.usuario)
        #         menu.mostrarMenu()
        # elif desicion=="2":
        #     print("hasta pronto "+self.usuario.username)
