#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 17:06:25 2024

@author: dcocu
"""

import pandas as pd
import numpy as np
from matplotlib import ticker   # Para agregar separador de miles
from matplotlib import rcParams # Para modificar el tipo de letra
import matplotlib.pyplot as plt # Para graficar series multiples
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_graphviz
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from verImagenesTP2 import ver_imagen, promediar_pixeles_letra, mediana_pixeles_letra

carpeta = 'dataset/'

df = pd.read_csv(carpeta + 'sign_mnist_train.csv')

dicc_alfabeto = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 10:'K', 11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X', 24:'Y'}

for label in dicc_alfabeto:
    label_to_plot = dicc_alfabeto[label]
    label_value = label
    # Filter the DataFrame for the specified label
    subset_df = df[df['label'] == label_value]

    # Exclude the 'label' column
    pixels = subset_df.drop('label', axis=1).values.flatten()

    # Number of pixels in a single image (assuming 28x28)
    num_pixels_per_image = 28 * 28

    # Number of images in the subset
    num_images = subset_df.shape[0]

    # Create x-axis values for all pixels in the subset
    x_values = np.tile(np.arange(num_pixels_per_image), num_images)
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(x_values, pixels, s=0.5, c='blue', alpha=0.5)
    plt.title(f'Scatter Plot for Grayscale Values of Label "{label_to_plot}" (Label {label_value})')
    plt.xlabel('Pixel Index within a 28x28 Image')
    plt.ylabel('Grayscale Value (0-255)')
    
    filas = list(range(0,785,28))
    
    plt.xticks(filas)
    
    plt.show()


for label in dicc_alfabeto:
    subset_df = df[df['label'] == label]
    ver_imagen(mediana_pixeles_letra(subset_df))

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

X = letras_LyA.iloc[:,1:]
y = letras_LyA['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


neigh = KNeighborsClassifier(n_neighbors=5)

neigh.fit(X_train, y_train)

predicciones = list(neigh.predict(X_test))

neigh.score(predicciones, y_test)




letras_vocales = df[(df['label'] == 0) | (df['label'] == 4) | (df['label'] == 8) | (df['label'] == 14) | (df['label'] == 20)]

X = letras_vocales.iloc[:,1:]
y = letras_vocales['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

arbol = DecisionTreeClassifier(random_state=0)

arbol.fit(X_train, y_train) #Entrenamiento

arbol.score(X_test, y_test)




