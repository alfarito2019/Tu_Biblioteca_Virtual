
from typing import Generic, Tuple, TypeVar, Optional
T = TypeVar("T", covariant=False, contravariant=False)

class Nodo:
    # Constructor
    def __init__(self,datoN)->None:
        self.dato = datoN
        self.siguiente = None

    # Obtiene el dato
    def verDato(self):
        return self.dato
    
    # Obtiene el dato siguiente
    def traerSiguiente(self):
        return self.siguiente

    # Actualiza el dato a uno dado
    def entrarDato(self,datoNuevo):
        self.dato = datoNuevo

    # Agrega dato al siguiente
    def colocarSiguiente(self,sigNuevo):
        self.siguiente = sigNuevo


class ListaEnlazada:
    # Constructor
    def __init__(self):
        self.cabeza = None
        self.cola = None

    # Devuelve (True) si la lista esta vacia
    def estarVacia(self):
        return self.cabeza == None

    # Agrega un valor a la lista al final
    def agregar(self,dato):
        nuevoValor = Nodo(dato)
        if self.estarVacia():
            self.cola= nuevoValor
            self.cabeza=nuevoValor
        else:
            self.cola.colocarSiguiente(nuevoValor)
            self.cola=nuevoValor

    # Cuenta los elementos de la lista
    def cantidad(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador += 1
            actual = actual.traerSiguiente()
        return contador

    # Imprime cada valor de la lista de esta manera: (-->[x]-->[y]-->[z])
    def verLista(self):
        actual = self.cabeza
        cadena = ""
        while actual != None:
            cadena += "->"+"["+str(actual.verDato())+"]"
            actual = actual.traerSiguiente()
        print(cadena)

    # Retorna (True) si el valor dado esta en la lista
    def buscar(self,dato):
        actual = self.cabeza
        while actual != None:
            if (dato == actual.verDato()):
                return True
            else:
                actual = actual.traerSiguiente()
            return False

    # Busca el valor dado (dato) y lo excluye de la lista
    def borrar(self,dato):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado:
            if(actual != None):
                if(actual.verDato() == dato):
                    encontrado = True
                else:
                    previo = actual
                    actual = actual.traerSiguiente()
            else:
                break
        if (actual != None):
            if (previo == None):
                self.cabeza = actual.siguiente()
            else:
                previo.colocarSiguiente(actual.traerSiguiente())
    
    
def split(texto:str):
    currentToken = ""
    mini_lista =   ListaEnlazada()
    for c in texto:
        
        if c == "|" :
            mini_lista.agregar( currentToken)  
            currentToken = ""
            c=""
        currentToken += c
        
    return mini_lista

        
            

