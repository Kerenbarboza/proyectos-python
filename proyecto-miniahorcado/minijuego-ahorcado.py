#########EL AHORCADO ##################
import random

def palabra_aleatoria(lista_palabras):
    cadena_aleatoria = random.choice(lista_palabras)
    lista_palabra_aleatoria = list(cadena_aleatoria)
    palitos = list(len(lista_palabra_aleatoria) * "-")
    return cadena_aleatoria, palitos, lista_palabra_aleatoria

def pedir_letra():
    while True:
        try:
            letra_usuario = input("Ingresa una letra: ").lower()
            if len(letra_usuario) != 1 or not letra_usuario.isalpha():
                raise ValueError("Entrada no válida. Ingresa solo una letra (a-z).")
            return letra_usuario
        except ValueError as e:
            print(e)
    
    
        
def validacion_letra(lista_palabra_aleatoria, palitos):
    intentos = 0
    while intentos < 6:
        letra_usuario = pedir_letra()
        
        print(f"Ingresaste la letra {letra_usuario}")
        
        bandera = False
        for indice, valor in enumerate(lista_palabra_aleatoria):
            if valor == letra_usuario:
                palitos[indice] = letra_usuario
                bandera = True
        
        if bandera == True:
             print(f"¡Enhorabuena! Así es como vas {palitos}")
        else:
            intentos += 1
            print(f"¡Fallaste en el intento {intentos}! Sigue intentandolo")
            
        if palitos == lista_palabra_aleatoria:
            print(f"Felicidades, ganaste el juego. La palabra era {"".join(lista_palabra_aleatoria)}")
            break
    
    else:        
        print(f"Te quedaste sin intentos. La palabra era {"".join(lista_palabra_aleatoria)}")
              
        
    
lista_palabras = [
    "relámpago", "horizonte", "mermelada", "susurro", "cristal", "albahaca",
    "neblina", "zorro", "ráfaga", "enciclopedia", "candelabro", "espiral",
    "trueno", "luminaria", "mosaico", "torbellino", "cuaderno", "aurora",
    "fragancia", "relicario"
]

# ------
cadena_aleatoria, palitos, lista_palabra_aleatoria = palabra_aleatoria(lista_palabras)
validacion_letra(lista_palabra_aleatoria, palitos)



