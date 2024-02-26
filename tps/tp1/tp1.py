# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:51:27 2024

@author: dantec19
"""

#%% PROCESAMIENTO Y LIMPIEZA DE DATOS
#%%% IMPORTS Y CARGA DE DATOS
import pandas as pd
import numpy as np
from inline_sql import sql, sql_val
import matplotlib.pyplot as plt
import seaborn as sns

# Las bases de datos necesarias para el TP las guardamos en la carpeta datasets
carpeta = "datasets/"

# Cargamos los datos de las sedes
sede_basico = pd.read_csv(carpeta + "sede-basico.csv")

sede_completo = pd.read_csv(carpeta + "sede-completo.csv", usecols=list(range(0, 37)))

sede_secciones = pd.read_csv(carpeta + "sede-secciones.csv")

# Cargamos los datos del PBI
pbi_per_capita = pd.read_csv(carpeta + "pbipercapita.csv", header=2)

# Cambiamos los nombres de las columnas que usamos y tienen espacios o números
# para facilitar las consultas de SQL
pbi_per_capita = pbi_per_capita.rename(
    columns={"Country Code": "pais_iso_3", "2022": "pbi_pc_2022"}
)

#%%% LIMPIEZA DE DATOS

# Armamos las bases pais, sede y redes a partir del DER que planteamos
# mediante funciones de Pandas y consultas SQL

pais = sql^"""
           SELECT DISTINCT s.pais_iso_3,
                           s.region_geografica,
                           s.pais_castellano AS nombre_pais,
           FROM   sede_completo AS s 
           """

sede = sql^"""
           SELECT DISTINCT s.pais_iso_3,
                           s.sede_id,
                           secc.sede_desc_castellano AS sede_desc
           FROM   sede_completo AS s
                  LEFT OUTER JOIN sede_secciones AS secc
                               ON s.sede_id = secc.sede_id 
           """
           
pib = sql^"""
           SELECT DISTINCT pbi.pais_iso_3,
                           pbi.pbi_pc_2022
           FROM   pbi_per_capita AS pbi
           """


# La base redes es más difícil de armar, por lo que lo hacemos en varios pasos

# En la base sede_completo, la columna redes_sociales no es un atributo
# atómico, ya que admite como valor una lista de URLs separadas por dos barras,
# por lo tanto creamos una tabla con atributos sede_id y url que pone cada
# URL en una fila distinta

# Conseguimos las sedes con alguna red social
dict_urls = sede_completo[["sede_id", "redes_sociales"]].loc[
    sede_completo["redes_sociales"].notnull()
]

# Creamos un diccionario vacío que después vamos a pasar a DataFrame
red_limpia = {"sede_id": [], "url": []}
for i in dict_urls.index:
    # Conseguimos el id de la sede y armamos una lista con sus redes sociales,
    # tomando "  //  " como separador
    sede_id = dict_urls["sede_id"][i]
    redes_sede = dict_urls["redes_sociales"][i].split("  //  ")[:-1]
    for red in redes_sede:
        # Agregamos tantas columnas como redes que tiene la sede
        red_limpia["sede_id"].append(sede_id)
        red_limpia["url"].append(red)

df_urls = pd.DataFrame(red_limpia)

redes = sql^"""
            SELECT *,
                   CASE
                     WHEN Lower(url) LIKE '%facebook%' THEN 'Facebook'
                     WHEN Lower(url) LIKE '%twitter%' THEN 'Twitter'
                     WHEN Lower(url) LIKE '%youtube%' THEN 'Youtube'
                     WHEN Lower(url) LIKE '%instagram%' THEN 'Instagram'
                     WHEN Lower(url) LIKE '%linkedin%' THEN 'Linkedin'
                     WHEN Lower(url) LIKE '%flickr%' THEN 'Flickr'
                   END AS red_social
            FROM   df_urls
            WHERE  red_social IS NOT NULL 
            """

#%% EJERCICIOS DE CONSULTAS SQL
#%%% EJERCICIO 1
consigna = """
Para cada país informar cantidad de sedes, cantidad de secciones en
promedio que poseen sus sedes y el PBI per cápita del país en 2022. El
orden del reporte debe respetar la cantidad de sedes (de manera
descendente). En caso de empate, ordenar alfabéticamente por nombre de
país.
"""
# Empezamos obteniendo la cantidad de sedes de cada país

# Conseguimos la tabla con las sedes de los paises sin repetir
sedes_de_pais = sql^"""
                    SELECT DISTINCT pib.pais_iso_3, s.sede_id
                    FROM   pib
                    LEFT OUTER JOIN sede AS s ON pib.pais_iso_3 = s.pais_iso_3
                    """

# La cantidad de apariciones de un país en la anterior tabla nos indica cuántas
# sedes tiene este

"""CASE 
    WHEN sp.sede_id IS NULL THEN 0
    ELSE Count(sp.pais_iso_3) 
END AS sedes"""
cuenta_sedes_por_pais = sql^"""
                            SELECT DISTINCT sp.pais_iso_3,
                                            Count(sp.pais_iso_3)       
                            FROM   sedes_de_pais AS sp
                            GROUP  BY sp.pais_iso_3
                            """

# Ahora pasamos a conseguir la cantidad de secciones en promedio que posee cada
# sede

# Empezamos consiguiendo la cantidad de secciones que tiene cada sede
cuenta_secciones = sql^"""
                       SELECT s.pais_iso_3,
                              s.sede_id,
                              Count(sede_id) AS cant_secciones
                       FROM   sede AS s
                       GROUP  BY sede_id,
                                 pais_iso_3 
                       """

# Con la tabla anterior podemos calcular el promedio de secciones que tienen
# las sedes de cada país
promedio_secciones = sql^"""
                        SELECT sec.pais_iso_3,
                               Avg(sec.cant_secciones) AS secciones_promedio
                        FROM   cuenta_secciones AS sec
                        GROUP  BY sec.pais_iso_3 
                        """

# Juntamos el nombre de los paises, la cantidad de sedes, el promedio de
# secciones por sede y el pbi per capita
ejercicioI = sql^"""
                 SELECT DISTINCT Upper(p.nombre_pais) AS nombre_pais,
                                 cs.sedes,
                                 ps.secciones_promedio,
                                 p.pbi_pc_2022
                 FROM   pais AS p
                        INNER JOIN cuenta_sedes_por_pais AS cs
                                ON p.pais_iso_3 = cs.pais_iso_3
                        INNER JOIN promedio_secciones AS ps
                                ON p.pais_iso_3 = ps.pais_iso_3
                 WHERE  p.pbi_pc_2022 IS NOT NULL
                 ORDER  BY cs.sedes DESC,
                           p.nombre_pais ASC 
                 """
# Imprimimos el resultado
print(consigna, ejercicioI)

#%%% EJERCICIO 2
consigna = """
Reportar agrupando por región geográfica: a) la cantidad de países en que
Argentina tiene al menos una sede y b) el promedio del PBI per cápita 2022
de dichos países. Ordenar por el promedio del PBI per Cápita. 
"""

# Obtenemos todos los países que están en la base de sede (es decir que tienen
# alguna sede argentina) con su región geográfica y PBI per Capita
pbi_paises_con_sede = sql^"""
                          SELECT DISTINCT p.region_geografica,
                                          p.pais_iso_3,
                                          p.pbi_pc_2022
                          FROM   pais AS p
                                 INNER JOIN sede AS s
                                         ON p.pais_iso_3 = s.pais_iso_3
                          """

# Conseguimos la cantidad de países con sedes argentinas en cada región
# geográfica y el promedio del PBI Per Capita de estos a partir de la tabla
# anterior
ejercicioII = sql^"""
                  SELECT region_geografica,
                         Count(pais_iso_3) AS paises_con_sedes_arg,
                         Avg(pbi_pc_2022)  AS promedio_pbi_per_capita
                  FROM   pbi_paises_con_sede
                  GROUP  BY region_geografica
                  ORDER  BY promedio_pbi_per_capita DESC 
                  """

# Imprimimos el resultado
print(consigna, ejercicioII)
#%%% EJERCICIO 3
consigna = """
Para saber cuál es la vía de comunicación de las sedes en cada país, nos
hacemos la siguiente pregunta: ¿Cuán variado es, en cada el país, el tipo de
redes sociales que utilizan las sedes? Se espera como respuesta que para
cada país se informe la cantidad de tipos de redes distintas utilizadas. Por
ejemplo, si en Chile utilizan 4 redes de facebook, 5 de instagram y 4 de
twitter, el valor para Chile debería ser 3 (facebook, instagram y twitter).
"""
# Armamos una tabla con valores del nombre del país y los nombres de las
# redes sociales que tienen sus sedes
nombre_redes_pais = sql^"""
                        SELECT DISTINCT p.nombre_pais,
                                        r.red_social
                        FROM   redes AS r
                        INNER JOIN sede AS s
                                ON r.sede_id = s.sede_id
                        INNER JOIN pais AS p
                                ON p.pais_iso_3 = s.pais_iso_3 
                        """

# La cantidad de veces que aparece cada país será la cantidad de redes
# distintas que tiene
ejercicioIII = sql^"""
                   SELECT nombre_pais,
                          Count(nombre_pais) AS redes_distintas
                   FROM   nombre_redes_pais
                   GROUP  BY nombre_pais 
                   """

# Imprimimos el resultado
print(consigna, ejercicioIII)
#%%% EJERCICIO 4
consigna = """
Confeccionar un reporte con la información de redes sociales, donde se
indique para cada caso: el país, la sede, el tipo de red social y url utilizada.
Ordenar de manera ascendente por nombre de país, sede, tipo de red y
finalmente por url.
"""

# El ejercicio consiste únicamente en juntar datos tanto de redes como de país
# y sedes
ejercicioIV = sql^"""
                  SELECT DISTINCT Upper(p.nombre_pais) AS nombre_pais,
                                  s.sede_id,
                                  r.red_social,
                                  r.url
                  FROM   redes AS r
                  INNER JOIN sede AS s
                          ON r.sede_id = s.sede_id
                  INNER JOIN pais AS p
                          ON p.pais_iso_3 = s.pais_iso_3
                  ORDER  BY p.nombre_pais ASC,
                            s.sede_id ASC,
                            r.red_social ASC,
                            r.url ASC 
                  """

# Imprimimos el resultado
print(consigna, ejercicioIV)
#%% EJERCICIOS DE VISUALIZACIÓN DE DATOS
#%%% EJERCICIO 1
consigna = """
(Visualizar la) cantidad de sedes por región geográfica. Mostrarlos ordenados 
de manera decreciente por dicha cantidad.
"""
ax = plt.axes([0, 1, 3, 1])

# Armamos una tabla con la cantidad de sedes argentinas que hay en cada región
sedes_por_region = sql^"""
                       SELECT p.region_geografica,
                              Count(p.region_geografica) AS cant_sedes
                       FROM   pais AS p
                       FULL OUTER JOIN sede AS s
                                    ON p.pais_iso_3 = s.pais_iso_3
                       GROUP  BY p.region_geografica
                       ORDER  BY cant_sedes DESC 
                       """
# Agregamos saltos de linea en los nombres de las regiones para que entren en
# el gráfico
sedes_por_region["region_geografica"] = sedes_por_region["region_geografica"].replace(
    ["ÁFRICA  DEL  NORTE  Y  CERCANO  ORIENTE",
     "EUROPA  CENTRAL  Y  ORIENTAL",
     "AMÉRICA  CENTRAL  Y  CARIBE"],
    
    ["ÁFRICA  DEL  NORTE  Y\nCERCANO  ORIENTE",
     "EUROPA  CENTRAL Y\nORIENTAL",
     "AMÉRICA  CENTRAL Y\nCARIBE"]
)


ax.bar(
    x=sedes_por_region["region_geografica"],
    height=sedes_por_region["cant_sedes"],  # Alto de la barra
    align="center",   # Barra centrada
    color="skyblue",  # Color de la barra
    edgecolor="black" # Color del borde de la barra
)  

# Agregamos titulo, etiquetas a los ejes y limita el rango de valores de los ejes
ax.set_title(
    "Cantidad de sedes argentinas por región geográfica",
    fontsize="20",
    fontweight="bold",
)

ax.set_xlabel("Región Geográfica", fontsize="15", fontweight="bold")
ax.set_ylabel("Cantidad de sedes", fontsize="15", fontweight="bold")

ax.set_ylim(0, 160)

#%%% EJERCICIO 2
consigna = """
(Armar un) boxplot, por cada región geográfica, del PBI per cápita 2022 de los 
países donde Argentina tiene una delegación. Mostrar todos los boxplots en una
misma figura, ordenados por la mediana de cada región.
"""

# Para realizar este ejercicio, nos sirve la base de datos pbi_paises_con_sede, 
# armada en el ejercicio 2 de las consultas SQL

# Agregamos saltos de linea en los nombres de las regiones para que entren en
# el gráfico
pbi_paises_con_sede["region_geografica"] = pbi_paises_con_sede["region_geografica"].replace(
    ["ÁFRICA  DEL  NORTE  Y  CERCANO  ORIENTE",
     "EUROPA  CENTRAL  Y  ORIENTAL",
     "AMÉRICA  CENTRAL  Y  CARIBE",
     "EUROPA  OCCIDENTAL",
     "AMÉRICA  DEL  NORTE",
     "ÁFRICA  SUBSAHARIANA"
     ],
    
    ["ÁFRICA  DEL\nNORTE  Y\nCERCANO  ORIENTE",
     "EUROPA\nCENTRAL Y\nORIENTAL",
     "AMÉRICA  CENTRAL Y\nCARIBE",
     "EUROPA\nOCCIDENTAL",
     "AMÉRICA  DEL\nNORTE",
     "ÁFRICA\nSUBSAHARIANA"]
)

# Armamos la visualización de los boxplots, ordenándolos por valores de la
# mediana de forma decreciente
ax = sns.boxplot(
    x="region_geografica",
    y="pbi_pc_2022",
    data=pbi_paises_con_sede,
    order=[
        "OCEANÍA",
        "AMÉRICA  DEL\nNORTE",
        "EUROPA\nOCCIDENTAL",
        "EUROPA\nCENTRAL Y\nORIENTAL",
        "AMÉRICA  CENTRAL Y\nCARIBE",
        "ASIA",
        "AMÉRICA  DEL  SUR",
        "ÁFRICA  DEL\nNORTE  Y\nCERCANO  ORIENTE",
        "ÁFRICA\nSUBSAHARIANA",
    ],
)

# Cambiamos el tamaño del canvas
sns.set(rc={"figure.figsize": (18.7, 8.27)})

# Agregamos titulo, etiquetas a los ejes y limita el rango de valores de los ejes
ax.set_title(
    "PBI Per Capita de Paises con Sedes Argentinas según Región Geográfica",
    fontsize="20",
    fontweight="bold",
)
ax.set_xlabel("Región Geográfica", fontsize="15", fontweight="bold")
ax.set_ylabel("PBI Per Capita(US$)", fontsize="15", fontweight="bold")
ax.set_ylim(0, 110000)

#%%% EJERCICIO 3
consigna = """
(Visualizar la) relación entre el PBI per cápita de cada país (año 2022 y para todos los
países que se tiene información) y la cantidad de sedes en el exterior que
tiene Argentina en esos países.
"""
fig, ax = plt.subplots()

# Elegimos representarlo con un scatter plot
ax.scatter(
    data=ejercicioI, x="sedes", y="pbi_pc_2022", s=20
)

# Agregamos titulo, etiquetas a los ejes y limita el rango de valores de los ejes
ax.set_title(
    "PBI Per Capita vs Cantidad de Sedes Argentinas", fontsize="20", fontweight="bold"
)
ax.set_xlabel("Cantidad de Sedes Argentinas", fontsize="15", fontweight="bold")
ax.set_ylabel("PBI Per Capita", fontsize="15", fontweight="bold")
ax.set_xlim(0, 12)
ax.set_ylim(0, 110000)