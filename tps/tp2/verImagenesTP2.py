#!/usr/bin/env python
# coding: utf-8

# ## Visualizar imagenes 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

carpeta = 'dataset/'

def ver_imagen_promedio(label_letra: int, df):
    registros_letra = df[df['label'] == label_letra]
    letra_promediada = registros_letra.iloc[1:,1:].mean()
    pixeles = np.array(letra_promediada)
    pixeles.reshape(28, 28)
    plt.matshow(pixeles.reshape(28, 28), cmap = "gray")
    
def mediana_pixeles_letra(registros):
    return registros.median()



def atributos_random(k):  
    res = []
    for i in range(k):
        random.seed(i)
        res.append(random.randint(1, 784))
    return res