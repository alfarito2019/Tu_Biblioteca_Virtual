import BaseDatos,Usuario,Menu,time,IntAgregar

class Operacion2:
    def __init__(self,user:Usuario.usuario) -> None:
        self.usuario=user
    def agregarLibros(self):
        agregar=IntAgregar.Agregar()
        agregar.createIntAgregar()
        # print("\nPara agregar un nuevo libro a su biblioteca digite la siguiente información")
        # autor = input("\n¿Quien es el autor? ") #libre
        # titlulo = input("\n¿Cual es el titulo del libro? ") #libre

        # print("\n¿Pertenece a alguna familia de libros? ")
        # print("De que tipo sería ")
        # print("Autoconclusivo(1) ")
        # print("Bilogía(2) ")
        # print("Trilogía(3) ")
        # print("Saga(4) ")
        # print("otros(5) ")
        # extension = int(input("\nPorfavor escoja una de las anteriores: ")) #cerrada

        # while (extension !=1 and extension !=2  and extension != 3 and extension != 4 and extension != 5):
        #         extension =int( input(" \nporfavor escoja una de las anteriores ")) #cerrada
        # if extension == 1 :
        #     extension = "Autoconclusivo"
        
        # if extension ==  2:
        #     extension = "Bilogía"

        # if extension ==  3:
        #     extension = "Trilogía"

        # if extension == 4 :
        #     extension = "Saga"
        
        # if extension == 5 :
        #     extension = "otros"
        
            
        # print("\nEscoge entre las siguientes: ")
        # print("Libro academico(1) ")
        # print("Biografía(2) ")
        # print("Libro de poesia(3) ")
        # print("Cuento(4) ")
        # print("Novela(5) ")
        # print("Fabulas(6) ")
        # print("Libros de comedia(7) ")
        # print("Crónica(8) ")
        # print("Ensayo(9) ")
        # print("otros(0) ")

        # genero = int(input("\n¿Categoría de tu libro? "))
        # while(genero != 0 and genero != 1 and genero != 2 and genero != 3 and genero != 4 and genero != 5 and genero != 6 and genero != 7 and genero != 8 and genero !=9):
        #     print("\nporfavor escoge una opcion valida")
        #     print("\nEscoge entre las anteriores:")
        #     genero = int(input("\n¿Categoría de tu libro? "))
        
        # if genero == 1:
        #         genero = "Libro academico"
        # if genero == 2:
        #         genero = "Biografía"
        # if genero == 3:
        #         genero = "Libro de poesia"
        # if genero == 4:
        #         genero = "Cuento"
        # if genero == 5:
        #         genero = "Novela"
        # if genero == 6:
        #         genero = "Fabulas"
        # if genero == 7:
        #         genero = "Libros de comedia"
        # if genero == 8:
        #         genero = "Crónica"
        # if genero == 9:
        #         genero = "Ensayo"
        # if genero == 0:
        #         genero = "otros(0)"

            
        # print("\nEscoge entre las siguientes:")
        # print("Libro de Papel(1) o Libro electrónico(2)")
        # formato = int(input("\n¿Categoria de tu libro? ")) #escoger
        
        # while(formato !=1  and formato !=2 ):
        #     print("\nporfavor escoge una opcion valida")
        #     formato = int(input("\n¿En que formato esta tu libro? ")) #escoger
        
        # if formato == 1:
        #     formato = "Libro de Papel"
        # if formato == 2:
        #     formato = "Libro electrónico"

        # print("\nEscoge entre las siguientes:")
        # print("finalizado(1) o pendiente(2)")
        # estadodeLectura=int(input("\n¿En que estado se encuentra tu libro? ")) #escoger
        
        # while(estadodeLectura != 1 and estadodeLectura != 2 ):
        #     print("\nporfavor escoge una opcion valida")
        #     formato = int(input("\n¿En que estado se encuentra tu libro? ")) #escoger
        
        # if estadodeLectura == 1:
        #     estadodeLectura = "finalizado"
        # if estadodeLectura == 2:
        #     estadodeLectura = "pendiente"
            
        # print("\n¿Prestaste tu libro? ")
        # prestado = input("¿si o no? ") #escoger
        # while (prestado != "si" and prestado!= "no" ): 
        #     print ("\nescoge una opcion valida")
        #     prestado = input("¿si o no?") #escoger

        # inicio = time.perf_counter() 
        # baseLibros=BaseDatos.BD(self.usuario)
        # baseLibros.appendLibros(autor,titlulo,extension,genero,formato,estadodeLectura,prestado)

        # print("\n-- Has agregado un nuevo libro a tu colección! --")
        # final  = time.perf_counter()
        # print(final - inicio )

        # print("\nDesea volver al menu o salir del programa? ")
        # print("1. Volver ")
        # print("2. Salir ")
        # desicion=input().strip()
        # if desicion=="1":
        #     anterior=Menu.display.pop()
        #     if anterior == "menu":
        #         menu=Menu.Menu(self.usuario)
        #         menu.mostrarMenu()
        # elif desicion=="2":
        #     print("\nHasta pronto "+self.usuario.username) 
