#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Materia: Laboratorio de datos - FCEyN - UBA
Clase  : Clase Visualizacion. Script clase.
Autor  : Dante Cocú
Fecha  : 2024-02-05
Descripcion: Graficos de distribucion
"""

# Importamos bibliotecas
import pandas as pd
import numpy as np
from matplotlib import ticker   # Para agregar separador de miles
from matplotlib import rcParams # Para modificar el tipo de letra
import matplotlib.pyplot as plt # Para graficar series multiples

carpeta = 'datasets/'

# Cargamos los datos del zoo
zoo = pd.read_csv(carpeta + "zoo.csv")

# Gráfico por defecto de asistencia al zoo en función al mes
plt.bar(data=zoo, x="Mes", height="Asistencia")

# Mejoramos el formato
fig, ax = plt.subplots()

plt.rcParams["font.family"] = "sans-serif"

ax.bar(data=zoo, x="Mes", height="Asistencia")
ax.set_title("Asistencia mensual al zoo")
ax.set_xlabel("Mes", fontsize="medium")
ax.set_ylabel("Cantidad de asistentes", fontsize="medium")
ax.set_ylim(0,25000)
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.0f}"))

# -----------
# Cargamos los datos de snow
snow = pd.read_csv(carpeta + "snow.csv")

# Generar el gráfico que relaciona el promedio de nevadas en función del
# promedio de temperaturas minimas (gráfico por defecto)
plt.scatter(data=snow, x="PromedioTempMinima", y="PromedioNevadas")

# Mejoramos el formato
fig, ax = plt.subplots()

ax.scatter(data=snow, 
            x="PromedioTempMinima", 
            y="PromedioNevadas",
            s=8) # Tamaño del punto, s es size

ax.set_title("Promedio de Nevadas vs. Promedio de Temp. Mínimas")
ax.set_xlabel("Promedio de Temperaturas Mínimas (ºC)", fontsize="medium")
ax.set_ylabel("Promedio de Nevadas (Pulgadas)", fontsize="medium")
ax.set_xlim(0,26)
ax.set_ylim(-2,120)

# -----------
# Cargamos los datos de airport
airport = pd.read_csv(carpeta + "airport.csv")

# Generar el gráfico que relaciona el tiempo de espera, el costo de
# estacionamiento y los Boardings por año (gráfico por defecto)
plt.scatter(data=airport,
            x="WaitTime",
            y="ParkingCost",
            s="AnnualEnplanements")

# Mejoramos el formato
fig, ax = plt.subplots()

plt.rcParams["font.family"] = "sans-serif"

tamanoBurbuja = 30

ax.scatter(data=airport,
            x="WaitTime",
            y="ParkingCost",
            s=airport["AnnualEnplanements"]*tamanoBurbuja)

ax.set_title("Relación entre 3 variables")
ax.set_xlabel("Tiempo de espera TSA (min)", fontsize="medium")
ax.set_ylabel("Tarifa de estacionamiento más económica ($)", fontsize="medium")
ax.set_xlim(0,12)
ax.set_ylim(0,25)

ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:,.2f}"))
ax.yaxis.set_major_formatter(ticker.StrMethodFormatter("${x:,.2f}"))

# -----------
# Cargamos los datos de cheetah
cheetah = pd.read_csv(carpeta + "cheetah.csv")

# Generamos el gráfico por defecto
plt.scatter(data=cheetah,
            x="Anio",
            y="Ventas")

# Mejoramos el formato
fig, ax = plt.subplots()

plt.rcParams["font.family"] = "sans-serif"

ax.plot("Anio", "Ventas", data=cheetah, marker="o")

ax.set_title("Ventas de la Compañia Cheetah Sports")
ax.set_xlabel("Año", fontsize="medium")
ax.set_ylabel("Ventas (millones de $)", fontsize="medium")
ax.set_xlim(0,12)
ax.set_ylim(0,250)

# -----------
# Cargamos los datos de cheetahRegion
cheetahRegion = pd.read_csv(carpeta + "cheetahRegion.csv")

# Gráfico por defecto
fig, ax = plt.subplots()

ax.plot("Anio", "regionEste", data=cheetahRegion)
ax.plot("Anio", "regionOeste", data=cheetahRegion)

# Mejoramos el formato
fig, ax = plt.subplots()

plt.rcParams["font.family"] = "sans-serif"


ax.plot("Anio",
        "regionEste",
        data=cheetahRegion,
        marker=".",
        linestyle="-",
        linewidth=0.7,
        label="Región Este")

ax.plot("Anio",
        "regionOeste",
        data=cheetahRegion,
        marker=".",
        linestyle="-",
        linewidth=0.7,
        label="Región Oeste")


ax.set_title("Ventas de la Compañia Cheetah Sports según Región")
ax.set_xlabel("Año", fontsize="medium")
ax.set_ylabel("Ventas (millones de $)", fontsize="medium")
ax.set_xlim(0,12)
ax.set_ylim(0,140)

ax.legend() # Muestra la leyenda

# -----------
cheetah= pd.read_csv(carpeta+"cheetah.csv")    

# Genera el grafico de barras de las ventas mensuales (grafico por defecto)
fig, ax = plt.subplots()

ax.bar(data=cheetah, x='Anio', height='Ventas')


# Genera el grafico de barras de las ventas mensuales (mejorando la informacion mostrada)
fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'           
plt.rcParams['axes.spines.left']  = False # Remueve linea derecha  del recuadro

ax.bar(data=cheetah, x='Anio', height='Ventas')
 
ax.set_title('Ventas de la compañía Cheetah Sports')
ax.set_xlabel('Año', fontsize='medium')                       
ax.set_ylabel('Ventas (millones de $)', fontsize='medium')    
ax.set_xlim(0, 11)
ax.set_ylim(0, 250)

ax.set_xticks(range(1,11,1)) # Muestra todos los ticks del eje x
ax.set_yticks([]) # Remueve los ticks del eje y
ax.bar_label(ax.containers[0], fontsize=8) # Agrega la etiqueta a cada barra


# -----------
# Cargamos dataset CheetahRegion
cheetahRegion= pd.read_csv(carpeta+"cheetahRegion.csv")    


# Genera el grafico de barras de ambas series temporales (grafico por defecto)
fig, ax = plt.subplots()

ax = cheetahRegion.plot(x='Anio', y=['regionEste', 'regionOeste'], kind='bar')


# Genera el grafico de barras de ambas series temporales (mejorando la informacion mostrada)
fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'           
plt.rcParams['axes.spines.left']  = True # Incorpora linea derecha del recuadro

ax = cheetahRegion.plot(x='Anio', 
                        y=['regionEste', 'regionOeste'], 
                        kind='bar',
                        label=['Region Este', 'Region Oeste']) # Agrega etiquetas a la serie

ax.set_title('Ventas de la compañía Cheetah Sports según región')
ax.set_xlabel('Año')
ax.set_ylabel('Ventas (millones de $)')
ax.set_xlim(-1,10)
ax.set_ylim(0,140)

# -----------
# Cargamos dataset votacionGeneral
votacionGeneral= pd.read_csv(carpeta+"votacionGeneral.csv")    

# Genera el grafico de torta (grafico por defecto)
fig, ax = plt.subplots()

ax.pie(data=votacionGeneral, x='Porcentaje')


# Genera el grafico de barras torta (mejorando la informacion mostrada)
fig, ax = plt.subplots()

plt.rcParams['font.family'] = 'sans-serif'           
plt.rcParams['axes.spines.left']  = False       # Remueve linea derecha  del recuadro
plt.rcParams['font.size'] = 9.0
ax.pie(data=votacionGeneral, 
       x='Porcentaje', 
       labels='Alias',          # Etiquetas
       autopct='%1.2f%%',       # porcentajes
       colors=['dodgerblue',
               'purple',
               'gold',
               'slateblue',
               'orangered'],
       shadow = True,
       counterclock = True, 
       explode = (0.1,0,0,0,0)
       )


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
    

# ARCHIVO DADO EN CLASE

# # # # # # # # # # # # # # # # # # # # # # # # 
# #   Gaseosas
# # # # # # # # # # # # # # # # # # # # # # # # 

# Cargamos dataset gaseosas
gaseosas= pd.read_csv(carpeta+"gaseosas.csv")

# Mostramos las primeras observaciones
gaseosas.head()

# Tabla de frecuencias
gaseosas['Compras_gaseosas'].value_counts()    

# Genera el grafico de frecuencias (grafico por defecto)
gaseosas['Compras_gaseosas'].value_counts().plot.bar()

# Genera el grafico de frecuencias (mejorando la informacion mostrada)
fig, ax = plt.subplots()

rcParams['font.family'] = 'sans-serif'           # Modifica el tipo de letra
rcParams['axes.spines.right'] = False            # Elimina linea derecha  del recuadro
rcParams['axes.spines.left']  = False            # Elimina linea derecha  del recuadro
rcParams['axes.spines.top']   = False            # Elimina linea superior del recuadro


ax = gaseosas['Compras_gaseosas'].value_counts().plot.bar()


# Agrega titulo, etiquetas a los ejes y limita el rango de valores de los ejes
ax.set_title('Frecuencia Venta de Gaseosas')
ax.set_yticks([])                                  # Remueve los ticks del eje y
ax.bar_label(ax.containers[0], fontsize=8)         # Agrega la etiqueta a cada barra
ax.tick_params(axis='x', labelrotation=0)          # Rota las etiquetas del eje x para que las muestre horizontales


########### Frecuencias relativas

# Tabla de frecuencias relativas
gaseosas['Compras_gaseosas'].value_counts(normalize=True)


# Genera el grafico de frecuencias relativas (mejorando la informacion mostrada)
fig, ax = plt.subplots()

rcParams['font.family'] = 'sans-serif'           # Modifica el tipo de letra
rcParams['axes.spines.right'] = False            # Elimina linea derecha  del recuadro
rcParams['axes.spines.left']  = False            # Elimina linea derecha  del recuadro
rcParams['axes.spines.top']   = False            # Elimina linea superior del recuadro


ax = gaseosas['Compras_gaseosas'].value_counts(normalize=True).plot.bar()


# Agrega titulo, etiquetas a los ejes y limita el rango de valores de los ejes
ax.set_title('Frecuencia Relativa de Venta de Gaseosas')
ax.set_yticks([])                                  # Remueve los ticks del eje y
ax.bar_label(ax.containers[0], fontsize=8)         # Agrega la etiqueta a cada barra
ax.tick_params(axis='x', labelrotation=0)          # Rota las etiquetas del eje x para que las muestre horizontales
# En formato porcentual
# ax.set_title('Frecuencia Porcentual de Venta de Gaseosas')
# ax.bar_label(ax.containers[0], fontsize=8, fmt='{:.2%}') # Agrega la etiqueta a cada barra en formato de porcentaje



# # # # # # # # # # # # # # # # # # # # # # # # 
# #   Age at Death
# # # # # # # # # # # # # # # # # # # # # # # # 
# Cargamos dataset 
ageAtDeath= pd.read_csv(carpeta+"ageAtDeath.csv")

# Mostramos las primeras observaciones
ageAtDeath.head()

# Tabla de frecuencias
ageAtDeath['AgeAtDeath'].sort_values().value_counts(sort=False)    

# Genera el grafico de frecuencias como con las variables categoricas (grafico por defecto)
ageAtDeath['AgeAtDeath'].sort_values().value_counts(sort=False).plot.bar()

# Genera el grafico de frecuencias (mejorando la informacion mostrada)
fig, ax = plt.subplots()

rcParams['font.family'] = 'sans-serif'           # Modifica el tipo de letra
rcParams['axes.spines.right'] = False            # Elimina linea derecha  del recuadro
rcParams['axes.spines.left']  = True             # Agrega  linea derecha  del recuadro
rcParams['axes.spines.top']   = False            # Elimina linea superior del recuadro


# Calculamos datos necesarios para generar las barras
# bins ...
width = 7                                                              # Cada esta cantidad de anios
# width = 14                                                           # Cada esta cantidad de anios
# width = 28                                                           # Cada esta cantidad de anios
# width = 56                                                           # Cada esta cantidad de anios
bins = np.arange(1,114, width)                                         # Desde 1 a 114 (inclusive) cada width anios
# Contamos cuantos de los datos caen en cada uno de los bins
counts, bins = np.histogram(ageAtDeath['AgeAtDeath'], bins=bins)       # Hace el histograma (por bin)
# Fijamos la ubicacion de cada bin
center = (bins[:-1] + bins[1:]) / 2                                    # Calcula el centro de cada barra

ax.bar(x=center,            # Ubicacion en el eje x de cada bin
       height=counts,       # Alto de la barra
       width=width,         # Ancho de la barra
       align='center',      # Barra centrada
       color='skyblue',     # Color de la barra
       edgecolor='black')   # Color del borde de la barra

# Agrega titulo, etiquetas a los ejes y limita el rango de valores de los ejes    
ax.set_title('Distribución de edades al momento de muerte')
ax.set_xlabel('Edad al momento de muerte (años)')
ax.set_ylabel('Cantidad de personas')
ax.set_ylim(0,160)
# ax.set_ylim(0,250)
# ax.set_ylim(0,400)
# ax.set_ylim(0,650)

# En eje x agrega etiquetas a las barras a modo de rango
bin_edges = [max(0, i-1) for i in bins]              # Define los limites de los bins

labels =  [f'({int(edge)},{int(bin_edges[i+1])}]' 
              for i, edge in enumerate(bin_edges[:-1])] # Genera el string de los labels del estilo (v1, v2]

ax.set_xticks(bin_edges[:-1])                        # Ubica los ticks del eje x
ax.set_xticklabels(labels, rotation=45, fontsize=12) # Asigna labels a los ticks del eje x
ax.tick_params(bottom = False)                       # Remueve los ticks del eje x



# # # # # # # # # # # # # # # # # # # # # # # # 
# #   Age at Death Two
# # # # # # # # # # # # # # # # # # # # # # # # 
# Cargamos dataset 
ageAtDeathTwo= pd.read_csv(carpeta+"ageAtDeathTwo.csv")

# Mostramos las primeras observaciones
ageAtDeathTwo.head()

# Armamos dos subsets: Male y Female
obsFemale=ageAtDeathTwo[ageAtDeathTwo['Sex']=='Female']['AgeAtDeath']
obsMale  =ageAtDeathTwo[ageAtDeathTwo['Sex']=='Male'  ]['AgeAtDeath']


fig, ax = plt.subplots()

# Calculamos datos necesarios para generar las barras
# bins ...
width = 7                                                              # Cada esta cantidad de anios
bins = np.arange(1,114, width)                                         # Desde 1 a 113 (inclusive) cada width anios
# Contamos cuantos de los datos caen en cada uno de los bins
countsFemale, bins = np.histogram(obsFemale, bins=bins)     # Hace el histograma (por bin)
countsMale  , bins = np.histogram(obsMale  , bins=bins)     # Hace el histograma (por bin)
# Si queremos graficar la frecuencia en vez de la cantidad, la calculamos
freqFemale = countsFemale / float(countsFemale.sum())
freqMale   = countsMale   / float(countsMale.sum()  )

# Fijamos la ubicacion de cada bin
center = (bins[:-1] + bins[1:]) / 2                         # Calcula el centro de cada barra

# Graficamos Female
ax.bar(x=center-width*0.2,        # Ubicacion en el eje x de cada bin
       height=countsFemale, # Alto de la barra
       width=width*.4,         # Ancho de la barra
       align='center',      # Barra centrada
       color='orange',     # Color de la barra
       edgecolor='black')   # Color del borde de la barra

# Graficamos Male
ax.bar(x=center+width*0.2,        # Ubicacion en el eje x de cada bin
       height=countsMale,   # Alto de la barra
       width=width*.4,      # Ancho de la barra
       align='center',      # Barra centrada
       color='skyblue',     # Color de la barra
       edgecolor='black')   # Color del borde de la barra

# Agrega titulo, etiquetas a los ejes y limita el rango de valores de los ejes    
ax.set_title('Distribución de edades al momento de muerte')
ax.set_xlabel('Edad al momento de muerte (años)')
ax.set_ylabel('Cantidad de personas')
ax.set_ylim(0,100)

# En eje x agrega etiquetas a las barras a modo de rango
bin_edges = [max(0, i-1) for i in bins]              # Define los limites de los bins

labels =  [f'({int(edge)},{int(bin_edges[i+1])}]' 
              for i, edge in enumerate(bin_edges[:-1])] # Genera el string de los labels del estilo (v1, v2]

ax.set_xticks(bin_edges[:-1])                        # Ubica los ticks del eje x
ax.set_xticklabels(labels, rotation=45, fontsize=12) # Asigna labels a los ticks del eje x
ax.tick_params(bottom = False)                       # Remueve los ticks del eje x

#Agrega leyenda
ax.legend(['Femenino', 'Masculino'], loc='upper left')

# - - - - - - - - - - - - - - - - - 
# Graficamos la frecuencia relativa
# - - - - - - - - - - - - - - - - - 
fig, ax = plt.subplots()


# Graficamos Female
ax.bar(x=center-width*0.2,        # Ubicacion en el eje x de cada bin
       height=freqFemale, # Alto de la barra
       width=width*.4,         # Ancho de la barra
       align='center',      # Barra centrada
       color='orange',     # Color de la barra
       edgecolor='black')   # Color del borde de la barra

# Graficamos Male
ax.bar(x=center+width*0.2,        # Ubicacion en el eje x de cada bin
       height=freqMale,   # Alto de la barra
       width=width*.4,      # Ancho de la barra
       align='center',      # Barra centrada
       color='skyblue',     # Color de la barra
       edgecolor='black')   # Color del borde de la barra

# Agrega titulo, etiquetas a los ejes y limita el rango de valores de los ejes    
ax.set_title('Distribución de edades al momento de muerte')
ax.set_xlabel('Edad al momento de muerte (años)')
ax.set_ylabel('Frecuencia Relativa de Cantidad de personas')
ax.set_ylim(0,0.3)

# En eje x agrega etiquetas a las barras a modo de rango
bin_edges = [max(0, i-1) for i in bins]              # Define los limites de los bins

labels =  [f'({int(edge)},{int(bin_edges[i+1])}]' 
              for i, edge in enumerate(bin_edges[:-1])] # Genera el string de los labels del estilo (v1, v2]

ax.set_xticks(bin_edges[:-1])                        # Ubica los ticks del eje x
ax.set_xticklabels(labels, rotation=45, fontsize=12) # Asigna labels a los ticks del eje x
ax.tick_params(bottom = False)                       # Remueve los ticks del eje x

#Agrega leyenda
ax.legend(['Femenino', 'Masculino'], loc='upper left')


# - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Graficamos la frecuencia relativa en forma de lineas
# - - - - - - - - - - - - - - - - - - - - - - - - - - - 

fig, ax = plt.subplots()

# Graficamos con lineas
ax.plot(center, freqFemale, marker='.', linestyle='-', color='orange')
ax.plot(center, freqMale  , marker='.', linestyle='-', color='skyblue')

# Agrega titulo, etiquetas a los ejes y limita el rango de valores de los ejes    
ax.set_title('Distribución de edades al momento de muerte')
ax.set_xlabel('Edad al momento de muerte (años)')
ax.set_ylabel('Frecuencia Relativa de Cantidad de personas')
ax.set_ylim(0,0.3)

# En eje x agrega etiquetas a las barras a modo de rango
bin_edges = [max(0, i-1) for i in bins]              # Define los limites de los bins

labels =  [f'({int(edge)},{int(bin_edges[i+1])}]' 
              for i, edge in enumerate(bin_edges[:-1])] # Genera el string de los labels del estilo (v1, v2]

ax.set_xticks(bin_edges[:-1])                        # Ubica los ticks del eje x
ax.set_xticklabels(labels, rotation=45, fontsize=12) # Asigna labels a los ticks del eje x
ax.tick_params(bottom = False)                       # Remueve los ticks del eje x

#Agrega leyenda
ax.legend(['Femenino', 'Masculino'], loc='upper left')