import tkinter as tk
from tkinter import CENTER, ttk
from turtle import width
import Opciones
import IntLogin
import Menu,estructuras

class Mostrar:
    def __init__(self) -> None:
        self.usuario=IntLogin.user1
    def createIntMostrar(self):
                #mainFrame
        
        root=tk.Tk()
        root.title("Libros encontrados")  
        titulo=tk.Label(root,text="Books 4 Dummies",font=("Arial",24))
        titulo.pack(side=tk.TOP)
        scrollbar=tk.Scrollbar(root)
        c=tk.Canvas(root,yscrollcommand=scrollbar.set,width=560)
        scrollbar.config(command=c.yview)
        scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        mostrarFrame=tk.Frame(c,width=560)
        c.pack(side="left",fill="both",expand=True)
        c.create_window(0,0,window=mostrarFrame,anchor="nw")
        tablaLibros=ttk.Treeview(mostrarFrame, columns=("Col1","Col2","Col3","Col4","Col5","Col6"))
        tablaLibros.column("#0",width=80)
        tablaLibros.column("Col1",width=80, anchor=CENTER)
        tablaLibros.column("Col2",width=80, anchor=CENTER)
        tablaLibros.column("Col3",width=80, anchor=CENTER)
        tablaLibros.column("Col4",width=80, anchor=CENTER)
        tablaLibros.column("Col5",width=80, anchor=CENTER)
        tablaLibros.column("Col6",width=80, anchor=CENTER)

        tablaLibros.heading("#0", text="Autor",anchor=CENTER)
        tablaLibros.heading("Col1", text="Titulo",anchor=CENTER)
        tablaLibros.heading("Col2", text="Autoconclusivo...",anchor=CENTER)
        tablaLibros.heading("Col3", text="Genero",anchor=CENTER)
        tablaLibros.heading("Col4", text="Formato",anchor=CENTER)
        tablaLibros.heading("Col5", text="Estado",anchor=CENTER)
        tablaLibros.heading("Col6", text="Prestado",anchor=CENTER)
        listaLibros= Menu.baseLibros.getLibros()
        recorrido:estructuras.Nodo =listaLibros.cabeza
        
        
        while recorrido!=None:
            libro:estructuras.ListaEnlazada=recorrido.verDato()
            if(libro.cabeza.dato==self.usuario.username):
                recorrido2:estructuras.Nodo =libro.cabeza.siguiente
                contador=0
                while recorrido2!=None:
                    if contador==0:
                        autor=recorrido2.verDato()
                    elif contador==1:
                        title=recorrido2.verDato()
                    elif contador==2:
                        conclusividad=recorrido2.verDato()
                    elif contador==3:
                        genero=recorrido2.verDato()
                    elif contador==4:
                        formato=recorrido2.verDato()
                    elif contador==5:
                        estado=recorrido2.verDato()
                    elif contador==6:
                        prestado=recorrido2.verDato()
                    recorrido2=recorrido2.siguiente
                    contador+=1
                tablaLibros.insert("",tk.END,text=autor,values=(title,conclusividad,genero,formato,estado,prestado))
            recorrido=recorrido.siguiente
        
        tablaLibros.pack()
        butBuscar=ttk.Button(mostrarFrame,text="Buscar un libro",command=buscar)
        butBuscar.pack()
        root.update()
        c.config(scrollregion=c.bbox("all"))
        root.mainloop
def buscar():
    opcion=Opciones.Opciones(IntLogin.user1)
    opcion.buscarLibro()
