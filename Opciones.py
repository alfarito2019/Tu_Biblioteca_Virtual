import estructuras,BaseDatos,Usuario,Menu,estructuraCola
import time


class Opciones:
    decision=0
    global baseLibros

    def __init__(self,user:Usuario.usuario) -> None:
        self.usuario=user

    def mostrarLibros(self)->None:
            
            baseLibros=BaseDatos.BD(self.usuario)
            baseLibros.descargarLibros()
            listaLibros= baseLibros.getLibros()
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
            opcion=Opciones(self.usuario)
            if desicion == 1:
                
                opcion.buscarLibro()
            elif desicion == 2:
                anterior=Menu.display.pop()
                if anterior == "menu":
                    menu=Menu.Menu(self.usuario)
                    menu.mostrarMenu()
            
    ##Configurar metodo para agregar busqueda de libros
    def buscarLibro(self)->None:
        inicio = time.perf_counter()
        baseLibros=BaseDatos.BD(self.usuario)
        baseLibros.descargarLibros()
        listaLibros= baseLibros.getLibros()
        print("¿Bajo que categoría quisiera buscar el libro?")
        print("1. Nombre libro")
        print("2. Autor")
        desicion=int(input().strip())
        confirmacion=False
        if desicion == 1:
            nombre_dado=input("¿Que nombre de libro busca? ")
            inicio = time.perf_counter()
            
            recorrido:estructuras.Nodo =listaLibros.cabeza
            
            contador=0
            while recorrido!=None:
                
                libro:estructuras.ListaEnlazada=recorrido.verDato()
                usuario=libro.cabeza.verDato()
                nombre_libro:str=libro.cabeza.siguiente.siguiente.verDato()
                if(usuario==self.usuario.username and nombre_libro==nombre_dado.strip()):
                    confirmacion=True
                    contador+=1
                    if contador==1:
                        print("Autor| Título| Autoconclusivo/Bilogía/Trilogía/Saga| Genero| Formato(electrónico o físico)|Estado de lectura (leido/pendiente)|Prestado(Si/No)|")
                        

                    recorrido2:estructuras.Nodo =libro.cabeza.siguiente
                    
                    while recorrido2!=None:
                        
                        print(recorrido2.verDato(),end="|")
                        recorrido2=recorrido2.siguiente
                    print("")

                recorrido=recorrido.siguiente
                final  = time.perf_counter()
                print(final - inicio )     
            if not confirmacion:
                    print("Busqueda no encontrada")
                    final  = time.perf_counter()
                    print(final - inicio )     
        elif desicion == 2:
            autor_dado=input("¿Que autor busca? ")
            inicio = time.perf_counter()
            recorrido:estructuras.Nodo =listaLibros.cabeza
            confirmacion=False
            contador=0
            while recorrido!=None:
                libro:estructuras.ListaEnlazada=recorrido.verDato()
                usuario=libro.cabeza.verDato()
                autor:str=libro.cabeza.siguiente.verDato()
                nombre_libro:str=libro.cabeza.siguiente.siguiente.verDato()
                if(usuario==self.usuario.username and autor==autor_dado.strip()):
                    confirmacion=True
                    contador+=1
                    if contador==1:
                        print("Autor| Título| Autoconclusivo/Bilogía/Trilogía/Saga| Genero| Formato(electrónico o físico)|Estado de lectura (leido/pendiente)|Prestado(Si/No)|")
                    
                    recorrido2:estructuras.Nodo =libro.cabeza.siguiente
                    while recorrido2!=None:
                        
                        print(recorrido2.verDato(),end="|")
                        recorrido2=recorrido2.siguiente
                    print("")
                recorrido=recorrido.siguiente
                
            if not confirmacion:
                print("Busqueda no encontrada")
                
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


        

    def agregarLibros(self):
        print("\nPara agregar un nuevo libro a su biblioteca digite la siguiente información")
        autor = input("\n¿Quien es el autor? ") #libre
        titlulo = input("\n¿Cual es el titulo del libro? ") #libre

        print("¿Pertenece a alguna familia de libros? ")
        print("De que tipo sería ")
        print("Autoconclusivo(1) ")
        print("Bilogía(2) ")
        print("Trilogía(3) ")
        print("Saga(4) ")
        print("otros(5) ")
        extension = int(input(" porfavor escoja una de las anteriores: ")) #cerrada

        while (extension !=1 and extension !=2  and extension != 3 and extension != 4 and extension != 5):
                extension =int( input(" porfavor escoja una de las anteriores ")) #cerrada
        if extension == 1 :
            extension = "Autoconclusivo"
        
        if extension ==  2:
            extension = "Bilogía"

        if extension ==  3:
            extension = "Trilogía"

        if extension == 4 :
            extension = "Saga"
        
        if extension == 5 :
            extension = "otros"
        
            
        print("Escoge entre las siguientes: ")
        print("Libro academico(1) ")
        print("Biografía(2) ")
        print("Libro de poesia(3) ")
        print("Cuento(4) ")
        print("Novela(5) ")
        print("Fabulas(6) ")
        print("Libros de comedia(7) ")
        print("Crónica(8) ")
        print("Ensayo(9) ")
        print("otros(0) ")

        genero = int(input("\n¿Categoría de tu libro? "))
        while(genero != 0 and genero != 1 and genero != 2 and genero != 3 and genero != 4 and genero != 5 and genero != 6 and genero != 7 and genero != 8 and genero !=9):
            print("porfavor escoge una opcion valida")
            print("Escoge entre las anteriores:")
            genero = int(input("\n¿Categoría de tu libro? "))
        
        if genero == 1:
                genero = "Libro academico"
        if genero == 2:
                genero = "Biografía"
        if genero == 3:
                genero = "Libro de poesia"
        if genero == 4:
                genero = "Cuento"
        if genero == 5:
                genero = "Novela"
        if genero == 6:
                genero = "Fabulas"
        if genero == 7:
                genero = "Libros de comedia"
        if genero == 8:
                genero = "Crónica"
        if genero == 9:
                genero = "Ensayo"
        if genero == 0:
                genero = "otros(0)"

            
        print("Escoge entre las siguientes:")
        print("Libro de Papel(1) o Libro electrónico(2)")
        formato = int(input("\n¿Categoria de tu libro? ")) #escoger
        
        while(formato !=1  and formato !=2 ):
            print("porfavor escoge una opcion valida")
            formato = int(input("\n¿En que formato esta tu libro? ")) #escoger
        
        if formato == 1:
            formato = "Libro de Papel"
        if formato == 2:
            formato = "Libro electrónico"

        print("Escoge entre las siguientes:")
        print("finalizado(1) o pendiente(2)")
        estadodeLectura=int(input("\n¿En que estado se encuentra tu libro? ")) #escoger
        
        while(estadodeLectura != 1 and estadodeLectura != 2 ):
            print("porfavor escoge una opcion valida")
            formato = int(input("\n¿En que estado se encuentra tu libro? ")) #escoger
        
        if estadodeLectura == 1:
            estadodeLectura = "finalizado"
        if estadodeLectura == 2:
            estadodeLectura = "pendiente"
            
        print("\n¿Prestaste tu libro? ")
        prestado = input("¿si o no? ") #escoger
        while (prestado != "si" and prestado!= "no" ): 
            print ("escoge una opcion valida")
            prestado = input("¿si o no?") #escoger

        inicio = time.perf_counter() 
        baseLibros=BaseDatos.BD(self.usuario)
        baseLibros.appendLibros(autor,titlulo,extension,genero,formato,estadodeLectura,prestado)

        print("\n-- Has agregado un nuevo libro a tu colección! --")
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


    def eliminarLibro(self):
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

    def librosPorLeer(self):
            baseLibros=BaseDatos.BD(self.usuario)
            baseLibros.descargarLibros()
            listaLibros= baseLibros.getLibros()
            recorrido:estructuras.Nodo =listaLibros.cabeza 
            misLibros=estructuras.ListaEnlazada()
            librosSinLeer=estructuraCola.Cola()  
            datosLibro =estructuras.ListaEnlazada()
            while recorrido!=None:
                
                libro:estructuras.ListaEnlazada=recorrido.verDato()

                if(libro.cabeza.dato==self.usuario.username):
                    recorrido2:estructuras.Nodo =libro.cabeza.siguiente
                    while recorrido2!=None:
                        datosLibro.agregar(recorrido2.verDato())
                        
                        recorrido2=recorrido2.siguiente
                misLibros.agregar(datosLibro)   
                datosLibro =estructuras.ListaEnlazada()
                recorrido=recorrido.siguiente

            recorrido:estructuras.Nodo = misLibros.cabeza
            misLibros.verLista()
            while recorrido!=None:
                
                libro:estructuras.ListaEnlazada=recorrido.verDato()
                librosSinLeer=estructuraCola.Cola()  
                if(  misLibros.buscar("Pendiente")==True or misLibros.buscar("pendiente")== True):
                    recorrido2:estructuras.Nodo =libro.cabeza
                    while recorrido2!=None:
                        librosSinLeer.enqueue(recorrido2.verDato())
                        
                        recorrido2=recorrido2.siguiente
                    print("")
                recorrido=recorrido.siguiente
            if librosSinLeer.colaVacia()==True:
                print("Eres un excelente lector")
                print("Haz leido todos tus libros")

            else:
                librosSinLeer.verCola()
                print("¿Leiste el siguiente libro de lista?")
                print(librosSinLeer.verDequeue())
                datos:estructuras.ListaEnlazada = librosSinLeer.verDequeue()
                print("Si(1)  No(2)")
                leido = int(input("\n  ")) 
                if  leido == 1:
                    
                    titulo:estructuras.Nodo = datos.cabeza.siguiente
                    baseLibros.actualizarBaseleido(titulo.verDato(),leido)
                    librosSinLeer.dequeue()
                    
                    print("Exceletnte")
                    print ("Tu siguiente libro por leer es")


                else : 
                    print ("¿Que esperas para leerlo?")    


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