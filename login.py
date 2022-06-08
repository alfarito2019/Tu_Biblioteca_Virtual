from crearLabel import *
from Usuario import usuario

# def createGUI():
        #ventana principal
root = Tk()
root.title("Books 4 Dummies")

        #mainFrame
mainFrame=Frame()
mainFrame.pack()
mainFrame.config(width=480, height=320)#,bg="lightblue")

titulo=crearLabel(mainFrame,"¡Bienvenido a Books 4 Dummies!","Arial",24,0,0,10,10,2)
titulo.plainText()
opcionLabel=crearLabel(mainFrame,"Escoge una opción","Arial",16,0,1,10,10,2)
opcionLabel.plainText()

        #Usuario
nombreLabel= crearLabel(mainFrame,"Usuario: ","Arial", 14,0,2,5,5,1)
nombreLabel.textEntry(False)
dato=nombreLabel.textEntry
        #contraseña
passLabel=crearLabel(mainFrame, "Contraseña: ","Arial",14,0,3,5,5,1)
passLabel.textEntry(True)

        #botones
logInButton=crearLabel(mainFrame, "Log In","Arial", 14,1,4,10,10,1)
logInButton.boton(5,5)

signUpButton=crearLabel(mainFrame, "Sign Up","Arial", 14,0,4,10,10,1)
signUpButton.boton(5,5)

root.mainloop()