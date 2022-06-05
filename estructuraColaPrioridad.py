from estructuras import ListaEnlazada

# Diseño de Colas de prioridad

class ColaPrioridad:
    def __init__(self):
        self.cola = []

    def estaVacia(self):
        return self.cola == []

    def encolar(self,dato):
        self.cola.append(dato)

    def desencolar(self):
        maximo = 0
        posicion = 0
        for n in self.cola:
            prioridad = int(n.cabeza.verDato())
            if prioridad > maximo:
                maximo = n.cabeza.verDato()
                maxPrior = posicion
            posicion += 1
        dato = self.cola[maxPrior]
        self.cola.pop(maxPrior)
        return dato

    def verCola(self):
        for n in self.cola:
            n.verLista()
