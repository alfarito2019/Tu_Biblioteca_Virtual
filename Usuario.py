from email.mime import base
from importlib.resources import Package
from xmlrpc.client import Boolean

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
            return True
        else:
            return False

    #iniciar Sesion 
    def inicioSesion(self) ->bool:
        baseUsuarios=BaseDatos.BD(self)
        baseUsuarios.descargarUsuarios()
        listaUsuarios= baseUsuarios.getUsuarios()
        confirmacion=False
        recorrido:estructuras.Nodo =listaUsuarios.cabeza
        while recorrido!=None:
            minilista:estructuras.ListaEnlazada=recorrido.verDato()

            if minilista.cabeza.dato==self.username:
                if minilista.cola.dato==self.password:
                    confirmacion=True
                    self.online=True
            recorrido=recorrido.siguiente
        

        return confirmacion
    def salirSesion(self)->bool:
        if self.online:
            self.online = False
            return True
            
        else:
            return False

    
    def nombreUsuario(self):
        return str(self.username)


