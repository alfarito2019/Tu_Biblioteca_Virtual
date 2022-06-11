from pickle import FALSE
import Menu
import estructuraPila
#import timeort time
import Usuario
import IntLogin
from tkinter import messagebox


if __name__ == '__main__':
        
        IntLogin.LabelLogin.createIntLogin()

# '''

'''

        if IntLogin.variable==1: #escogio registrarse
                username = IntLogin.varUser
                password = IntLogin.varPass
                if username and password != FALSE:
                        user1 = Usuario.usuario(username, password)


#         if IntLogin.variable==1: #escogio registrarse
#                 username = IntLogin.varUser
#                 password = IntLogin.varPass
#                 if username and password != FALSE:
#                         user1 = Usuario.usuario(username, password)

#                 if not user1.registro():
#                         response=messagebox.showinfo(message="Ya te encuentras registrado", title="advertencia")
#                         print(response)
#                 else:
#                         response=messagebox.showinfo(message="Se registro satisfactoriamente", title="advertencia")
#                         print(response)
#                         # print("Se registro satisfactoriamente")
#                         # user1.online=True
#                         # menu=Menu.Menu(user1)
#                         # menu.mostrarMenu()
                
#         else: #Escogió iniciar sesion
#                 username = IntLogin.varUser
#                 password = IntLogin.varPass  
#                 user1 = Usuario.usuario(username, password)            
#                 inicio=user1.inicioSesion()
                
#                 if inicio:
#                         print("Se inició sesión correctamente")
                        

#                         menu=Menu.Menu(user1)
#                         menu.mostrarMenu()
#                         IntLogin.root.destroy()

#                 else:
#                         print("Usuario o contraseña incorrecta")
# '''
                        menu=Menu.Menu(user1)
                        menu.mostrarMenu()
                        IntLogin.root.destroy()

                else:
                        print("Usuario o contraseña incorrecta")
'''

