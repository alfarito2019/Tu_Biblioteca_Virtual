from tkinter import *
from tkinter import ttk as ttk
from IntLogin import *

variable=1
loginComando=""
#botones de inicio SignIn
def SignInButton(ubicacion):
    signInButton=ttk.Button(ubicacion,text="Sign In",command=SignUpStarter)
    signInButton.grid(column=1,row=4,ipadx=10,ipady=10,padx=10,pady=10)
            #variables de comando SignUp
def SignUpStarter():
    global variable
    variable=1
#botones de inicio Login
def LoginButton(ubicacion):
    logInButton=ttk.Button(ubicacion,text="Log In",command=logInStarter)
    logInButton.grid(column=0,row=4,ipadx=10,ipady=10,padx=10,pady=10)
        #variables de comando logIn
def logInStarter():
    global variable
    variable=2

variableMenu=7
#boton menu VerButton
def VerButton(ubicacion):
    verButton=ttk.Button(ubicacion,text="Ver los libros guardados", command=VerButtonStarter)
    verButton.grid(column=0,row=2,ipadx=10,ipady=10,padx=10,pady=10)
        #variable de comando VerButton
def VerButtonStarter():
    global variableMenu
    variableMenu=1
#boton menu AgregarButton
def AgregarButton(ubicacion):
    agregarButton=ttk.Button(ubicacion,text="Agregar un libro", command=AgregarButtonStarter)
    agregarButton.grid(column=0,row=3,ipadx=10,ipady=10,padx=10,pady=10)
        #variable de comando AgregarButton
def AgregarButtonStarter():
    global variableMenu
    variableMenu=2
#boton menu EliminarButton
def EliminarButton(ubicacion):
    eliminarButton=ttk.Button(ubicacion,text="Eliminar un libro", command=EliminarButtonStarter)
    eliminarButton.grid(column=0,row=4,ipadx=10,ipady=10,padx=10,pady=10)
        #variable de comando EliminarButton
def EliminarButtonStarter():
    global variableMenu
    variableMenu=3
#boton menu ActualizarButton
def ActualizarButton(ubicacion):
    actualizarButton=ttk.Button(ubicacion,text="Actualizar estado de un libro", command=ActualizarButtonStarter)
    actualizarButton.grid(column=0,row=5,ipadx=10,ipady=10,padx=10,pady=10)
        #variable de comando ActualizarButton
def ActualizarButtonStarter():
    global variableMenu
    variableMenu=4  
#boton menu MisLibrosButton
def MisLibrosButton(ubicacion):
    misLibrosButton=ttk.Button(ubicacion,text="Mis libros por leer", command=MisLibrosButtonStarter)
    misLibrosButton.grid(column=0,row=6,ipadx=10,ipady=10,padx=10,pady=10)
        #variable de comando MisLibrosButton
def MisLibrosButtonStarter():
    global variableMenu
    variableMenu=5
#boton menu SalirButton
def SalirButton(ubicacion):
    salirButton=ttk.Button(ubicacion,text="Salir", command=SalirButtonStarter)
    salirButton.grid(column=0,row=7,ipadx=10,ipady=10,padx=10,pady=10)
        #variable de comando SalirButton
def SalirButtonStarter():
    global variableMenu
    variableMenu=6
#boton menu SalirBorrarButton
def SalirBorrarButton(ubicacion):
    salirBorrarButton=ttk.Button(ubicacion,text="Eliminar usuario y salir", command=SalirBorrarButtonStarter)
    salirBorrarButton.grid(column=0,row=8,ipadx=10,ipady=10,padx=10,pady=10)
        #variable de comando SalirBorrarButton
def SalirBorrarButtonStarter():
    global variableMenu
    variableMenu=0




