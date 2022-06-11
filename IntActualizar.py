import tkinter as tk
from tkinter import *
from tkinter import CENTER, ttk
from turtle import width
import Opciones
import IntLogin
from tkinter import messagebox
import Menu,estructuras,IntMostrar, Usuario, BaseDatos

class Actualizar:
    def __init__(self) -> None:
        self.usuario=IntLogin.user1
    def createIntActualizar(self):
                #mainFrame
        global root
        root=tk.Tk()
                #titulo principal
        root.title("Actualizar libro")  
        titulo=tk.Label(root,text="¿Qué libro deseas actualizar?",font=("Arial",20))        
        titulo.grid(column=0,row=0,padx=10,pady=10,columnspan=2)
                #titulo
        tituloLabel=Label(root,text="titulo :",font=("Arial",14))
        tituloLabel.grid(column=0,row=1,padx=5,pady=5,columnspan=1)
        tituloVariable=StringVar()
        global tituloEntry
        tituloEntry=Entry(root,width=70 ,textvariable=tituloVariable)
        tituloEntry.grid(column=1,row=1,columnspan=1)
                #prestado?
        prestadoLabel=Label(root,text="¿Lo has prestado?",font=("Arial",14))
        prestadoLabel.grid(column=0,row=2,padx=5,pady=5,columnspan=1)
        prestadoList = ["Si","No"]
        global prestadoVariable
        prestadoVariable = tk.StringVar(root)
        prestadoVariable.set(prestadoList[0]) 
        prestadoOpt = OptionMenu(root, prestadoVariable, *prestadoList)
        prestadoOpt.config(width=70, font=('Arial', 14))
        prestadoOpt.grid(column=1,row=2,padx=5,pady=5,columnspan=2)
        #botones
                #boton volver
        volverButton=ttk.Button(root,text="volver",command=volverBoton)
        volverButton.grid(column=0,row=8,ipadx=10,ipady=10,padx=10,pady=10)
            #boton guardar
        gurdarButton=ttk.Button(root,text="Actualizar",command=actualizarBoton)
        gurdarButton.grid(column=1,row=8,ipadx=10,ipady=10,padx=10,pady=10)

def gettituloOpt():
    return tituloEntry.get()

def getPrestadoOpt():
    return prestadoVariable.get()

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

def actualizarBoton():
    res = messagebox.askquestion('Confirmación', '¿Quieres actualizar el libro?')
#     print(res)
    if res == 'yes':
        titulo=gettituloOpt()
        prestado=getPrestadoOpt()
        
        usuario=IntLogin.user1  
        baseLibros=BaseDatos.BD(usuario)
        baseLibros.actualizarBaseLibro(titulo,prestado)
        res2=messagebox.askquestion('Confirmación', '¡En hora buena! \n Has actualizado un libro \n ¿Quieres actualizar otro?')
        if res2 == 'no':
                usuario=IntLogin.user1           
                menu=Menu.Menu(usuario)
                root.destroy()
                menu.mostrarMenu()
        elif res2 == 'yes':
                return
    elif res== 'no':
        messagebox.showwarning('Advertencia',"no se ha actualizado ningún libro")
        return