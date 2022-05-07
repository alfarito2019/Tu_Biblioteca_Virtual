
import estructuras,Menu

import Usuario
if __name__ == '__main__':
        print("Esocoja una opcion ")
        print("1.Registrarse")
        print("2.Iniciar Sesión")
        variable  = int(input().strip())
        if variable ==1: #escogio registrarse
                print("Registrandose")
                username = input("Ingrese su usario: ")
                password = input("Ingrese su contraseña: ")
                user1 = Usuario.usuario(username, password)
                if user1.registro() == False:
                        print("Ya te encuentras registrado")
                else:
                        print("Se registro satisfactoriamente")
                
        else: #Escogió iniciar sesion
                username = input("Ingrese su usario: ")
                password = input("Ingrese su contraseña: ")     
                user1 = Usuario.usuario(username, password)            
                inicio=user1.inicioSesion()
                
                if inicio:
                        print("Se inició sesión correctamente")
                        Menu.Menu.mostrarMenu()

                else:
                        print("Usuario o contraseña incorrecta")
