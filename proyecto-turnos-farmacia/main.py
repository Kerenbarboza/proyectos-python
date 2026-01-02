from os import system
from turnos import turno_farmacia, turno_perfumeria, turno_cosmetiquero
def menu():
    print("Bienvenido a su farmacia de confianza")
    while True:
        opcion = input("Por favor elige una opción [F] Farmacia, [P] Perfumería, [C] Cosmética, [S] Salir: ").lower()
        
        if opcion in {"f", "farmacia", "p", "perfumeria", "perfumería", "c", "cosmetica", "cosmética", "s", "salir"}:
            return opcion
        
        print("Ingresa una opción válida")

            
def resultado(opcion) -> bool:
    if opcion == "f" or opcion == "farmacia":
        turno_farmacia()
        return True
    elif opcion == "p" or opcion == "perfumeria" or opcion == "perfumería":
        turno_perfumeria()
        return True
    elif opcion == "c" or opcion == "cosmetica" or opcion == "cosmética":
        turno_cosmetiquero()
        return True
    elif opcion == "s" or opcion == "salir":
        print("Saliendo del programa...")
        exit()
    return False
    
def principal():
    system('cls')
    
    while True:
        opcion = menu()
        
        print("Imprimiendo Turno...")
        resultado(opcion)
        
        while True:
            regresar_menu = input("¿Deseas salir del programa [S] Si / [N] No?: ").lower()
            
            if regresar_menu == "s" or regresar_menu == "si":
                print("Saliendo del programa...")
                exit()
            elif regresar_menu == "n" or regresar_menu == "no":
                system('cls')
                break
                
            else:
                print("Ingresa una opción válida: [S] Si / [N] No: ")
            
principal()
