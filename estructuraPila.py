
class Pila:
    # constructor
    def __init__(self):
        self.pila = []
    
    # Agraga dato al final de la pila
    def push(self,dato):
        self.pila.append(dato)
    
    # Elimina y obtiene el ultimo dato de la pila o False si no hay ninguno
    def pop(self):
        if self.pilaVacia():
            return False
        else:
            sacado = self.pila.pop()
            return sacado

    # Obtiene la cantidad de datos dentro de la pila
    def tamañoPila(self):
        return len(self.pila)

    # retorna True si la pila esta vacia
    def pilaVacia(self):
        if self.tamañoPila() == 0:
            return True
        return False

    # Retorna el ultimmo dato de la pila o False si esta vacia
    def top(self):
        if self.pilaVacia():
            return False
        ultimoDato = (self.tamañoPila())-1
        return self.pila[ultimoDato]

    # Imprime la pila
    def verPila(self):
        print(self.pila)
