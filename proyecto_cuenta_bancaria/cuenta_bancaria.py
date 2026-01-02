from os import system
from random import randint

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
        
    def __str__(self):
        return f'''
              Los datos del cliente son:
              Nombre Completo: {self.nombre.capitalize()} {self.apellido.capitalize()}
              Número de cuenta: {self.numero_cuenta}
              Balance: ${self.balance}'''
        
    def depositar(self):
        agregar_cuenta = int(input("Ingrese cuanto dinero quiere agregar a su cuenta: "))
        self.balance = self.balance + agregar_cuenta
        print(f"Ha agregado a su cuenta ${agregar_cuenta}. Su saldo actual es de ${self.balance}")
        
    def retirar(self):
        if self.balance == 0:
            print("No puede realizar esta operación. Aún no tiene dinero en su cuenta.")
        else:
            retirar_cuenta = int(input("Ingrese cuanto dinero desea retirar de su cuenta: "))
            if retirar_cuenta > self.balance:
                print(f"Fondos insuficientes. Su saldo actual es: ${self.balance}")
            else:
                self.balance = self.balance - retirar_cuenta
                print(f"Ha retirado ${retirar_cuenta}. Su saldo actual es: ${self.balance}")

def crear_cliente():
    nombre = input("Por favor ingrese su nombre: ")
    apellido = input("Por favor ingrese su apellido: ")
    numero_cuenta = randint(10000000, 99999999)
    balance = 0
    print("Gracias por la información. Hemos creado con éxito su usuario. Por favor agregue dinero a su cuenta")
    return Cliente(nombre, apellido, numero_cuenta, balance)
    
def inicio(usuario1):
    while True:
        eleccion = int(input(f'''Bienvenido! {usuario1.nombre} {usuario1.apellido} por favor elija una opción (del 1 al 4):
    1. Consulta de cuenta
    2. Depositar dinero
    3. Retirar dinero
    4. Salir
    '''))
        
        if eleccion == 1:
            system('cls')
            print(str(usuario1))
        
        if eleccion == 2:
            system('cls')
            usuario1.depositar()
        
        if eleccion == 3:
            system('cls')
            usuario1.retirar()
        if eleccion == 4:
            system('cls')
            print("Saliendo del programa...")
            break
            

usuario1 = crear_cliente()
inicio(usuario1)
