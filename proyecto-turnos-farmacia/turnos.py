def decorador_turnos(funcion):
    def wrapped():
        print("Su turno es:")
        print(funcion())
        print("Aguarde su turno")
    return wrapped

def generador_turnos(prefijo):
    contador = 1
    while True:
        yield f"{prefijo}-{contador}"
        contador += 1
        
generador_turno_farmacia = generador_turnos("F")
generador_turno_cosmetiquero = generador_turnos("C")
generador_turno_perfumeria = generador_turnos("P")

@decorador_turnos
def turno_farmacia():
    return next(generador_turno_farmacia)

@decorador_turnos
def turno_perfumeria():
    return next(generador_turno_perfumeria)

@decorador_turnos
def turno_cosmetiquero():
    return next(generador_turno_cosmetiquero)
