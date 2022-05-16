import estructuras
import Usuario

class BD():
    
    def __init__(self,usuario:Usuario.usuario):
        self.base_usuarios= estructuras.ListaEnlazada() 
        self.base_libros= estructuras.ListaEnlazada()
        self.usuario=usuario
        

    def descargarUsuarios(self)-> None:
        f = open ('DatosPrueba/Usuarios.txt',mode='r', encoding='utf8')
        while(True):
            #leer la siguiente linea
            linea = f.readline()
            #revisar si la linea no es null
            if not linea:
                break
            #terminamos de leer el archivo 
            self.base_usuarios.agregar(estructuras.split(linea))

        f.close()
        
        
    def cargarUsuarios(self,username,password)-> bool:    
        f = open ('DatosPrueba/Usuarios.txt',mode='w', encoding='utf8')
        f.write(username,password)        
        f.close()

    def getUsuarios(self)-> estructuras.ListaEnlazada:
        return self.base_usuarios

    def appendUsuarios(self, username, password)->bool:
        f = open ('DatosPrueba/Usuarios.txt',mode='a', encoding='utf8')
        f.write(username+"|"+password+"|\n")
        f.close()

    def borrarUsuario(self):
        # Borrar libros del usuario
        fr = open('DatosPrueba/Libros.txt',mode='r', encoding='utf8')
        lineas = fr.readlines()
        fr.close()
        f = open('DatosPrueba/Libros.txt',mode='w', encoding='utf8')
        for linea in lineas:
            infoLibro = estructuras.split(linea)
            if infoLibro.cabeza.verDato() != self.usuario.nombreUsuario():
                f.write(linea)        
        f.close()

        # Borrar usuario
        usuarioEncontrado = False
        fr = open('DatosPrueba/Usuarios.txt',mode='r', encoding='utf8')
        lineas = fr.readlines()
        fr.close()
        f = open('DatosPrueba/Usuarios.txt',mode='w', encoding='utf8')
        for linea in lineas:
            infoUsuarios = estructuras.split(linea)
            if infoUsuarios.cabeza.verDato() != self.usuario.nombreUsuario():
                f.write(linea)
            else:
                usuarioEncontrado = True
        f.close()

        if usuarioEncontrado:
            print("\n-- Tu usuario se ha eliminado exitosamente! --")
        else:
            print("-- Lo sentimos, ocurrió un problema con la eliminación de tu usuario --")
        

    def descargarLibros(self)-> None:
        
        f = open ('DatosPrueba/Libros.txt', mode='r', encoding='utf-8')
        while(True):
            #leer la siguiente linea
            linea = f.readline()
            #revisar si la linea no es null
            if not linea:
                break
            #terminamos de leer el archivo 
            self.base_libros.agregar(estructuras.split(linea))

        f.close()
        
        

    def getLibros(self)-> estructuras.ListaEnlazada:
        return self.base_libros 


    def appendLibros(self,autor,titlulo,extension,genero,formato,estadodelectura,prestado)->bool:
        
        userName = self.usuario.nombreUsuario()
        f = open ('DatosPrueba/Libros.txt',mode='a', encoding='utf8')
        f.write("{a}|{b}|{c}|{d}|{e}|{f}|{g}|{h}|".format(a=userName,b=autor,c=titlulo,d=extension,e=genero,f=formato,g=estadodelectura,h=prestado)+"\n")
        f.close()   

    def actualizarBaseLibro(self,titulo,estado):
        libroEncontrado = False
        fr = open('DatosPrueba/Libros.txt',mode='r', encoding='utf8')
        lineas = fr.readlines()
        fr.close()
        f = open('DatosPrueba/Libros.txt',mode='w', encoding='utf8')
        for linea in lineas:
            infoLibro = estructuras.split(linea)
            tituloActual:str = infoLibro.cabeza.traerSiguiente().traerSiguiente().verDato()
            if infoLibro.cabeza.verDato() != self.usuario.nombreUsuario() or titulo != tituloActual: 
                f.write(linea)
            else:
                recorrido:estructuras.Nodo= infoLibro.cabeza
                escrito=""
                if estado=="1":
                    estado="si"
                elif estado=="2":
                    estado="no"
                while(recorrido!=None):
                    if recorrido==infoLibro.cola:
                        escrito=escrito+estado+"|\n"
                    else:
                        escrito+=recorrido.verDato()+"|"
                    recorrido=recorrido.siguiente
                libroEncontrado = True
                f.write(escrito)
                
        f.close()
        if libroEncontrado:
            print("El estado del libro '"+titulo+"'se actualizó")
        else:
            print("El libro '"+titulo+"'no esta en tu colección")

    def actualizarBaseleido(self,titulo,estado):
        libroEncontrado = False
        fr = open('DatosPrueba/Libros.txt',mode='r', encoding='utf8')
        lineas = fr.readlines()
        fr.close()
        f = open('DatosPrueba/Libros.txt',mode='w', encoding='utf8')
        for linea in lineas:
            infoLibro = estructuras.split(linea)
            tituloActual:str = infoLibro.cabeza.traerSiguiente().traerSiguiente().verDato()
            if infoLibro.cabeza.verDato() != self.usuario.nombreUsuario() or titulo != tituloActual: 
                f.write(linea)
            else:
                recorrido:estructuras.Nodo= infoLibro.cabeza
                escrito=""
                if estado==1:
                    estado="finalizado"
                while(recorrido!=None):
                    if recorrido.verDato()=="pendiente" or  recorrido.verDato()=="Pendiente" :
                        escrito+=estado+"|"
                    else:
                        escrito+=recorrido.verDato()+"|"
                    recorrido=recorrido.siguiente
                if recorrido==infoLibro.cola:
                    escrito += "\n"
                libroEncontrado = True
                f.write(escrito)
                
        f.close()
        if libroEncontrado:
            print("El estado del libro '"+titulo+"'se actualizó")
        else:
            print("El libro '"+titulo+"'no esta en tu colección")

    def borrarLibro(self,libroBorrado):
        libroEncontrado = False
        fr = open('DatosPrueba/Libros.txt',mode='r', encoding='utf8')
        lineas = fr.readlines()
        fr.close()
        f = open('DatosPrueba/Libros.txt',mode='w', encoding='utf8')
        for linea in lineas:
            infoLibro = estructuras.split(linea)
            titulo:str = infoLibro.cabeza.traerSiguiente().traerSiguiente().verDato()
            if infoLibro.cabeza.verDato() != self.usuario.nombreUsuario() or titulo != libroBorrado:
                f.write(linea)
            else:
                libroEncontrado = True
        if libroEncontrado:
            print("Tu libro")
                
        f.close()
        if libroEncontrado:
            print("\n-- Se ha eliminado '"+libroBorrado+"' de tu colección! --")
        else:
            print("-- Lo sentimos, el libro '"+libroBorrado+"' no se encontró en tu colección --")
    
 
