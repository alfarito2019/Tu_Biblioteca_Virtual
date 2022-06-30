from email.mime import base
from importlib.resources import Package
from xmlrpc.client import Boolean
import time
import estructuras
import NodoAVLUsuario, estructuraArbolAVLUsuario


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
        baseUsuarios.descargarUsuariosHash()
        listaUsuarios=baseUsuarios.getUsuariosHash()
        if listaUsuarios.buscar(self.username+"|"+self.password+"|\n")==None:
            baseUsuarios.appendUsuarios(self.username,self.password)
            return True
        
        else:
            return False
    # """
    # def registro(self)->bool:
    #     baseUsuarios=BaseDatos.BD(self)
    #     baseUsuarios.descargarUsuariosHash()
    #     listaUsuarios=baseUsuarios.getUsuariosHash()
    #     if listaUsuarios.buscar(self.username)==False:
    #         baseUsuarios.appendUsuarios(self.username,self.password)
    #         return True
        
    #     else:
    #         return False
    #     """
        # baseUsuarios=BaseDatos.BD(self)
        # baseUsuarios.descargarUsuariosArbol()
        # listaUsuarios= baseUsuarios.getUsuariosArbol()
        # if listaUsuarios.buscar(self.username) == False:
        #     baseUsuarios.appendUsuarios(self.username,self.password)
        #     return True
        
        # else:
        #     return False



     #iniciar Sesion 
    def inicioSesion(self) ->bool:
        baseUsuarios=BaseDatos.BD(self)
        baseUsuarios.descargarUsuariosHash()
        listaUsuarios=baseUsuarios.getUsuariosHash()
        datos = listaUsuarios.buscar(self.username+"|"+self.password+"|\n")
        if  datos !=  None:
            self.online = True 
            return self.online
                
        else:
            return self.online
    """        
    #iniciar Sesion 
    def inicioSesion(self) ->bool:
        # baseUsuarios=BaseDatos.BD(self)
        # baseUsuarios.descargarUsuariosHash()
        # listaUsuarios=baseUsuarios.getUsuariosHash()
        # datos:
        baseUsuarios=BaseDatos.BD(self)
        baseUsuarios.descargarUsuariosHash()
        listaUsuarios= baseUsuarios.getUsuariosArbol()
        datos:NodoAVLUsuario.Nodo =  listaUsuarios.encontrar(self.username)
        if  datos !=  None: 
            if  datos.valor.cabeza.traerSiguiente().verDato() == self.password:
                self.online = True
                return self.online
        else:
            return self.online
        """



    def salirSesion(self)->bool:
        if self.online:
            self.online = False
            return True
            
        else:
            return False
            
    
    def nombreUsuario(self):
        return str(self.username)

import BaseDatos