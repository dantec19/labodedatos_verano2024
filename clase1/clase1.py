#%%
# EJERCICIOS EN CLASE

#%%%
"""
Escribir un programa que decida si una palabra de longitud exactamente 5 es
palíndromo. Ej. “NADAN” es palíndromo. “JUJUY” no lo es.
"""
def es_palindromo(palabra):
    return palabra[:] == palabra[::-1]

#%%%
"""
Escribir un programa que imprima en pantalla los números enteros entre 0 y 213 
que sean divisibles por 13.
"""
def imprimir_divisibles_por_13(limite=213):
    n = 13
    while n < limite:
        print(n)
        n += 13

#%%%
"""
Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 
'pi', 'po', o 'pu' según corresponda luego de cada vocal.
"""
def traducir_a_geringoso(cadena):
    capadepenapa = ""
    vocales = {'a','e','i','o','u'}
    for c in range(len(cadena)):
        capadepenapa += cadena[c]
        if cadena[c].lower() in vocales:
            capadepenapa += 'p' + cadena[c].lower()
            
    return capadepenapa

#%%%
"""
Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que 
toca el piso salta 3/5 de la altura desde la que cayó. Escribí un programa que 
imprima una tabla mostrando las alturas que alcanza en cada uno de sus primeros
diez rebotes.
"""
def altura_de_rebotes(altura_inicial, rebotes=10):
    for r in range(1,11):
        print(r, round(altura_inicial,4))
        altura_inicial *= 3/5

#%%%
"""
Definir una función maximo(a,b) que tome dos parámetros numéricos y devuelva el
máximo
"""
def maximo(a, b):
    return a if a>=b else b

#%%%
"""
Definir una función tachar_pares(lista) que tome una lista de números y 
devuelva una similar pero donde los números pares estén reemplazados por ‘x’
"""
def tachar_pares(lista):
    return ['x' if i % 2 == 0 else i for i in range(len(lista))]

#%%

# GUÍA DE EJERCICIOS DE LA CLASE 1

#%%%
"""
1. Una mañana ponés un billete en la vereda al lado del obelisco porteño. A 
partir de ahí, cada día vas y duplicás la cantidad de billetes, apilándolos 
prolijamente. ¿Cuánto tiempo pasa antes de que la pila de billetes sea más alta
que el obelisco? Datos: espesor del billete: 0.11 mm, altura obelisco: 67.5 m.
"""
def calcular_tiempo_apilamiento(espesor_billete=0.11, altura=67.5):
    # espesor_billete en mm, altura en m
    dias = 0
    altura_acumulada = espesor_billete
    while altura_acumulada < altura:
        dias += 1 
        altura_acumulada *= 2
    
    return dias

#%%%

"""
2. Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que
toca el piso salta 3/5 de la altura desde la que cayó. Escribí un programa
rebotes.py que imprima una tabla mostrando las alturas que alcanza en cada uno
de sus primeros diez rebotes.
"""
# Hecho en clase, lo copio acá
def altura_de_rebotes(altura_inicial, rebotes=10):
    for r in range(1,11):
        print(r, round(altura_inicial,4))
        altura_inicial *= 3/5

#%%%
"""
3. Queremos hacer un traductor que cambie las palabras masculinas de una frase
por su versión neutra. Como primera aproximación, completá el siguiente código
para reemplazar todas las letras 'o' que figuren en el último o anteúltimo
caracter de cada palabra por una 'e'.
Por ejemplo 'todos somos programadores' pasaría a ser 'todes somes
programadores'.
"""
def traducir_a_neutro(frase):
    traduccion = ""
    for palabra in frase.split(" "):
        if len(palabra) > 1:
            traduccion += palabra[:-2]
            if palabra[-2] == "o":
                traduccion += "e"
            else:
                traduccion += palabra[-2]
            
        if palabra[-1] == "o":
            traduccion += "e"
        else:
            traduccion += palabra[-1]
        
        traduccion += " "
    
    return traduccion[:-1]

#%%%

"""
4. Definir una función es_par(n) que devuelva True si el número es par y False
en caso contrario.
"""
def es_par(n):
    return n % 2 == 0

#%%%

"""
5. Definir una función dos_pertenece(lista) que tome una lista de enteros y
devuelva True si la lista tiene al 2 y False en caso contrario.
"""
def dos_pertenece(lista):
    return 2 in lista

#%%%
"""
6. Definir una función pertenece(lista, elem) que tome una lista y un elemento,
y devuelva True si la lista tiene al elemento dado y False en caso contrario.
"""
def pertenece(lista, elem):
    return elem in lista

#%%%

"""
7. Definir una función mas_larga(lista1, lista2) que tome dos listas y
devuelva la más larga.
"""
def mas_larga(lista1, lista2):
    return lista1 if len(lista1) >= len(lista2) else lista2

#%%%
"""
8. Definir una función cant_e que tome una lista de caracteres y devuelva la
cantidad de letras ‘e’ que tiene la misma.
"""
def cant_e(s):
    res = 0
    for c in s:
        if c == 'e':
            res += 1
            
    return res

#%%%
"""
9. Definir una función sumar_unos que tome una lista de enteros, les sume 1 a
todos sus elementos, y devuelva la misma lista, pero modificada.
"""
def sumar_unos(lista):
    return list(map(lambda n: n+1, lista))

#%%%
"""
10. Definir la función mezclar(cadena1, cadena2) que tome dos strings y
devuelva el resultado de intercalar elemento a elemento. Por ejemplo: si
intercalamos Pepe con Jose daría PJeopsee. En el caso de Pepe con Josefa daría
PJeopseefa.
"""
def mezclar(cadena1, cadena2):
    res = ""
    i = 0
    while i < len(cadena1) or i < len(cadena2):
        if i >= len(cadena1):
            res += cadena2[i]
        elif i >= len(cadena2):
            res += cadena1[i]
        else:
            res += cadena1[i] + cadena2[i]
        i+=1
    
    return res                          