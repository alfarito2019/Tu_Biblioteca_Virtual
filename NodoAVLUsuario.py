import estructuras

class Nodo:
    # Constructor
	def __init__(self,valor=None):
		self.valor:estructuras.ListaEnlazada=valor
		self.key=self.valor.cabeza.verDato()
		self.hijo_izquierdo=None
		self.hijo_derecho=None
		self.padre=None # Apuntador al padre del nodo
		self.altura=1 # altura del nodo (max dist. a la hoja)
