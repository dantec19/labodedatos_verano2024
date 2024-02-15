# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 14:01:10 2024
Materia: Laboratorio de datos - FCEyN - UBA
Clase  : Clase Visualización. Script primeros gráficos.
Autor  : Dante Cocú
Fecha  : 2024-02-15
Descripción: primeros gráficos
@author: dantec19
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import ticker

carpeta = "archivos-clase/"

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
    








