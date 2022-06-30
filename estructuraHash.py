# Estructura: Tabla Hash
class Hash:
    def __init__(self):
        self.table = [None] * 127
    
    # función hash
    def funcionHash(self, hashValue):
        key = 0
        for i in range(0,len(hashValue)):
            key += ord(hashValue[i])
        return key % 127

    def insertar(self, hashValue):
        hash = self.funcionHash(hashValue)
        if self.table[hash] is None:
            self.table[hash] = hashValue
   
    def buscar(self,hashValue):
        hash = self.funcionHash(hashValue)
        if self.table[hash] is None:
            return None
        else:
            return hex(id(self.table[hash]))
  
    def eliminar(self,hashValue):
        hash = self.funcionHash(hashValue)
        if self.table[hash] is None:
            print("No se encontró elemento con valor ", hashValue)
        else:
            print("El elemento con valor ", hashValue, "fue borrado")
            self.table[hash] = None