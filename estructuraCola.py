from typing import Generic, Tuple, TypeVar, Optional
T = TypeVar("T", covariant=False, contravariant=False)

class Cola:
    # Constructor
    def __init__(self):
        self.cola = []
    
    # Agraga dato al final
    def enqueue(self,dato):
        self.cola.append(dato)
      
    # Elimina y obtiene el primer dato de la cola o False si no hay ninguno
    def dequeue(self):
        if self.colaVacia():
            return False
        sacado = self.cola.pop(0)
        return sacado

    # Retorna True si el dato dado se encuentra en la cola
    def buscarDato(self,dato):
        for x in self.cola:
            if x == dato:
                return True
        return False

    # Obtiene la cantidad de datos dentro de la cola
    def tamañoCola(self):
        return len(self.cola)

    # Retorna True si la cola esta vacia
    def colaVacia(self):
        if self.tamañoCola() == 0:
            return True
        return False
    
    # Imprime la cola
    def verCola(self):
        print(self.cola)

    #Mostrar el dato que se desencolaria  
    def verDequeue(self):
        if self.colaVacia():
            return False
        return  self.cola(0)
