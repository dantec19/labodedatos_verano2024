#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Materia: Laboratorio de datos - FCEyN - UBA
Clase  : Clase Visualizacion. Script clase.
Autor  : Pablo Turjanski
Fecha  : 2024-02-05
Descripcion: Graficos de analisis estadistico
"""

# Importamos bibliotecas
import pandas as pd
import numpy as np
from inline_sql import sql, sql_val
from matplotlib import ticker   # Para agregar separador de miles
from matplotlib import rcParams # Para modificar el tipo de letra
import matplotlib.pyplot as plt # Para graficar series multiples
import seaborn as sns

def main():

    # Carpeta donde se encuentran los archivos a utilizar
    carpeta = "archivos-clase/"
    
    # # # # # # # # # # # # # # # # # # # # # # # # 
    # #   ventaCasas
    # # # # # # # # # # # # # # # # # # # # # # # # 

    # Cargamos dataset ventaCasas
    ventaCasas= pd.read_csv(carpeta+"ventaCasas.csv")
    
    # Mostramos las primeras observaciones
    ventaCasas.head()

    # Estadistica Descritiva
    ventaCasas.describe()

    # Genera el grafico de boxplot (grafico por defecto)
    fig, ax = plt.subplots()
    
    ax.boxplot(ventaCasas['PrecioDeVenta'])
    
    # Genera el grafico de boxplot (mejorando la informacion mostrada)    
    fig, ax = plt.subplots()
    
    rcParams['font.family'] = 'sans-serif'           # Modifica el tipo de letra
    rcParams['axes.spines.right']  = False            # Elimina linea derecha   del recuadro
    rcParams['axes.spines.left']   = True             # Agrega  linea izquierda del recuadro
    rcParams['axes.spines.top']    = False            # Elimina linea superior  del recuadro
    rcParams['axes.spines.bottom'] = False            # Elimina linea inferior  del recuadro

    ax.boxplot(ventaCasas['PrecioDeVenta'], showmeans=True)

    # Agrega titulo, etiquetas a los ejes y limita el rango de valores de los ejes
    ax.set_title('Precio de venta de casas')
    ax.set_xticks([])
 
    ax.set_ylabel('Precio de venta ($)')
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("$ {x:,.2f}")); # Agrega separador de decimales y signo $
    ax.set_ylim(0,500)
    
    
    # # # # # # # # # # # # # # # # # # # # # # # # 
    # #   Propinas
    # # # # # # # # # # # # # # # # # # # # # # # # 

    # Cargamos dataset propinas
    propinas= pd.read_csv(carpeta+"tips.csv")
    
    # Mostramos las primeras observaciones
    propinas.head()

    # Estadistica Descritiva
    propinas.describe()

    # Genera el grafico de boxplot 
    fig, ax = plt.subplots()
    
    rcParams['font.family'] = 'sans-serif'           # Modifica el tipo de letra
    rcParams['axes.spines.right']  = False            # Elimina linea derecha   del recuadro
    rcParams['axes.spines.left']   = True             # Agrega  linea izquierda del recuadro
    rcParams['axes.spines.top']    = False            # Elimina linea superior  del recuadro
    rcParams['axes.spines.bottom'] = False            # Elimina linea inferior  del recuadro

    ax.boxplot(propinas['tip'], showmeans=True)

    # Agrega titulo, etiquetas a los ejes y limita el rango de valores de los ejes
    ax.set_xlabel('Propinas')
    ax.set_ylabel('Valor de Propina ($)')
    ax.set_xticks([])
 

    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("$ {x:,.2f}")); # Agrega separador de decimales y signo $
    ax.set_ylim(0,12)



    # # # # # # # # 
    # Genera el grafico de boxplot por sexo
    # # # # # # # # 
    fig, ax = plt.subplots()
    
    rcParams['font.family'] = 'sans-serif'           # Modifica el tipo de letra
    rcParams['axes.spines.right']  = False            # Elimina linea derecha   del recuadro
    rcParams['axes.spines.left']   = True             # Agrega  linea izquierda del recuadro
    rcParams['axes.spines.top']    = False            # Elimina linea superior  del recuadro
    rcParams['axes.spines.bottom'] = False            # Elimina linea inferior  del recuadro

    propinas.boxplot(by=['sex'], column=['tip'], ax=ax, grid=False, showmeans=True)

    # Agrega titulo, etiquetas a los ejes y limita el rango de valores de los ejes
    fig.suptitle('')
    ax.set_title('Propinas')
    ax.set_xlabel('Sexo')
    ax.set_ylabel('Valor de Propina ($)')

    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("$ {x:,.2f}")); # Agrega separador de decimales y signo $
    ax.set_ylim(0,12)
    


    # # # # # # # # 
    # Genera el grafico de boxplot por dia (y agrupado por sexo)
    # # # # # # # # 
    ax = sns.boxplot(x="day", 
                     y="tip", 
                     hue="sex", 
                     data=propinas, 
                     order=['Thur', 'Fri', 'Sat', 'Sun'], 
                     palette={"Female": "orange", "Male": "skyblue" })
    
    
    ax.set_title('Propinas')
    ax.set_xlabel('Día de la Semana')
    ax.set_ylabel('Valor de Propina ($)')
    ax.set_ylim(0,12)
    ax.legend(title="Sexo")
    ax.set_xticklabels(['Jueves','Viernes','Sábado','Domingo'])    
    
    
    
    # # # # # # # # 
    # Genera el grafico de violinplot 
    # # # # # # # # 
    
    
    
    
    ax = sns.violinplot(x ="sex", y ="tip", data = propinas,
                         palette={"Female": "orange", "Male": "skyblue" })
    
    ax.set_title('Propinas')
    ax.set_xlabel('sexo')
    ax.set_ylabel('Porcentaje de Propina (%)')
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("$ {x:,.2f}")); # Agrega separador de decimales y signo $
    ax.set_ylim(0,12)
    ax.set_xticklabels(['Femenino','Masculino'])    
    
    # # # # # # # # 
    # Genera el grafico de boxplot por dia (y agrupado por sexo)
    # # # # # # # # 
    
    porcentaje_tip = sql^"""
                           SELECT *, (tip / total_bill) * 100 AS porcentaje_tip
                           FROM propinas
                         """
    
    ax = sns.boxplot(x="day", 
                     y="porcentaje_tip", 
                     hue="sex", 
                     data=porcentaje_tip, 
                     order=['Thur', 'Fri', 'Sat', 'Sun'], 
                     palette={"Female": "orange", "Male": "skyblue" })
    
    
    ax.set_title('Porcentaje de la propina con respecto al valor de la cuenta')
    ax.set_xlabel('Día de la Semana')
    ax.set_ylabel('porcentaje (%)')
    ax.set_ylim(0,50)
    ax.legend(title="Sexo")
    ax.set_xticklabels(['Jueves','Viernes','Sábado','Domingo'])    
    
