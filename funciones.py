"""
En este archivo creare las funciones necesarias para el que la cuenta bancaria pueda cumplir con las ordenes y desiciones que el usuario decida hacer
"""
#_________________________________________________________________________________

class persona():

    """
    La clase persona se encargara de recibir el nombre y el apellido de los usuarios
    """
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
#_________________________________________________________________________________
class cliente(persona):
    """
    La clase cliente se encargara de llevar el numero de cuenta y el saldo ademas de heredar la clase de persona
    """
    def __init__(self, numero_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
    
    def imprimir(self):
        return print(f"Usuario {self.nombre} {self.apellido}\nSu numero de cuenta es {self.numero_cuenta}\nSu saldo disponible es {self.saldo}")

    def depositar(self):
        deposito = float(input("Por favor ingrese el la cantidad a depositar: "))
        self.saldo = self.saldo + deposito
        return print(f"Su nuevo saldo es {self.saldo}")

    def retirar(self):
        retiro = float(input("Por favor ingrese la cantidad a retirar: "))
        if retiro < self.saldo:
            print("Lo sentimos, saldo insuficiente")
        else:
            self.saldo = self.saldo - retiro
        return print(f"Su nuevo saldo es {self.saldo}")
#___________________________________________________________________________________

def nuevo_usuario():
    print("Creación de nuevo usuario\n")
    nombre = str(input("Nombre de usuario: "))
    apellido = str(input("Apellido de usuario: "))
    return persona(nombre, apellido)

#_________________________________________________________________________________
def inicio():
    """
    Esta funcion da incio a todo el codigo manteniendo al usuario en un loop hasta que decida salir de la aplicación
    """
    def nuevo_usuario():
        pass
    
    