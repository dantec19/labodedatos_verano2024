#%%
# GUIA DE EJERCICIOS

import pandas as pd

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

def leer_parque(parque, nombre_archivo='archivos/arbolado-en-espacios-verdes.csv'):
   df = pd.read_csv(nombre_archivo) 
   arboles_parque = df[df['espacio_ve'] == parque]
   dict_arboles = arboles_parque.to_dict(orient='records')
   
   return dict_arboles

#%%%
"""
2. Escribir una función especies(lista_arboles) que tome una lista de árboles
como la generada en el ejercicio anterior y devuelva el conjunto de especies (la
columna 'nombre_com' del archivo) que figuran en la lista.
"""

def especies(lista_arboles):
    conjunto_especies = set()
    for arbol in lista_arboles:
        especie = arbol['nombre_com']
        conjunto_especies.add(especie)
    
    return conjunto_especies

#%%%
"""
3. Escribir una función contar_ejemplares(lista_arboles) que, dada una
lista como la generada con leer_parque(...), devuelva un diccionario en el
que las especies sean las claves y tengan como valores asociados la cantidad de
ejemplares en esa especie en la lista dada.
Debería verse que en el parque General Paz hay 20 Jacarandás, en el Parque Los
Andes hay 3 Tilos y en Parque Centenario hay 1 Laurel.
"""

def contar_ejemplares(lista_arboles):
    cuenta_ejemplares = dict()
    for arbol in lista_arboles:
        especie = arbol['nombre_com']
        cuenta_ejemplares[especie] = 1 + cuenta_ejemplares.get(especie, 0)
    
    return cuenta_ejemplares

#%%%
"""
4. Escribir una función obtener_alturas(lista_arboles, especie) que,
dada una lista como la generada con leer_parque(...) y una especie de
árbol (un valor de la columna 'nombre_com' del archivo), devuelva una lista con
las alturas (columna 'altura_tot') de los ejemplares de esa especie en la lista.
"""
def obtener_alturas(lista_arboles, especie):
    lista_alturas = list()
    for arbol in lista_arboles:
        especie_actual = arbol['nombre_com']
        if especie_actual == especie:
            altura = arbol['altura_tot']
            lista_alturas.append(altura)
    
    return lista_alturas


muestra = ['GENERAL PAZ','ANDES, LOS','CENTENARIO']
alturas_jacaranda_muestra = pd.DataFrame()

i=0

"""
Usar la función para calcular la altura promedio y altura máxima de los
'Jacarandá' en los tres parques mencionados

for parque in muestra:
    lista_arboles = leer_parque(parque)
    dict_alturas_jacaranda = pd.DataFrame({parque: obtener_alturas(lista_arboles, "Jacarandá")})
    alturas_jacaranda_muestra = pd.concat([alturas_jacaranda_muestra, dict_alturas_jacaranda], axis=1)
    i+=1
alturas_jacaranda_muestra.describe().applymap('{:,.2f}'.format)
"""

#%%%
"""
5. Escribir una función obtener_inclinaciones(lista_arboles, especie)
que, dada una lista como la generada con leer_parque(...) y una especie
de árbol, devuelva una lista con las inclinaciones (columna 'inclinacio') de
los ejemplares de esa especie.
"""
def obtener_inclinaciones(lista_arboles, especie):
    dfparque = pd.DataFrame(lista_arboles)
    dfespecie = dfparque[dfparque['nombre_com'] == especie]
    inclinaciones_especie = dfespecie['inclinacio']
    return inclinaciones_especie

#%%%
"""
6. Combinando la función especies() con obtener_inclinaciones() escribir
una función especimen_mas_inclinado(lista_arboles) que, dada una
lista de árboles devuelva la especie que tiene el ejemplar más inclinado y su
inclinación.
Correrlo para los tres parques mencionados anteriormente. Debería obtenerse,
por ejemplo, que en el Parque Centenario hay un Falso Guayabo inclinado 80
grados.
"""
def especimen_mas_inclinado(lista_arboles):
    conjunto_especies = especies(lista_arboles)
    inclinacion_max = -1
    especie_max = ""
    for especie in conjunto_especies:
        inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        if inclinaciones.max() > inclinacion_max:    
            inclinacion_max = inclinaciones.max()
            especie_max = especie
            
    return especie_max, inclinacion_max

#%%%
"""
7. Volver a combinar las funciones anteriores para escribir la función
especie_promedio_mas_inclinada(lista_arboles) que, dada una lista
de árboles devuelva la especie que en promedio tiene la mayor inclinación y el
promedio calculado.
Resultados. Debería obtenerse, por ejemplo, que los Álamos Plateados del
Parque Los Andes tiene un promedio de inclinación de 25 grados
"""
def especie_promedio_mas_inclinada(lista_arboles):
    conjunto_especies = especies(lista_arboles)
    promedio_inclinacion_max = -1
    especie_max = ""
    for especie in conjunto_especies:
        inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        if inclinaciones.mean() > promedio_inclinacion_max:    
            promedio_inclinacion_max = inclinaciones.mean()
            especie_max = especie
            
    return especie_max, promedio_inclinacion_max
