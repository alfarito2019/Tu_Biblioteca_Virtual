from tkinter import *
from tkinter import ttk as ttk
from Opciones import *
from IntBoton import *


def createIntMenu():
            #mainFrame
    IntMenu=Tk()
    IntMenu.title("Menu Principal")        
    menuFrame=Frame()
    menuFrame.pack()
    menuFrame.config(width=480,height=320)
        #bienvenida
    titulo=Label(menuFrame,text="¡Al equipo de BiblioVirtual nos alegra que nos escojas para organizar tus libros!",font=("Arial",24))
    titulo.grid(column=0,row=0,padx=10,pady=10,columnspan=1)

    titulo=Label(menuFrame,text="¿Qué deseas hacer?",font=("Arial",20))
    titulo.grid(column=0,row=1,padx=10,pady=10,columnspan=1)

    VerButton(menuFrame)
    # verButton=ttk.Button(menuFrame,text="Ver los libros guardados")
    # verButton.grid(column=0,row=2,ipadx=10,ipady=10,padx=10,pady=10)
    AgregarButton(menuFrame)
    # agregarButton=ttk.Button(menuFrame,text="Agregar un libro")
    # agregarButton.grid(column=0,row=3,ipadx=10,ipady=10,padx=10,pady=10)
    EliminarButton(menuFrame)
    # eliminarButton=ttk.Button(menuFrame,text="Eliminar un libro")
    # eliminarButton.grid(column=0,row=4,ipadx=10,ipady=10,padx=10,pady=10)
    ActualizarButton(menuFrame)
    # actualizarButton=ttk.Button(menuFrame,text="Actualizar estado de un libro")
    # actualizarButton.grid(column=0,row=5,ipadx=10,ipady=10,padx=10,pady=10)
    MisLibrosButton(menuFrame)
    # misLibrosButton=ttk.Button(menuFrame,text="Mis libros por leer")
    # misLibrosButton.grid(column=0,row=6,ipadx=10,ipady=10,padx=10,pady=10)
    SalirButton(menuFrame)
    # salirButton=ttk.Button(menuFrame,text="Salir")
    # salirButton.grid(column=0,row=7,ipadx=10,ipady=10,padx=10,pady=10)
    SalirBorrarButton(menuFrame)
    # salirBorrarButton=ttk.Button(menuFrame,text="Eliminar usuario y salir")
    # salirBorrarButton.grid(column=0,row=8,ipadx=10,ipady=10,padx=10,pady=10)
