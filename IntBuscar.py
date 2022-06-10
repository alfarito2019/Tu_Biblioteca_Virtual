import tkinter as tk
from tkinter import CENTER, ttk
from turtle import width
import Opciones
import IntLogin
from tkinter import messagebox
import Menu,estructuras,IntMostrar

class Buscar:
    def __init__(self) -> None:
        self.usuario=IntLogin.user1
    def createIntBuscar(self):
                #mainFrame
        global root
        root=tk.Tk()
        root.title("Libros encontrados")  
        titulo=tk.Label(root,text="Buscador de Libros",font=("Arial",24))
        titulo.pack(side=tk.TOP)
        scrollbar=tk.Scrollbar(root)
        c=tk.Canvas(root,yscrollcommand=scrollbar.set,width=560)
        scrollbar.config(command=c.yview)
        scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        mostrarFrame=tk.Frame(c,width=560)
        c.pack(side="left",fill="both",expand=True)
        c.create_window(0,0,window=mostrarFrame,anchor="nw")
        libroLabel=tk.Label(mostrarFrame,text="Libro",font=("Arial",14))
        libroLabel.pack()
        libroVariable=tk.StringVar()
        global libroEntry
        libroEntry=tk.Entry(mostrarFrame,textvariable=libroVariable)
        libroEntry.pack()
        butBuscar=ttk.Button(mostrarFrame,text="Buscar un libro",command=buscar)
        butBuscar.pack()
        butVolver=ttk.Button(mostrarFrame,text="Volver",command=Volver)
        butVolver.pack()
        root.update()
        c.config(scrollregion=c.bbox("all"))
        root.mainloop
def buscar():
    listaLibros= Menu.baseLibros.getLibrosArbol()
    datoslibro=listaLibros.encontrar(getTitulo())
    if datoslibro != None:
        lista:estructuras.ListaEnlazada=datoslibro.valor 
        
        messagebox.showinfo(message=lista.verLista(), title="Libro encontrado")
            
    else:
        messagebox.showinfo(message="Por ahora no posees este libro", title="advertencia")

def Volver():
    root.destroy()
    mostrar=IntMostrar.Mostrar()
    mostrar.createIntMostrar()

def getTitulo():
    return libroEntry.get()