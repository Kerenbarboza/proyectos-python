#Este programa es un administrador de recetas que permite al usuario leer, crear y eliminar recetas 
# y categorías dentro de una estructura de directorios, 
# mostrando un menú interactivo que se repite hasta que el usuario decida salir.

from pathlib import Path
from os import system
import os

print(f"¡Bievenido al recetario!")
def ruta_acceso ():
    base = os.getcwd()
    ruta_carpetas = Path(base, "proyecto_recetario", "recetas")
    
    lista_recetas = []
    for indice, receta in enumerate(Path(ruta_carpetas).glob('**/*.txt'), start=1):
        lista_recetas.append(receta.stem)
    
    return ruta_carpetas, lista_recetas

def opciones(ruta_carpetas, lista_recetas):
    print(f'''Recuerda que las recetas se encuentra en la ruta {ruta_carpetas}
Además, hay un total de {len(lista_recetas)} recetas listas para ser aplicadas.
''')

    input("Presiona cualquier tecla para iniciar:")    
    system('cls')
    
    while True:
        print('''Elige una opción (del 1 al 6):
                            
        1) Leer receta
        2) Crear receta
        3) Crear categoría
        4) Eliminar receta
        5) Eliminar categoría
        6) Finalizar programa
        ''')
        
        opcion = input("¿Qué opción eliges? (del 1 al 6): ")
        system('cls')
        
        if opcion in {"1", "2", "3", "4", "5", "6"}:
            return int(opcion)
        else:
            print("Elige una opción válida. Del 1 al 6")
        
def elegir_categoria(ruta_carpetas):    
    print("Lista de categorías\n")
    while True:
        
        #Lista de categorías
        lista_categorias = []
        for indice, categoria in enumerate(ruta_carpetas.iterdir(), start=1): #iterdir permite revisar qué hay adentro
            lista_categorias.append(categoria.name.lower())
            print(indice, categoria.name)
        
        categoria_elegida = input(f"¿Que categoría eliges? Ej. Carnes: ").lower()
        
        if categoria_elegida in lista_categorias:
            return categoria_elegida
        
        else: 
            print(f"Elige una opción válida: \n")

def elegir_receta(ruta_carpetas, categoria_elegida):
        print(f"Lista de recetas dentro de {categoria_elegida}\n")
        
        nombres_recetas = []
        for indice, receta in enumerate(Path(ruta_carpetas, categoria_elegida).glob('*.txt'), start=1):
            nombres_recetas.append(receta.stem.lower())
            print(indice, receta.stem)
            
        while True:
            nombre_receta = input("¿Que receta desea leer?. Ej. Entrecot al Malbec: ").lower()
            
            if nombre_receta in nombres_recetas:
                return nombre_receta
            
            else:
                print("La receta no existe. Intenta de nuevo")
    
def leer_receta(ruta_carpetas, categoria_elegida, nombre_receta):
    archivo = Path(ruta_carpetas,categoria_elegida,nombre_receta + '.txt')
    print(f"Abriendo receta {nombre_receta}... \n")
    
    abrir_receta = open(archivo, 'r')
    return abrir_receta.read() #Retornar receta

def crear_receta(categoria, ruta_carpetas):
    print(f"A continuación crearás una nueva receta dentro de la categoria {categoria}")
    nombre_nueva_receta = input("Por favor ingresa el nombre de la nueva receta: ")
    
    ruta_nueva_receta = Path(ruta_carpetas, categoria, nombre_nueva_receta + '.txt')
    
    if not ruta_nueva_receta.exists():
        nueva_receta = open(ruta_nueva_receta, 'w')
        nueva_receta.write(input(f"Ingrese las instrucciones de la receta {nombre_nueva_receta}: "))
        nueva_receta.close()
    else: 
        print("La reseta ya existe")
        return
    
def crear_categoria(ruta_carpetas):
    print("A continuación crearás una nueva categoría")
    while True:
        nombre_nueva_categoria = input("Ingresa el nombre de la nueva categoría: ").capitalize()
        
        ruta_nueva_categoria = Path(ruta_carpetas, nombre_nueva_categoria)
        if not ruta_nueva_categoria.exists():
            os.makedirs(ruta_nueva_categoria)
            print(f"Se ha creado la nueva categoría {nombre_nueva_categoria}")
            break
        
        else:
            print(f"La categoria {nombre_nueva_categoria} ya existe")
        
def eliminar_receta(ruta_carpetas, categoria):
    print("A continuación eliminarás una receta")
    nombre_receta_eliminar = input("Ingresa el nombre de la receta a eliminar: ")
    
    ruta_receta_eliminar = Path(ruta_carpetas, categoria, nombre_receta_eliminar + '.txt')
    
    if not ruta_receta_eliminar.exists():
        print("La receta no existe")
        
    else:
        os.remove(ruta_receta_eliminar)
        print("La receta ha sido eliminada con éxito")

def eliminar_categoria(ruta_carpetas):
    print("A continuación eliminaras una categoría")
    nombre_categoria_eliminar = input("Ingresa el nombre de la categoría a eliminar: ").capitalize()
    
    ruta_categoria_eliminar = Path(ruta_carpetas, nombre_categoria_eliminar)
    
    if not ruta_categoria_eliminar.exists():
        print("La categoría no existe. Intente de nuevo")
        
    else: 
        os.rmdir(ruta_categoria_eliminar)
        print(f"La categoría {nombre_categoria_eliminar} ha sido eliminada con éxito")
      
def resultado_opcion_elegida(opcion_elegida, ruta_carpetas):
    if opcion_elegida == 1:
        categoria = elegir_categoria(ruta_carpetas)
        receta = elegir_receta(ruta_carpetas, categoria)
        print(leer_receta(ruta_carpetas, categoria, receta))
    
    elif opcion_elegida == 2:
        categoria = elegir_categoria(ruta_carpetas)
        crear_receta(categoria, ruta_carpetas)
    
    elif opcion_elegida == 3:
        crear_categoria(ruta_carpetas)
        
    elif opcion_elegida == 4:
        categoria = elegir_categoria(ruta_carpetas)
        eliminar_receta(ruta_carpetas, categoria)
        
    elif opcion_elegida == 5:
        eliminar_categoria(ruta_carpetas)
        
    else:
        print("Finalizando programa...")
        
ruta_carpetas, lista_recetas = ruta_acceso()
opcion_elegida = opciones(ruta_carpetas, lista_recetas)
resultado_opcion_elegida(opcion_elegida, ruta_carpetas)


    