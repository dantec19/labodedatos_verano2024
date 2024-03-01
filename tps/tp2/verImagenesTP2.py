#!/usr/bin/env python
# coding: utf-8

# ## Visualizar imagenes 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

carpeta = 'dataset/'

def ver_imagen(registro):
    pixeles = np.array(registro)
    pixeles.reshape(28, 28)
    plt.matshow(pixeles.reshape(28, 28), cmap = "gray")
    
def promediar_pixeles_letra(registros):
    """
    los registros tienen que ser de la misma letra
    """
    return registros.iloc[1:,1:].mean()


def mediana_pixeles_letra(registros):
    """
    los registros tienen que ser de la misma letra
    """
    return registros.median()