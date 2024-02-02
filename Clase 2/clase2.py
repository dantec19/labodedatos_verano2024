#%%

# EJERCICIOS/APUNTES EN CLASE

import clase1

#%%%
"""
Construí una función traductor_geringoso(lista) que, a partir de una lista de 
palabras, devuelva un diccionario geringoso.
Las claves del diccionario deben ser las palabras de la lista y los valores 
deben ser sus traducciones al geringoso.
"""
def traductor_geringoso(lista):
    diccionario_geringoso = dict()
    for palabra in lista:
        diccionario_geringoso[palabra] = clase1.traducir_a_geringoso(palabra)
    return diccionario_geringoso

#%%%
"""
Escribir una función generala_tirar() que simule una tirada de dados para el 
juego de la generala. Es decir, debe devolver una lista aleatoria de 5 valores 
de dados. Por ejemplo [2,3,2,1,6].
"""
import random
def generala_tirar(cant_dados=5):
    return [random.choice(list(range(1,7))) for _ in range(5)]

"""
Agregar al ejercicio generala_tirar() que además imprima en pantalla si salió 
poker, full, generala, escalera o ninguna de las anteriores. Por ejemplo, si 
sale 2,1,1,2,2 debe devolver [2,1,1,2,2] e imprimir en pantalla Full
"""
def es_escalera(dados):
    return set(dados) == {1,2,3,4,5} or set(dados) == {2,3,4,5,6}

def es_poker(dados):
    return dados.count(dados[0]) == 4 or dados.count(dados[1]) == 4

def es_generala(dados):
    return dados.count(dados[0]) == 5

def es_full(dados):
    return not es_poker(dados) and not es_generala(dados) and len(set(dados)) == 2

def generala_tirar_2():
    dados = generala_tirar()
    if es_full(dados):
        texto = "Full"
    elif es_poker(dados):
        texto = "Poker"
    elif es_generala(dados):
        texto = "Generala"
    elif es_escalera(dados):
        texto = "Escalera"
    else:
        texto = "Nada"
    return dados, texto

#%%%
"""
Escribir un programa que recorra las líneas del archivo ‘datame.txt’ e imprima 
solamente las líneas que contienen la palabra ‘estudiante’.
"""
nombre_archivo = 'datame.txt'
with open(nombre_archivo, 'r') as file:
    for linea in file:
        if 'estudiante' in linea:
            print(linea)

#%%%
# SIN utilizar el módulo csv:
"""
Utilizando el archivo cronograma_sugerido, armar una lista de las materias del 
cronograma, llamada “lista_materias”.
"""
def conseguir_listado_materias(nombre_archivo='cronograma_sugerido.csv'):
    with open(nombre_archivo, 'rt') as file:
        lista_materias = list()
        for line in file:
            datos_linea = line.split(',')
            lista_materias.append(datos_linea[1])
    return lista_materias[1:]

"""
Luego, definir una función “cuantas_materias(n)” que, dado un número de 
cuatrimestre (n entre 3 y 8), devuelva la cantidad de materias a cursar en 
ese cuatrimestre.
Por ejemplo: cuantas_materias(5) debe devolver 3
"""
def cuantas_materias(n, nombre_archivo='cronograma_sugerido.csv'):
    with open(nombre_archivo, 'rt') as file:
        res = 0
        for line in file:
            if line[0] == 'C':
                continue
            datos_linea = line.split(',')
            if int(datos_linea[0]) == n:
                res += 1
    return res

#%%%
# UTILIZANDO el módulo csv:
"""
Definir una función materias_cuatrimestre(nombre_archivo, n) que recorra el archivo indicado,
conteniendo información de un cronograma sugerido de cursada, y devuelva una lista de diccionarios con la
información de las materias sugeridas para cursar el n-ésimo cuatrimestre.
"""
#%%
# GUIA DE EJERCICIOS

import pandas as pd
import os

#%%%
"""
1. Definir una función leer_parque(nombre_archivo, parque) que abra el
archivo indicado y devuelva una lista de diccionarios con la información del
parque especificado. La lista debe tener un diccionario por cada árbol del 
parque elegido. Dicho diccionario debe tener los datos correspondientes a un 
árbol (recordar que cada fila del csv corresponde a un árbol).
Sugerencia: la columna que indica el parque se llama ‘espacio_ve’.
Probar la función en el parque ‘GENERAL PAZ’ y debería dar una lista con 690
árboles.
"""

def leer_parque(nombre_archivo='arbolado-en-espacios-verdes.csv', parque):
   df = pd.read_csv(nombre_archivo) 
   re
    
    
    
    
    
    
    
    
    
    
    
    
    
    
