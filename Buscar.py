import estructuras,BaseDatos,estructuraArbolAVL,Usuario,Menu,time

class Operacion1_1:
    def __init__(self,user:Usuario.usuario) -> None:
        self.usuario=user
    def buscarLibro(self)->None:
        
        baseLibros=BaseDatos.BD(self.usuario)
        print("Aqui estamos llegando1")
        baseLibros.descargarLibrosArbol()
        print("Aqui estamos llegando2")
        listaLibros= baseLibros.getLibrosArbol()
        print("¿Bajo que categoría quisiera buscar el libro?")
        print("1. Nombre libro")
        print("2. Autor")
        desicion=int(input().strip())
        confirmacion=False
        if desicion == 1:
            nombre_dado=input("¿Que nombre de libro busca? ")
            datoslibro=listaLibros.encontrar(nombre_dado)
            if datoslibro != None:
                lista:estructuras.ListaEnlazada=datoslibro.valor 
                lista.verLista()
            
            else:
                print("Por ahora no posees este libro")           
                       
        elif desicion == 2:
            autor_dado=input("¿Que autor busca? ")
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
