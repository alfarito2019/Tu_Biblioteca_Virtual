import estructuras
class BD():
    
    def __init__(self):
        self.base_usuarios= estructuras.ListaEnlazada() 
        self.base_libros= estructuras.ListaEnlazada()
        

    def descargarUsuarios(self)-> None:
        f = open ('Usuarios.txt','r')
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
        f = open ('Usuarios.txt','a')
        f.write(username,password)        
        f.close()

    def getUsuarios(self)-> estructuras.ListaEnlazada:
        return self.base_usuarios

    def appendUsuarios(self, username, password)->bool:
        f = open ('Usuarios.txt','a')
        f.write(username+","+password+",")
        f.close()


    def descargarLibros(self)-> None:
        f = open ('Libros.txt','r')
        while(True):
            #leer la siguiente linea
            linea = f.readline()
            #revisar si la linea no es null
            if not linea:
                break
            #terminamos de leer el archivo 
            self.base_libros.agregar(linea)

        f.close()
        
        
    def cargarLibros(self,username,password)-> bool:    
        f = open ('Usuarios.txt','a')
        f.write(username,password)        
        f.close()

    def getLibros(self)-> estructuras.ListaEnlazada:
        return self.base_libros 


    def appendLibros(self, username, password)->bool:
        f = open ('Usuarios.txt','a')
        f.write(username+","+password+",")
        f.close()   

    
