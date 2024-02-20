# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:51:27 2024

@author: dantec19
"""

import pandas as pd
import numpy as np
from inline_sql import sql, sql_val


carpeta = "datasets/"
 
sede_basico = pd.read_csv(carpeta+"sede-basico.csv")    

sede_completo = pd.read_csv(carpeta+"sede-completo.csv", usecols=list(range(0,37)))

sede_secciones = pd.read_csv(carpeta+"sede-secciones.csv")    

pbi_per_capita = pd.read_csv(carpeta+"pbipercapita.csv", header=2)

pbi_per_capita = pbi_per_capita.rename(columns={'Country Code': 'codigo_pais', '2022':'pbi_pc_2022'})

df = sede_completo[['sede_id','redes_sociales']].loc[sede_completo['redes_sociales'].notnull()]

caca = {'sede_id':[], 'url':[]}
for i in df.index:
    sede_id = df['sede_id'][i]
    redes_sede = df['redes_sociales'][i].split('  //  ')[:-1]
    for red in redes_sede:
        caca['sede_id'].append(sede_id)
        caca['url'].append(red)
            
d = pd.DataFrame(caca)

pais = sql^"""
          SELECT DISTINCT s.pais_iso_3, s.region_geografica, s.pais_castellano AS nombre_pais, pbi.pbi_pc_2022
          FROM sede_completo AS s
          INNER JOIN pbi_per_capita AS pbi ON s.pais_iso_3 = pbi.codigo_pais
        """

sede = sql^"""
          SELECT DISTINCT s.pais_iso_3, s.sede_id, secc.tipo_seccion
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
          FROM d
          WHERE red_social IS NOT NULL
        """
        
ejercicioHI = sql^"""
                
             """
             
ejercicioIIaux = sql^"""
                  SELECT DISTINCT p.region_geografica, s.sede_id, p.pbi_pc_2022
                  FROM pais AS p
                  INNER JOIN sede AS s
                  ON p.pais_iso_3 = s.pais_iso_3
                """
             
ejercicioII = sql^"""
                SELECT region_geografica, COUNT(sede_id), AVG(pbi_pc_2022)
                FROM ejercicioIIaux
                GROUP BY region_geografica
             """
             
ejercicioIIIaux = sql^"""
                SELECT p.nombre_pais, r.red_social, COUNT(r.red_social)
                FROM redes AS r
                INNER JOIN sede AS s 
                ON r.sede_id = s.sede_id
                INNER JOIN pais AS p
                ON p.pais_iso_3 = s.pais_iso_3
                GROUP BY p.nombre_pais, r.red_social
             """    
             
ejercicioIII = sql^"""
                SELECT nombre_pais, COUNT(red_social)
                FROM ejercicioIIIaux
                GROUP BY nombre_pais
               """

ejercicioIV = sql^"""
                SELECT p.nombre_pais, s.sede_id, r.red_social, r.url
                FROM redes AS r
                INNER JOIN sede AS s 
                ON r.sede_id = s.sede_id
                INNER JOIN pais AS p
                ON p.pais_iso_3 = s.pais_iso_3
             """
        
        
        
        
        
        
        
        
        
        
        
        
        