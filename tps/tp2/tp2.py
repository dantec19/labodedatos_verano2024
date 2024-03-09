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
import seaborn as sns
from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV, KFold
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_graphviz
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.neighbors import KNeighborsClassifier
from verImagenesTP2 import ver_imagen_promedio, mediana_pixeles_letra, atributos_random

carpeta = 'dataset/'

df = pd.read_csv(carpeta + 'sign_mnist_train.csv')

#%% EJERCICIO 1

#%%%
letra_C = df[df['label'] == 2]



dicc_alfabeto = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y'}

for label in dicc_alfabeto:
    ver_imagen_promedio(label, df)
#%%%



filas = np.arange(1,785)

labels = [4,11]

plt.figure(figsize=(10, 6))

for label in labels:
    label_to_plot = dicc_alfabeto[label]
    subset_df = df[df['label'] == label]
    plt.plot(filas, np.array(subset_df.iloc[1:,1:].mean()))
    
plt.title(f'Gráfico de línea del promedio de color de píxeles de las letras E y L')
plt.xlabel('Número de pixel')
plt.ylabel('Valor en escala de grises (0-255)')
plt.xticks(np.arange(1, 785, 56))
plt.ylim(0, 260)
    
plt.show()
#%%%

filas = np.arange(1,785)

labels = [4,11]


for label in dicc_alfabeto:
    plt.figure(figsize=(10, 6))

    label_to_plot = dicc_alfabeto[label]
    subset_df = df[df['label'] == label]
    plt.plot(filas, np.array(subset_df.iloc[1:,1:].std()))
    
    plt.title(f'Gráfico de línea del desvío estandar de píxeles de la letra {label_to_plot}')
    plt.xlabel('Número de pixel')
    plt.ylabel('Valor en escala de grises (0-255)')
    plt.xticks(np.arange(1, 785, 56))
    plt.ylim(0, 70)
    
    
    plt.show()
#%%%

labels = [4,12]

plt.figure(figsize=(10, 6))

for label in labels:
    label_to_plot = dicc_alfabeto[label]
    subset_df = df[df['label'] == label]
    plt.plot(filas, np.array(np.array(subset_df.iloc[1:,1:].mean())))
    
plt.title(f'Gráfico de línea del promedio de color de píxeles de las letras E y M')
plt.xlabel('Número de pixel')
plt.ylabel('Valor en escala de grises (0-255)')
plt.xticks(np.arange(1, 785, 56))
plt.ylim(0, 260)
    
plt.show()

#%% EJERCICIO 2

letras_LyA = df[(df['label'] == 0) | (df['label'] == 11)]

letras_LyA.value_counts()
# El 52,43% son L y el 47,57% son A


def resultados_knn(vecinos: list, cant_atributos, graficar_matrices_confusion=False):
    atributos = atributos_random(cant_atributos)
    X = letras_LyA[list(map(lambda a: 'pixel' + str(a), atributos))]
    y = letras_LyA['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    resultados_por_vecinos = {'k':[], 'resultados':[]}
    for k in vecinos:
        
        neigh = KNeighborsClassifier(n_neighbors = k)
        neigh.fit(X_train, y_train)
    
        predicciones = neigh.predict(X_test)
        score = neigh.score(X_test, y_test)
        resultados_por_vecinos['k'].append(k)
        resultados_por_vecinos['resultados'].append(score)
        if graficar_matrices_confusion:
            ax = plt.subplot()
            ax.set_title(f"k: {k}, score = {score}")
            conf_matrix_display = ConfusionMatrixDisplay(confusion_matrix(y_test, predicciones), display_labels=["A", "L"])
            conf_matrix_display.plot(ax=ax)
            
            plt.rcParams["figure.figsize"] = (10, 6)
            plt.show()
    return resultados_por_vecinos



fig, ax = plt.subplots()

vecinos = list(range(1,200))
ax.scatter(
    data=resultados_knn(vecinos, 3), x="k", y="resultados", s=100, label="3 atributos"
)

ax.scatter(
    data=resultados_knn(vecinos, 5), x="k", y="resultados", s=100, label="5 atributos"
)

# Agregamos titulo, etiquetas a los ejes y limita el rango de valores de los ejes
ax.set_title(
    f"Precisión de modelos con diferente cantidad de vecinos y atributos", fontsize="15"
)   

plt.rcParams["figure.figsize"] = (15, 8)
ax.set_xticks(list(range(1,200)))
ax.set_xlabel("k", fontsize="15", fontweight="bold")
ax.set_ylabel("Score", fontsize="15", fontweight="bold")
ax.xaxis.set_tick_params(labelsize=15)
ax.yaxis.set_tick_params(labelsize=15)
ax.set_xlim(0, 200)
ax.set_ylim(0.7, 1)
ax.legend()
    
# para todos los k hasta como 900 tiene 100% de accuracy.
# con 1893 predice que todos son l porque son mas


    
#%% EJERCICIO 3
letras_vocales = df[(df['label'] == 0) | (df['label'] == 4) | (df['label'] == 8) | (df['label'] == 14) | (df['label'] == 20)]

X = letras_vocales.iloc[:,1:]
y = letras_vocales['label']

X_dev, X_eval, y_dev, y_eval = train_test_split(X, y, test_size=0.2, random_state=10)


profundidades = list(range(1,15))
criterios = ['gini', 'entropy']
X_train, X_test, y_train, y_test = train_test_split(X_dev, y_dev, test_size=0.2, random_state=10)


mejores_profundidades = []
for criterio in criterios:
    for profundidad in profundidades:
        arbol = DecisionTreeClassifier(criterion=criterio, max_depth=profundidad, random_state=0)
        arbol.fit(X_train, y_train)
    
        predicciones = arbol.predict(X_test)
        
        score = arbol.score(X_test, y_test)
        
        if len(mejores_profundidades) < 10:
            mejores_profundidades.append((score,profundidad,criterio))
        elif score > min(mejores_profundidades)[0]:
            mejores_profundidades.remove(min(mejores_profundidades))
            mejores_profundidades.append((score,profundidad,criterio))
            
        ax = plt.subplot()
        ax.set_title(f"Criterio: {criterio}, Profundidad: {profundidad}, score={round(score,4)}")
        conf_matrix_display = ConfusionMatrixDisplay(confusion_matrix(y_test, predicciones), display_labels=["A", "E", "I", "O", "U"])
        conf_matrix_display.plot(ax=ax)
        
        plt.rcParams["figure.figsize"] = (10, 6)
        plt.show()
 
mejores_profundidades = sorted(mejores_profundidades, reverse=True)

# entropy 11, gini 11, entropy 13, gini 13, entropy 8, gini 8



def promedio_resultados_kfold(X_train, y_train, criterio, profundidad, k=5):
    kf = KFold(n_splits=k, shuffle=True)
    folds = list(kf.split(X_train, y_train))
    resultados = np.array([])
    
    for train_index, test_index in folds:
        arbol = DecisionTreeClassifier(criterion=criterio, max_depth=profundidad, random_state=0)
        xtrain = X_train.iloc[train_index]
        ytrain = y_train.iloc[train_index]
        xtest = X_train.iloc[test_index]
        ytest = y_train.iloc[test_index]
        
        arbol.fit(xtrain, ytrain)
        
        resultado = arbol.score(xtest, ytest)
        
        resultados = np.append(resultados, arbol.score(xtest, ytest))
        
        if resultado >= max(resultados):
            mejor_xtrain, mejor_ytrain = xtrain, ytrain
    
    return resultados.mean(), criterio, profundidad, mejor_xtrain, mejor_ytrain


mejores_modelos = []
for modelo in mejores_profundidades:
    profundidad = modelo[1]
    criterio = modelo[2]
    mejores_modelos.append(promedio_resultados_kfold(X_train, y_train, criterio, profundidad))



mejores_modelos = sorted(mejores_modelos, reverse=True)
criterio_mejor_modelo = mejores_modelos[0][1]
profundidad_mejor_modelo = mejores_modelos[0][2]
mejor_xtrain = mejores_modelos[0][3]
mejor_ytrain = mejores_modelos[0][4]


arbol = DecisionTreeClassifier(criterion=criterio_mejor_modelo, max_depth=profundidad_mejor_modelo, random_state=0)
arbol.fit(mejor_xtrain, mejor_ytrain)
arbol.score(X_eval, y_eval)




