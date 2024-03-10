#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 17:06:25 2024

autores: Dante Cocú, Solana Navarro, Tomás Uriel Said
tema: Trabajo Práctico 02. Clasificación y validación cruzada
fecha de entrega: 10 de marzo de 2024 
"""

#%% IMPORTS

# Importación de bibliotecas y módulos necesarios
import pandas as pd
from sklearn.model_selection import train_test_split

# Importación de funciones específicas desde módulos personalizados
from visualizaciones import (
    ver_imagen_caracteristica,
    comparar_promedio_pixeles,
    comparar_modelos_knn,
)
from func_aux import label_a_letra, letra_a_label, conseguir_desvio_estandar_promedio
from entrenamiento_modelos import (
    resultados_knn,
    obtener_mejores_hiperparametros,
    evaluar_mejores_hiperparametros,
)

# Carpeta que contiene el dataset
carpeta = "dataset/"

sign_mnist = pd.read_csv(carpeta + "sign_mnist_train.csv")

# Lista de etiquetas únicas ordenadas
labels = sorted(sign_mnist["label"].unique())

#%% EJERCICIO 1
#%%% Item a
letra_C = sign_mnist[sign_mnist["label"] == letra_a_label("C")]

# Generamos las imagenes correspondientes a las medias, los desvíos estandar y las medianas de los pixeles
for label in labels:
    ver_imagen_caracteristica(sign_mnist, label_a_letra(label), funcion="media")
    ver_imagen_caracteristica(
        sign_mnist, label_a_letra(label), funcion="desvio_estandar"
    )
    ver_imagen_caracteristica(sign_mnist, label_a_letra(label), funcion="mediana")

#%%% Item b
# Graficamos el valor promedio de cada pixel para las letras E y L y después para E y M
comparar_promedio_pixeles(sign_mnist, ["E", "L"])
comparar_promedio_pixeles(sign_mnist, ["E", "M"])

#%%% Item c
# Conseguimos el valor promedio del desvío estandar de los píxeles para la C y la Q
conseguir_desvio_estandar_promedio(sign_mnist, "C")
conseguir_desvio_estandar_promedio(sign_mnist, "Q")


#%% EJERCICIO 2
#%%% Item a
# Generamos un DataFrame que contiene los valores de píxeles de las letras L y A
letras_LyA = sign_mnist[
    (sign_mnist["label"] == letra_a_label("A"))
    | (sign_mnist["label"] == letra_a_label("L"))
]

#%%% Item b
# Contamos la cantidad total de letras L y A
letras_LyA["label"].value_counts()

#%%% Items c, d y e
# Resultados de KNN y comparación de modelos con diferente cantidad de vecinos y atributos
k = list(range(1, 15))

lista_cant_atributos = [2, 3, 5, 6]

resultados_knn(letras_LyA, 3, 3, matriz_confusion=True)

comparar_modelos_knn(letras_LyA, k, lista_cant_atributos, matrices_confusion=False)


#%% EJERCICIO 3
#%%% Item a
# Generamos de un DataFrame con las letras vocales (A, E, I, O, U)
letras_vocales = sign_mnist[
    (sign_mnist["label"] == letra_a_label("A"))
    | (sign_mnist["label"] == letra_a_label("E"))
    | (sign_mnist["label"] == letra_a_label("I"))
    | (sign_mnist["label"] == letra_a_label("O"))
    | (sign_mnist["label"] == letra_a_label("U"))
]

X = letras_vocales.iloc[:, 1:]
y = letras_vocales["label"]

# Dividimos el conjunto de datos en desarrollo (X_dev, y_dev) y evaluación (X_eval, y_eval)
X_dev, X_eval, y_dev, y_eval = train_test_split(X, y, test_size=0.2, random_state=15)

#%%% Items b y c
# Buscamos de los mejores hiperparámetros para un árbol de decisión con GridSearch y evaluamos su desempeño
hyper_params = {
    "criterion": ["gini", "entropy"],
    "max_depth": [3, 5, 7, 9, 10, 11, 12, 13, 14],
}

mejores_parametros = obtener_mejores_hiperparametros(
    hyper_params, X_dev, y_dev, ver_detalles=True
)

evaluar_mejores_hiperparametros(
    mejores_parametros, X_dev, X_eval, y_dev, y_eval, matriz_confusion=True
)