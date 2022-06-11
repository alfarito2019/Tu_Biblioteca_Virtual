import tkinter as tk
from tkinter import *
from tkinter import CENTER, ttk
from turtle import width
import Opciones
import IntLogin
from tkinter import messagebox
import Menu,estructuras,IntMostrar, Usuario, BaseDatos,estructuraCola

class librosPorLeer:
    def __init__(self) -> None:
        self.usuario=IntLogin.user1
    def createIntlibrosPorLeer(self):
        
         #mainFrame
        global root
        root=tk.Tk()
                        # titulo principal
        root.title("mis libros por leer") 
        global baseLibros
        baseLibros=BaseDatos.BD(self.usuario)
        baseLibros.descargarLibros()
        listaLibros= baseLibros.getLibros()
        recorrido:estructuras.Nodo =listaLibros.cabeza
        global librosSinLeer
        librosSinLeer=estructuraCola.Cola()

        while recorrido!=None:
            
            libro:estructuras.ListaEnlazada=recorrido.verDato()
            pendiente:estructuras.Nodo=libro.cabeza.siguiente.siguiente.siguiente.siguiente.siguiente.siguiente
            if(libro.cabeza.dato==self.usuario.username and ((pendiente.verDato().lower())=="pendiente")):
                librosSinLeer.enqueue(libro.cabeza.siguiente.siguiente.verDato())  
            recorrido=recorrido.siguiente
            
        if librosSinLeer.colaVacia()==True:
            titulo=tk.Label(root,text="¡Eres un excelente lector! \n ¡Haz leido todos tus libros!",font=("Arial",20))        
            titulo.grid(column=0,row=0,padx=10,pady=10,columnspan=2)

        else:
            tituloPag=tk.Label(root,text="¿Ya leiste el siguiente libro?",font=("Arial",20))        
            tituloPag.grid(column=0,row=0,padx=10,pady=10,columnspan=3)
            global lib
            lib=librosSinLeer.verDequeue()
            libroPen=tk.Label(root,text=lib,font=("Arial",14))        
            libroPen.grid(column=1,row=1,padx=10,pady=10,columnspan=2)
                        #boton si
            siButton=ttk.Button(root,text="si",command=siBoton)
            siButton.grid(column=0,row=2,ipadx=10,ipady=10,padx=10,pady=10)
                        #boton Sign no
            noButton=ttk.Button(root,text="no",command=noBoton)
            noButton.grid(column=2,row=2,ipadx=10,ipady=10,padx=10,pady=10)
                        #boton volver
            volverButton=ttk.Button(root,text="volver",command=volverBoton)
            volverButton.grid(column=1,row=3,ipadx=10,ipady=10,padx=10,pady=10)


def siBoton():
    titulo:estructuras.Nodo = lib
    baseLibros.actualizarBaseleido(titulo,1)
    librosSinLeer.dequeue()
    messagebox.showinfo('información',"¡Excelente, bien Hecho!")

def noBoton():
    messagebox.showinfo('información',"¿Que esperas para leerlo?")

def volverBoton():
    res = messagebox.askquestion('confirmación', '¿Quieres volver al menu principal?')
#     print(res)
    if res == 'yes':
        usuario=IntLogin.user1           
        menu=Menu.Menu(usuario)
        root.destroy()
        menu.mostrarMenu()
    elif res == 'no':
        return


                #boton si
            # print("Si(1)  No(2)")
            # leido = int(input("\n  ")) 
            # if  leido == 1:
