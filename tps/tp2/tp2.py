#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 17:06:25 2024

@author: dcocu
"""
#%% IMPORTS
import pandas as pd
import numpy as np
from matplotlib import ticker   # Para agregar separador de miles
from matplotlib import rcParams # Para modificar el tipo de letra
import matplotlib.pyplot as plt # Para graficar series multiples
from sklearn.model_selection import cross_val_score, train_test_split, KFold
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_graphviz
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from verImagenesTP2 import ver_imagen, promediar_pixeles_letra, mediana_pixeles_letra

carpeta = 'dataset/'

df = pd.read_csv(carpeta + 'sign_mnist_train.csv')

#%% EJERCICIO 1

dicc_alfabeto = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y'}

filas = np.arange(1,785)

labels = [4,11]

plt.figure(figsize=(10, 6))

for label in labels:
    label_to_plot = dicc_alfabeto[label]
    subset_df = df[df['label'] == label]
    plt.plot(filas, np.array(promediar_pixeles_letra(subset_df)))
    
plt.title(f'Gráfico de línea del promedio de color de píxeles de las letras E y L')
plt.xlabel('Número de pixel')
plt.ylabel('Valor en escala de grises (0-255)')
plt.xticks(np.arange(1, 785, 56))
plt.ylim(0, 260)
    
plt.show()



labels = [4,12]

plt.figure(figsize=(10, 6))

for label in labels:
    label_to_plot = dicc_alfabeto[label]
    subset_df = df[df['label'] == label]
    plt.plot(filas, np.array(promediar_pixeles_letra(subset_df)))
    
plt.title(f'Gráfico de línea del promedio de color de píxeles de las letras E y M')
plt.xlabel('Número de pixel')
plt.ylabel('Valor en escala de grises (0-255)')
plt.xticks(np.arange(1, 785, 56))
plt.ylim(0, 260)
    
plt.show()


letras_LyA = df[(df['label'] == 0) | (df['label'] == 11)]

letras_LyA.value_counts()
# El 52,43% son L y el 47,57% son A


#%% EJERCICIO 2

X = letras_LyA.iloc[:,1:]
y = letras_LyA['label']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


hiperparametros = list(range(900,1500))

for k in hiperparametros:
    neigh = KNeighborsClassifier(n_neighbors = 1875)
    neigh.fit(X_train, y_train)

    predicciones = neigh.predict(X_test)

    print(k, confusion_matrix(y_test, predicciones))
    
# para todos los k hasta como 900 tiene 100% de accuracy.
# con 1893 predice que todos son l porque son mas


    
#%% EJERCICIO 3
letras_vocales = df[(df['label'] == 0) | (df['label'] == 4) | (df['label'] == 8) | (df['label'] == 14) | (df['label'] == 20)]

X = letras_vocales.iloc[:,1:]
y = letras_vocales['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)


hiperparametros = list(range(1,15))

profundidad_mejor_accuracy = 0 
score_max = 0
for depth in hiperparametros:
    arbol = DecisionTreeClassifier(max_depth=depth, random_state=0)
    arbol.fit(X_train, y_train)

    predicciones = arbol.predict(X_test)
    
    score = arbol.score(X_test, y_test)
    if score > score_max:
        profundidad_mejor_accuracy = depth
        score_max = score

    print(f"Profundidad: {depth}")
    print(confusion_matrix(y_test, predicciones))
    print(score)
    
print(profundidad_mejor_accuracy)
 
kf = KFold(k=5, shuffle=True)
list(kf.split(X, y))




