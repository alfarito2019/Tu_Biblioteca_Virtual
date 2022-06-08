import Menu
import estructuraPila
#import timeort time
import Usuario
from IntLogin import *


if __name__ == '__main__':
        createGUI()
        print("Esocoja una opcion ")
        print("1.Registrarse")
        print("2.Iniciar Sesión")
        variable  = int(input().strip())
        if variable ==1: #escogio registrarse
                print("Registrandose")
                username = input("Ingrese su usuario: ")
                password = input("Ingrese su contraseña: ")
                user1 = Usuario.usuario(username, password)

                if not user1.registro():
                        print("Ya te encuentras registrado")
                else:
                        print("Se registro satisfactoriamente")
                        user1.online=True
                        menu=Menu.Menu(user1)
                        menu.mostrarMenu()
                
        else: #Escogió iniciar sesion
                username = input("Ingrese su usario: ")
                password = input("Ingrese su contraseña: ")     
                user1 = Usuario.usuario(username, password)            
                inicio=user1.inicioSesion()
                
                if inicio:
                        print("Se inició sesión correctamente")
                        menu=Menu.Menu(user1)
                        menu.mostrarMenu()

                else:
                        print("Usuario o contraseña incorrecta")

