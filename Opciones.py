import Usuario,Agregar,Mostrar,Eliminar,Actualizar,Pendientes,Buscar


class Opciones:
    decision=0
    global baseLibros

    def __init__(self,user:Usuario.usuario) -> None:
        self.usuario=user

    def mostrarLibros(self)->None:
        mostrar=Mostrar.Operacion1(self.usuario)
        mostrar.mostrarLibros()
            
    ##Configurar metodo para agregar busqueda de libros
    def buscarLibro(self)->None:
        buscar=Buscar.Operacion1_1(self.usuario)
        buscar.buscarLibro()

    def agregarLibros(self):
        agregar=Agregar.Operacion2(self.usuario)
        agregar.agregarLibros()

    def eliminarLibro(self):
        eliminar=Eliminar.Operacion3(self.usuario)
        eliminar.eliminarLibro()
        
    def actualizarLibro(self): 
        actualizar=Actualizar.Operacion4(self.usuario)
        actualizar.actualizarLibro()

    def librosPorLeer(self):
        porleer=Pendientes.Operacion5(self.usuario)
        porleer.librosPorLeer()

    def eliminarUsuario(self):
        eliminar=Eliminar.Operacion0(self.usuario)
        eliminar.eliminarUsuario()