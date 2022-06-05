from random import random,randint,uniform
import estructuras
f = open('DatosPrueba/Generar100Libros.txt',mode='a', encoding='utf8')
for i in range(0,100) :
    
    
    f.write("{usuario}|{}|{c}|{d}|{e}|{f}|{g}|{h}|{i}|"+"\n")

f.close()   