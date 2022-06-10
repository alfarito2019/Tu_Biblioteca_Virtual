from tkinter import *
from tkinter import ttk as ttk
import Opciones
import IntLogin
import Usuario
from tkinter import messagebox



def createIntMenu():
            #mainFrame
    global opciones
    opciones=Opciones.Opciones(IntLogin.user1)
    global root
    root=Tk()
    root.title("Menu Principal") 
    menuFrame=Frame()
    menuFrame.pack()
    menuFrame.config(width=480,height=320)
    
        #bienvenida
    titulo=Label(menuFrame,text="¡Al equipo de BiblioVirtual nos alegra que nos escojas para organizar tus libros!",font=("Arial",24))
    titulo.grid(column=0,row=0,padx=10,pady=10,columnspan=1)

    titulo=Label(menuFrame,text="¿Qué deseas hacer?",font=("Arial",20))
    titulo.grid(column=0,row=1,padx=10,pady=10,columnspan=1)

    logInButton=ttk.Button(menuFrame,text="Ver los libros guardados",command=mostrar)
    logInButton.grid(column=0,row=2,ipadx=10,ipady=10,padx=10,pady=10)

    logInButton=ttk.Button(menuFrame,text="Agregar un libro",command=agregar)
    logInButton.grid(column=0,row=3,ipadx=10,ipady=10,padx=10,pady=10)

    logInButton=ttk.Button(menuFrame,text="Eliminar un libro",command=eliminar)
    logInButton.grid(column=0,row=4,ipadx=10,ipady=10,padx=10,pady=10)

    logInButton=ttk.Button(menuFrame,text="Actualizar estado de un libro",command=actualizar)
    logInButton.grid(column=0,row=5,ipadx=10,ipady=10,padx=10,pady=10)

    logInButton=ttk.Button(menuFrame,text="Mis libros por leer",command=pendientes)
    logInButton.grid(column=0,row=6,ipadx=10,ipady=10,padx=10,pady=10)

    logInButton=ttk.Button(menuFrame,text="Salir",command=salir)
    logInButton.grid(column=0,row=7,ipadx=10,ipady=10,padx=10,pady=10)

    logInButton=ttk.Button(menuFrame,text="Eliminar usuario y salir",command=el_salir)
    logInButton.grid(column=0,row=8,ipadx=10,ipady=10,padx=10,pady=10)

    root.mainloop()
def mostrar():
    root.destroy()
    opciones.mostrarLibros()
def agregar():
    root.destroy()
    opciones.agregarLibros()
def eliminar():
    root.destroy()
    opciones.eliminarLibro()
def actualizar():
    root.destroy()
    opciones.actualizarLibro()
def pendientes():
    root.destroy()
    opciones.librosPorLeer()
def salir():
    root.destroy()
    opciones.salir()
    messagebox.showinfo(message="¡hasta la proxima!", title="advertencia")
def el_salir():
    root.destroy()
    opciones.eliminarUsuario()