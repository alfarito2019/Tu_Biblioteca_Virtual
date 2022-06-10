from tkinter import *
from tkinter import ttk as ttk
dato_cuadro=""
class crearLabel():
    
    def __init__(self,ubicacion,texto,fuente,tamaño,columna,
                fila,padX,padY,columnSpan):
        self.ubicacion=ubicacion
        self.texto=texto
        self.fuente=fuente
        self.tamaño=tamaño
        self.columna=columna
        self.fila=fila
        self.padX=padX
        self.padY=padY
        self.columnSpan=columnSpan
#titulos y subtitulos
    def plainText(self):       
        self.titulo=Label(self.ubicacion,text=self.texto,
                        font=(self.fuente,self.tamaño))
        self.titulo.grid(column=self.columna,row=self.fila,
                        padx=self.padX,pady=self.padX,columnspan=self.columnSpan)
#Entradas de texto
    def textEntry(self,passw):
        self.titulo=Label(self.ubicacion,text=self.texto,
                        font=(self.fuente,self.tamaño))
        self.titulo.grid(column=self.columna,row=self.fila,
                        padx=self.padX,pady=self.padX,columnspan=self.columnSpan)
        self.columnaE=self.columna+1
        self.filaE=self.fila
        self.variableText=StringVar()


        
        
        self.passw=passw
    #si pass=true la entrada se ocultara para contraseñas
        if self.passw==True:
            self.entrada=Entry(self.ubicacion,textvariable=self.variableText,show="*")
        else:
            self.entrada=Entry(self.ubicacion,textvariable=self.variableText)
        self.entrada.grid(column=self.columnaE,row=self.filaE)
        dato_cuadro=self.variableText.get()
#botones
    def boton(self,ipadX,ipadY):
        self.ipadX=ipadX
        self.ipadY=ipadY
        self.button=ttk.Button(self.ubicacion,text=self.texto)
        self.button.grid(column=self.columna,row=self.fila,ipadx=self.ipadX,
                        ipady=self.ipadY,padx=self.padX,pady=self.padY)


