from email.mime import base
from importlib.resources import Package
from xmlrpc.client import Boolean
import time
import estructuras,BaseDatos

class usuario():
    #constructor
    def __init__(self, username, password ) -> None:
        self.username = username
        self.password = password
        self.online = False
        self.intentos = 3
        
    
    #Registrarse

    def registro(self)->bool:
        inicio = time.perf_counter()
        baseUsuarios=BaseDatos.BD(self)
        baseUsuarios.descargarUsuarios()
        listaUsuarios= baseUsuarios.getUsuarios()
        confirmacion=True
        recorrido:estructuras.Nodo =listaUsuarios.cabeza
        while recorrido!=None:
            minilista:estructuras.ListaEnlazada=recorrido.verDato()
            
            if minilista.cabeza.dato==self.username:
                confirmacion=False
                break
            recorrido=recorrido.siguiente

                
        if(confirmacion):
            baseUsuarios.appendUsuarios(self.username,self.password)
            final  = time.perf_counter()
            print(final - inicio )
            return True
            
        else:
            return False


    #iniciar Sesion 
    def inicioSesion(self) ->bool:
        inicio = time.perf_counter()
        baseUsuarios=BaseDatos.BD(self)
        baseUsuarios.descargarUsuarios()
        listaUsuarios= baseUsuarios.getUsuarios()
        confirmacion=False
        recorrido:estructuras.Nodo =listaUsuarios.cabeza
        while recorrido!=None:
            minilista:estructuras.ListaEnlazada=recorrido.verDato()
            if minilista.cabeza.verDato()==self.username and minilista.cabeza.verDato() != None:
                if minilista.cola.verDato()==self.password:
                    confirmacion=True
                    self.online=True
                    break
            recorrido=recorrido.siguiente
        final  = time.perf_counter()
        print(final - inicio )
        return confirmacion
        


    def salirSesion(self)->bool:
        inicio = time.perf_counter()
        if self.online:
            self.online = False
            final  = time.perf_counter()
            print(final - inicio )
            return True
            
        else:
            final  = time.perf_counter()
            print(final - inicio )
            return False
            
    
    def nombreUsuario(self):
        return str(self.username)


