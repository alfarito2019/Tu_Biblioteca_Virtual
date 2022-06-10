from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox

from setuptools import Command
import Usuario
import Menu

variable=0

root=Tk()
root.title("Books 4 Dummies")

class LabelLogin():
    def createIntLogin():
                #mainFrame
        mainFrame=Frame()
        mainFrame.pack()
        mainFrame.config(width=480,height=320)
            #titulo
        titulo=Label(mainFrame,text="Books 4 Dummies",font=("Arial",24))
        titulo.grid(column=0,row=0,padx=10,pady=10,columnspan=2)
            #subtitulo
        subtit=Label(mainFrame,text="Escoge una opción",font=("Arial",14))
        subtit.grid(column=0,row=1,padx=10,pady=10,columnspan=2)
            #entrada usuario
        userLabel=Label(mainFrame,text="Usuario",font=("Arial",14))
        userLabel.grid(column=0,row=2,padx=5,pady=5,columnspan=1)
        userVariable=StringVar()
        global userEntry
        userEntry=Entry(mainFrame,textvariable=userVariable)
        userEntry.grid(column=1,row=2)
            #entrada password
        passLabel=Label(mainFrame,text="Contraseña",font=("Arial",14))
        passLabel.grid(column=0,row=3,padx=5,pady=5,columnspan=1)
        passVariable=StringVar()
        global passEntry
        passEntry=Entry(mainFrame,textvariable=passVariable,show="*")
        passEntry.grid(column=1,row=3)
            #boton log In
        logInButton=ttk.Button(mainFrame,text="Log In",command=logInstarter)
        logInButton.grid(column=0,row=4,ipadx=10,ipady=10,padx=10,pady=10)
            #boton Sign In
        signInButton=ttk.Button(mainFrame,text="Sign In",command=SignUpStarter)
        signInButton.grid(column=1,row=4,ipadx=10,ipady=10,padx=10,pady=10)

        root.mainloop()

def logInstarter():
    global username
    username = getUser()
    global password
    password = getPass()
    user1 = Usuario.usuario(username, password)            
    inicio=user1.inicioSesion()
    if inicio:
        print("Se inició sesión correctamente")
        
        menu=Menu.Menu(user1)
        root.destroy()
        menu.mostrarMenu()
        

    else:
        messagebox.showinfo(message="Usuario o contraseña incorrecta", title="advertencia")
        

def SignUpStarter():
    global username
    username = getUser()
    global password
    password = getPass()
    if username and password != FALSE:
            user1 = Usuario.usuario(username, password)

    if not user1.registro():
            messagebox.showinfo(message="Ya te encuentras registrado", title="advertencia")

    else:
            messagebox.showinfo(message="Se registro satisfactoriamente", title="advertencia")
            # print("Se registro satisfactoriamente")
            # user1.online=True
            # menu=Menu.Menu(user1)
            # menu.mostrarMenu()

def getUser():
    return userEntry.get()

def getPass():
    return passEntry.get()
