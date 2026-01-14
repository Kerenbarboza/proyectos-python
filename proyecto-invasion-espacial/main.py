import pygame
import random
import math
from pygame import mixer
import io

# pygame setup - Inicializar
pygame.init()

#Crear pantalla con sus dimensiones (ancho * alto)
pantalla = pygame.display.set_mode((800,600))

#Titulo
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("Fondo.jpg")

#agregar musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(-1)

#crear_jugador
jugador_img = pygame.image.load("cohete.png")
#Variables del jugador
jugador_x = 368
jugador_y = 536
jugador_x_cambio = 0
velocidad = 0.3

#crear enemigo
enemigo_img = []
#Variables del enemigo
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    #crear enemigo 8 veces
    enemigo_img.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(velocidad)
    enemigo_y_cambio.append(30)

#crear bala
bala_img = pygame.image.load("bala.png")
#variables de la bala
bala_x = 0
bala_y = 536
bala_y_cambio = 2 * velocidad
bala_visible = False

def fuente_bytes(fuente):
    #abrir archivo en modo lectura 
    with open(fuente, 'rb') as f:
        ttf_bytes = f.read()
    #crear objeto BytesIO a partir de los bytes del archivo
    return io.BytesIO(ttf_bytes)

#Puntaje
puntaje = 0
fuente_como_bytes = fuente_bytes("FreeSansBold.ttf")
fuente = pygame.font.Font(fuente_como_bytes, 32)
texto_x = 10
texto_y = 10

#Funciones
def jugador(x, y):
    pantalla.blit(jugador_img, (x, y))
    
def enemigo(x,y, ene):
    pantalla.blit(enemigo_img[ene], (x,y))
    
def disparar_bala(x,y):
    global bala_visible
    
    bala_visible = True
    pantalla.blit(bala_img, (x + 16, y + 10))
    
def detectar_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False

def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255,255,255))
    pantalla.blit(texto, (x,y))
    
def texto_final():
    mi_fuente_final = fuente.render("JUEGO TERMINADO", True, (255,255,255))
    pantalla.blit(mi_fuente_final, (60,200))

#Loop del juego
se_ejecuta = True
while se_ejecuta:
    #cambiar color de pantalla       
    # pantalla.fill((205, 144, 228))
    #Cargar imagen de fondo
    pantalla.blit(fondo, (0,0))
    
    for evento in pygame.event.get():
        
        #Cerrar ventana cuando se haga clic en la X
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        
        #Movimiento de cohete
        #Si la tecla esta presionada:    
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -velocidad
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = velocidad
            if evento.key == pygame.K_SPACE:
                mixer.Sound('disparo.mp3').play()
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        #Movimiento de cohete
        #Si la tecla se suelta:    
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
    
    #Modificar ubicación del jugador en caso de presionar una tecla:          
    jugador_x += jugador_x_cambio   
    
    #Mantener jugador dentro de bordes
    if jugador_x <= 0:
        jugador_x = 0
        
    elif jugador_x >= 736:
        jugador_x = 736
        
        
    #Modificar ubicación del enemigo
    for e in range(cantidad_enemigos):
        
        #fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            
            texto_final()
            break
        
        enemigo_x[e] += enemigo_x_cambio[e]
    
    #Mantener enemigo y en caso que toque el borde rebote
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = velocidad
            enemigo_y[e] += enemigo_y_cambio[e]
        
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -velocidad
            enemigo_y[e] += enemigo_y_cambio[e]

        #colision
        colision = detectar_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            mixer.Sound('golpe.mp3').play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0,736)
            enemigo_y[e] = random.randint(50,200)
            
        enemigo(enemigo_x[e], enemigo_y[e], e)
        
    #Movimiento de la bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    #Movimiento bala
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio
        
    #llamada a función   
    jugador(jugador_x, jugador_y)
    
    mostrar_puntaje(texto_x, texto_y)
    
    #actualizar pantalla
    pygame.display.update()
    
    
            
    
            