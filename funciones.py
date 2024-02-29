
class Persona:

    """
    La clase persona se encargara de recibir el nombre y el apellido de los usuarios
    """
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
#_________________________________________________________________________________
class Cliente(Persona):
    """
    La clase cliente se encargara de llevar el numero de cuenta y el saldo ademas de heredar la clase de persona
    """
    def __init__(self, nombre, apellido, numero_cuenta, saldo = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
    
    def __str__ (self):
        return f"Cliente: {self.nombre} {self.apellido}\nSaldo de cuenta: {self.numero_cuenta}: ${self.saldo}"

    def depositar(self, deposito):
        self.saldo += deposito
        print("Deposito aceptado")

    def retirar(self, retiro):
        if self.saldo >= retiro:
            self.saldo -= retiro
            print("Retiro exitoso")
        else:
            print("Fondo insuficiente")
#___________________________________________________________________________________

def nuevo_usuario():
    """
    Esta funcion se encargara de crear a los nuevos usuarios y devolverlos como clientes
    """
    
    print("Registro de nuevo usuario\n")
    nombre_usuario = str(input("Nombre de usuario: "))
    apellido_usuario = str(input("Apellido de usuario: "))
    numero_cuenta = int(input("Ingrese su numero de cuenta: "))
    cliente = Cliente(nombre_usuario, apellido_usuario, numero_cuenta)
    return cliente
#_________________________________________________________________________________
def inicio():
    """
    Esta funcion da incio a todo el codigo manteniendo al usuario en un loop hasta que decida salir de la aplicación
    """
    usuario = nuevo_usuario()
    print(usuario)
    opcion = 0

    while opcion != 'S':
        print("Elige una opcion:\nDepositar (D)\nRetirar (R)\nSalir (S)")
        opcion = str.upper(input())

        if opcion == 'D':
            monto_deposito = int(input("Ingrese cantidad a depositar: "))
            usuario.depositar(monto_deposito)
        elif opcion == 'R':
            monto_retiro = int(input("Ingrese cantidad a retirar: "))
            usuario.retirar(monto_retiro)
        print(usuario)
    
    print("Gracias por operar con nuestro banco")

    