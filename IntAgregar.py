import tkinter as tk
from tkinter import *
from tkinter import CENTER, ttk
from turtle import width
import Opciones
import IntLogin
from tkinter import messagebox
import Menu,estructuras,IntMostrar, Usuario, BaseDatos

class Agregar:
    def __init__(self) -> None:
        self.usuario=IntLogin.user1
    def createIntAgregar(self):
                #mainFrame
        global root
        root=tk.Tk()
                #titulo
        root.title("Agrega un libro")  
        titulo=tk.Label(root,text="¿Qué deseas agregar?",font=("Arial",20))        
        titulo.grid(column=0,row=0,padx=10,pady=10,columnspan=2)
                #1 quien es el autor
        autorLabel=Label(root,text="¿Quién es el autor?",font=("Arial",14))
        autorLabel.grid(column=0,row=1,padx=5,pady=5,columnspan=1)
        autorVariable=StringVar()
        global autorEntry
        autorEntry=Entry(root,width=70 ,textvariable=autorVariable)
        autorEntry.grid(column=1,row=1,columnspan=2)
                #2 cual es el titulo
        titLibroLabel=Label(root,text="¿Cuál es el titulo del libro?",font=("Arial",14))
        titLibroLabel.grid(column=0,row=2,padx=5,pady=5,columnspan=1)
        titLibroVariable=StringVar()
        global titLibroEntry
        titLibroEntry=Entry(root,width=70,textvariable=titLibroVariable)
        titLibroEntry.grid(column=1,row=2,columnspan=2)
                #3 tipo de saga
        sagaLabel=Label(root,text="Pertenece a: ",font=("Arial",14))
        sagaLabel.grid(column=0,row=3,padx=5,pady=5,columnspan=1)
        sagaList = ["Autoconclusivo","Bilogía","Trilogía","Saga","Otros"]
        global sagaVariable
        sagaVariable = tk.StringVar(root)
        sagaVariable.set(sagaList[0]) 
        sagaOpt = OptionMenu(root, sagaVariable, *sagaList)
        sagaOpt.config(width=70, font=('Arial', 14))
        sagaOpt.grid(column=1,row=3,padx=5,pady=5,columnspan=1)
                #4 tipo de tema
        temaLabel=Label(root,text="Escoge una de las siguientes: ",font=("Arial",14))
        temaLabel.grid(column=0,row=4,padx=5,pady=5,columnspan=1)
        temaList = ["Académico","Biografía","Poesía","Cuento","Novela","Fabulas","Comedia","Crónica","Ensayo","Otros"]
        global temaVariable
        temaVariable = tk.StringVar(root)
        temaVariable.set(temaList[0]) 
        temaOpt = OptionMenu(root, temaVariable, *temaList)
        temaOpt.config(width=70, font=('Arial', 14))
        temaOpt.grid(column=1,row=4,padx=5,pady=5,columnspan=1)
                #5 fisico o digital
        fisDigLabel=Label(root,text="¿Físico o digital?",font=("Arial",14))
        fisDigLabel.grid(column=0,row=5,padx=5,pady=5,columnspan=1)
        fisDigList = ["Físico","Digital"]
        global fisDigVariable
        fisDigVariable = tk.StringVar(root)
        fisDigVariable.set(fisDigList[0]) 
        fisDigOpt = OptionMenu(root, fisDigVariable, *fisDigList)
        fisDigOpt.config(width=70, font=('Arial', 14))
        fisDigOpt.grid(column=1,row=5,padx=5,pady=5,columnspan=1)
                #6 finalizado o pendiente
        finPenLabel=Label(root,text="¿Finalizado o pendiente?",font=("Arial",14))
        finPenLabel.grid(column=0,row=6,padx=5,pady=5,columnspan=1)
        finPenList = ["Finalizado","Pendiente"]
        global finPenVariable
        finPenVariable = tk.StringVar(root)
        finPenVariable.set(finPenList[0]) 
        finPenOpt = OptionMenu(root, finPenVariable, *finPenList)
        finPenOpt.config(width=70, font=('Arial', 14))
        finPenOpt.grid(column=1,row=6,padx=5,pady=5,columnspan=2)
                #7 prestado
        prestLabel=Label(root,text="¿Lo has prestado?",font=("Arial",14))
        prestLabel.grid(column=0,row=7,padx=5,pady=5,columnspan=1)
        prestList = ["Si","No"]
        global prestVariable
        prestVariable = tk.StringVar(root)
        prestVariable.set(prestList[0]) 
        prestOpt = OptionMenu(root, prestVariable, *prestList)
        prestOpt.config(width=70, font=('Arial', 14))
        prestOpt.grid(column=1,row=7,padx=5,pady=5,columnspan=2)
                #boton volver
        volverButton=ttk.Button(root,text="volver",command=volverBoton)
        volverButton.grid(column=0,row=8,ipadx=10,ipady=10,padx=10,pady=10)
            #boton guardar
        gurdarButton=ttk.Button(root,text="Guardar",command=guardarBoton)
        gurdarButton.grid(column=1,row=8,ipadx=10,ipady=10,padx=10,pady=10)


def getAutorEntry():
    return autorEntry.get()

def getTitLibroEntryOpt():
    return titLibroEntry.get()

def getSagaOpt():
    return sagaVariable.get()

def getTemaOpt():
    return temaVariable.get()

def getfisDigOpt():
    return fisDigVariable.get()

def getFinPenOpt():
    return finPenVariable.get()

def getPrestOpt():
    return prestVariable.get()

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

def guardarBoton():
    res = messagebox.askquestion('Confirmación', '¿Quieres guardar el libro?')
#     print(res)
    if res == 'yes':
        autor=getAutorEntry()
        titlulo=getTitLibroEntryOpt()
        extension=getSagaOpt()
        genero=getTemaOpt()
        formato=getfisDigOpt()
        estadodeLectura=getFinPenOpt()
        prestado=getPrestOpt()
        
        usuario=IntLogin.user1  
        baseLibros=BaseDatos.BD(usuario)
        baseLibros.appendLibros(autor,titlulo,extension,genero,formato,estadodeLectura,prestado)
        res2=messagebox.askquestion('Confirmación', '¡En hora buena! \n Has guardado un libro \n ¿Quieres guardar otro?')
        if res2 == 'no':
                usuario=IntLogin.user1           
                menu=Menu.Menu(usuario)
                root.destroy()
                menu.mostrarMenu()
        elif res2 == 'yes':
                return
    elif res== 'no':
        messagebox.showwarning('Advertencia',"no se ha guardado ningún libro")
        return


