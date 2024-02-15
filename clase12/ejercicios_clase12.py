#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 15:42:36 2024

@author: dantec19
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

carpeta = "archivos-guia/"

# Cargamos los datos de las ventas por región
ventasPorRegion = pd.read_csv(carpeta + "ventasPorRegion.csv")

# Genera el grafico de torta (grafico por defecto)
fig, ax = plt.subplots()

ax.pie(data=ventasPorRegion, x='Porcentaje')


# Genera el grafico de barras torta (mejorando la informacion mostrada)
fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'           
plt.rcParams['axes.spines.left']  = False       # Remueve linea derecha  del recuadro
plt.rcParams['font.size'] = 9.0
ax.pie(data=ventasPorRegion, 
       x='Porcentaje', 
       labels='Region',          # Etiquetas
       autopct='%1.2f%%',       # porcentajes
       colors=['red',
               'green',
               'yellow',
               'blue'],
       shadow = True,
       counterclock = True, 
       )
    

