from typing import Generic, Tuple, TypeVar, Optional
T = TypeVar("T", covariant=False, contravariant=False)

class Cola:
    # Constructor
    def __init__(self):
        self.cola = []
    
    def enqueue(self,valor):
        self.cola.append(valor)
      
    def dequeue(self):
        self.cola.pop(0)

    def buscarValor(self,valor):
        for x in self.cola:
            if x == valor:
                return True
        return False
      
     
