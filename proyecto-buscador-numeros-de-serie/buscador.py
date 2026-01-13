import os
import re
from datetime import date
import time
import math

def retornar_contenido_archivos():
    ruta = os.getcwd() + "\\proyecto-buscador-numeros-de-serie" + "\\Mi_Gran_Directorio"
    
    dict_contenido_archivos = {}
    for carpetas, subcarpetas, archivos in os.walk(ruta):
        
        for archivo in archivos:
            ruta_completa = carpetas + '\\' + archivo
            archivo_abierto = open(ruta_completa, 'r')
            contenido = archivo_abierto.read()
            archivo_abierto.close()
            
            dict_contenido_archivos[archivo] = contenido
            
        
    return dict_contenido_archivos

def encontrar_coincidencias(dict_contenido_archivos):
    patron = r'N\D{3}-\d{5}'
    contador_coincidencias = 0
    dict_coincidencia = {}
    for archivo, contenido in dict_contenido_archivos.items():
        coincidencia = re.search(patron, contenido)
        if coincidencia:
            contador_coincidencias += 1
            dict_coincidencia[archivo] = coincidencia.group()
            
    return contador_coincidencias, dict_coincidencia

def reporte(contador_coincidencias, dict_coincidencia, tiempo_ejecucion):
        print("-"*80)
        fecha_actual = date.today()
        print(f"Fecha de búsqueda: {fecha_actual.strftime("%d/%m/%Y")}\n")
        print("ARCHIVO\t\t NRO. SERIE")
        print(f"{'-'*7}\t\t {'-'*10}")
        
        for key, value in dict_coincidencia.items():
            print(f"{key}\t {value}")
        
        print(f"\nNúmeros encontrados: {contador_coincidencias}")
        print(f"Duración de la búsqueda: {math.ceil(tiempo_ejecucion)}")
        print("-"*80)

inicio = time.time()
dict_contenido_archivos = retornar_contenido_archivos()
contador_coincidencias, dict_coincidencia = encontrar_coincidencias(dict_contenido_archivos)
final = time.time()
tiempo_ejecucion = final - inicio
reporte(contador_coincidencias,dict_coincidencia, tiempo_ejecucion)