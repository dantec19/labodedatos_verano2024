# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:51:27 2024

@author: dantec19
"""

#%%%
import pandas as pd
import numpy as np
from inline_sql import sql, sql_val


carpeta = "datasets/"

sede_basico = pd.read_csv(carpeta+"sede-basico.csv")    

sede_completo = pd.read_csv(carpeta+"sede-completo.csv", usecols=list(range(0,37)))

sede_secciones = pd.read_csv(carpeta+"sede-secciones.csv")    

pbi_per_capita = pd.read_csv(carpeta+"pbipercapita.csv", header=2)

pbi_per_capita = pbi_per_capita.rename(columns={'Country Code': 'codigo_pais', '2022':'pbi_pc_2022'})

#%%%
df = sede_completo[['sede_id','redes_sociales']].loc[sede_completo['redes_sociales'].notnull()]

red_limpia = {'sede_id':[], 'url':[]}
for i in df.index:
 sede_id = df['sede_id'][i]
 redes_sede = df['redes_sociales'][i].split('  //  ')[:-1]
 for red in redes_sede:
     red_limpia['sede_id'].append(sede_id)
     red_limpia['url'].append(red)
         
df_red = pd.DataFrame(red_limpia)


pais = sql^"""
       SELECT DISTINCT s.pais_iso_3, s.region_geografica, s.pais_castellano AS nombre_pais, pbi.pbi_pc_2022
       FROM sede_completo AS s
       INNER JOIN pbi_per_capita AS pbi ON s.pais_iso_3 = pbi.codigo_pais
       WHERE pbi.pbi_pc_2022 IS NOT null
     """

sede = sql^"""
       SELECT DISTINCT s.pais_iso_3, s.sede_id, secc.sede_desc_castellano AS sede_desc
       FROM sede_completo AS s
       INNER JOIN sede_secciones AS secc ON s.sede_id = secc.sede_id
     """
     
redes = sql^"""
       SELECT *, 
       CASE 
         WHEN LOWER(url) LIKE '%facebook%'
           THEN 'Facebook'
         WHEN LOWER(url) LIKE '%twitter%'
           THEN 'Twitter'
         WHEN LOWER(url) LIKE '%youtube%'
           THEN 'Youtube'
         WHEN LOWER(url) LIKE '%instagram%'
           THEN 'Instagram'
         WHEN LOWER(url) LIKE '%linkedin%'
           THEN 'Linkedin'
         WHEN LOWER(url) LIKE '%flickr%'
           THEN 'Flickr'
       END AS red_social
       FROM df_red
       WHERE red_social IS NOT NULL
     """

#%%%

sedes_de_pais = sql^"""
                   SELECT DISTINCT s.pais_iso_3, s.sede_id
                   FROM sede AS s
                 """

cuenta_sedes_por_pais = sql^"""
                           SELECT DISTINCT sp.pais_iso_3, COUNT(sp.pais_iso_3) AS sedes
                           FROM sedes_de_pais AS sp
                           GROUP BY sp.pais_iso_3
                         """
       
cuenta_secciones = sql^"""
                       SELECT s.pais_iso_3, s.sede_id, COUNT(sede_id) AS cant_sedes
                       FROM sede AS s
                       GROUP BY sede_id, pais_iso_3
                    """
promedio_secciones = sql^"""
                        SELECT sec.pais_iso_3, AVG(sec.cant_sedes) AS secciones_promedio 
                        FROM cuenta_secciones AS sec
                        GROUP BY sec.pais_iso_3
                      """

ejercicioHI = sql^"""
              SELECT DISTINCT p.nombre_pais, cs.sedes, ps.secciones_promedio, p.pbi_pc_2022
              FROM pais AS p
              INNER JOIN cuenta_sedes_por_pais AS cs
              ON p.pais_iso_3 = cs.pais_iso_3
              INNER JOIN promedio_secciones AS ps
              ON p.pais_iso_3 = ps.pais_iso_3
          """
#%%%
ejercicioIIaux = sql^"""
               SELECT DISTINCT p.region_geografica, p.pais_iso_3, p.pbi_pc_2022
               FROM pais AS p
               INNER JOIN sede AS s
               ON p.pais_iso_3 = s.pais_iso_3
             """

ejercicioII = sql^"""
             SELECT region_geografica, COUNT(pais_iso_3) AS paises_con_sedes_arg, AVG(pbi_pc_2022) AS promedio_pbi_per_capita
             FROM ejercicioIIaux
             GROUP BY region_geografica
          """
#%%%    
ejercicioIIIaux = sql^"""
             SELECT DISTINCT p.nombre_pais, r.red_social
             FROM redes AS r
             INNER JOIN sede AS s 
             ON r.sede_id = s.sede_id
             INNER JOIN pais AS p
             ON p.pais_iso_3 = s.pais_iso_3
          """    
          
ejercicioIII = sql^"""
             SELECT nombre_pais, COUNT(nombre_pais) AS redes_distintas
             FROM ejercicioIIIaux
             GROUP BY nombre_pais
            """
#%%%
ejercicioIV = sql^"""
             SELECT p.nombre_pais, s.sede_id, r.red_social, r.url
             FROM redes AS r
             INNER JOIN sede AS s 
             ON r.sede_id = s.sede_id
             INNER JOIN pais AS p
             ON p.pais_iso_3 = s.pais_iso_3
          """
#%%%  
