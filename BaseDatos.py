import estructuras
import Usuario

class BD():
    
    def __init__(self,usuario:Usuario.usuario):
        self.base_usuarios= estructuras.ListaEnlazada() 
        self.base_libros= estructuras.ListaEnlazada()
        self.usuario=usuario
        

    def descargarUsuarios(self)-> None:
        f = open ('DatosPrueba/Usuarios.txt','r')
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
        f = open ('DatosPrueba/Usuarios.txt','a')
        f.write(username,password)        
        f.close()

    def getUsuarios(self)-> estructuras.ListaEnlazada:
        return self.base_usuarios

    def appendUsuarios(self, username, password)->bool:
        f = open ('DatosPrueba/Usuarios.txt','a')
        f.write(username+"|"+password+"|\n")
        f.close()


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
        
        
    def cargarLibros(self,username,password)-> bool:    
        f = open ('DatosPrueba/Usuarios.txt','a')
        f.write(username,password)        
        f.close()

    def getLibros(self)-> estructuras.ListaEnlazada:
        return self.base_libros 


    def appendLibros(self,autor,titlulo,extension,genero,formato,estadodelectura,prestado)->bool:
        
        userName = self.usuario.nombreUsuario()
        f = open ('DatosPrueba/Libros.txt',mode='a', encoding='utf8')
        f.write("{a}|{b}|{c}|{d}|{e}|{f}|{g}|{h}|".format(a=userName,b=autor,c=titlulo,d=extension,e=genero,f=formato,g=estadodelectura,h=prestado)+"\n")
        f.close()   

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
                
        f.close()
        if libroEncontrado:
            print("\n-- Se ha eliminado '"+libroBorrado+"' de tu colección! --")
        else:
            print("-- Lo sentimos, el libro '"+libroBorrado+"' no se encontró en tu colección --")
    
