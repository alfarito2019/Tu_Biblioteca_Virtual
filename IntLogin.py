from tkinter import *
from tkinter import ttk as ttk

def createGUI():
    root=Tk()
    root.title("Books 4 Dummies")

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
    userEntry=Entry(mainFrame,textvariable=userVariable)
    userEntry.grid(column=1,row=2)
        #entrada password
    passLabel=Label(mainFrame,text="Contraseña",font=("Arial",14))
    passLabel.grid(column=0,row=3,padx=5,pady=5,columnspan=1)
    passVariable=StringVar()
    passEntry=Entry(mainFrame,textvariable=passVariable,show="*")
    passEntry.grid(column=1,row=3)
        #boton log In
    logInButton=ttk.Button(mainFrame,text="Log In")
    logInButton.grid(column=0,row=4,ipadx=10,ipady=10,padx=10,pady=10)
        #boton Sign In
    signInButton=ttk.Button(mainFrame,text="Sign In")
    signInButton.grid(column=1,row=4,ipadx=10,ipady=10,padx=10,pady=10)

    root.mainloop()
