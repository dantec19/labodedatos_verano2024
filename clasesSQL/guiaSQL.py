# Importamos bibliotecas
import pandas as pd
from inline_sql import sql, sql_val

def main():
    
    print(
    """
    OBJETIVO:
    Ejercitar comandos asociados a consultas SQL.
    
    FUENTE DE DATOS:
    Los datos a utilizar corresponden a casos confirmados de Dengue y Zika provenientes del
    Registro del Sistema Nacional de Vigilancia de la Salud 2.0. Ministerio de Salud. Secretaría
    de Promoción de la Salud, Prevención y Control de Riesgos. Subsecretaría de Prevención y
    Control de Enfermedades Comunicables e Inmunoprevenibles. Dirección Nacional de
    Epidemiología y Análisis de la Situación de Salud. Área de Vigilancia.
    
    Fuente. http://datos.salud.gob.ar/dataset/vigilancia-de-dengue-y-zika (años: 2019 y 2020).
    
    Con la intención de disminuir posibles inconsistencias, los datos utilizados en esta guía han
    sufrido un proceso de limpieza previa. La estructura de almacenamiento y algunos datos
    han sido modificados con fines didácticos.
    """
    )
    
    carpeta = "archivos-guia/"
    
    casos = pd.read_csv(carpeta+"casos.csv")    
    departamento = pd.read_csv(carpeta+"departamento.csv")
    grupoetario = pd.read_csv(carpeta+"grupoetario.csv")    
    provincia = pd.read_csv(carpeta+"provincia.csv")    
    tipoevento = pd.read_csv(carpeta+"tipoevento.csv")    


    print()
    print("# =============================================================================")
    print("# EJERCICIO A: Consultas sobre una tabla")
    print("# =============================================================================")
    
    consigna = "a.Listar sólo los nombres de todos los departamentos que hay en la tabla departamento (dejando los registros repetidos)"
    consultaSQL = """
                   SELECT descripcion AS nombre
                   FROM departamento
                  """
    imprimirEjercicio(consigna, [departamento], consultaSQL, sql^consultaSQL)   
    
    
    # -----------
    consigna = "b. Listar sólo los nombres de todos los departamentos que hay en la tabla departamento (eliminando los registros repetidos)."
    consultaSQL = """
                   SELECT DISTINCT descripcion AS nombre
                   FROM departamento
                  """
    imprimirEjercicio(consigna, [departamento], consultaSQL, sql^consultaSQL)   
    
    
    # -----------
    consigna = "c. Listar sólo los códigos de departamento y sus nombres, de todos los departamentos que hay en la tabla departamento."
    consultaSQL = """
                   SELECT DISTINCT id AS codigo_depto, descripcion AS nombre
                   FROM departamento
                  """
    imprimirEjercicio(consigna, [departamento], consultaSQL, sql^consultaSQL)
    
    
    # -----------
    consigna = "d. Listar todas las columnas de la tabla departamento."
    consultaSQL = """
                   SELECT *
                   FROM departamento
                  """
    imprimirEjercicio(consigna, [departamento], consultaSQL, sql^consultaSQL)
    
    
    # -----------
    consigna = "e. Listar los códigos de departamento y nombres de todos los departamentos que hay en la tabla departamento. Utilizar los siguientes alias para las columnas: codigo_depto y nombre_depto, respectivamente."
    consultaSQL = """
                   SELECT id AS codigo_depto, descripcion AS nombre_depto
                   FROM departamento
                  """
    imprimirEjercicio(consigna, [departamento], consultaSQL, sql^consultaSQL)
    
    
    # -----------
    consigna = "f. Listar los registros de la tabla departamento cuyo código de provincia es igual a 54"
    consultaSQL = """
                   SELECT *
                   FROM departamento
                   WHERE id_provincia = 54
                  """
    imprimirEjercicio(consigna, [departamento], consultaSQL, sql^consultaSQL)
    
    
    # -----------
    consigna = "g. Listar los registros de la tabla departamento cuyo código de provincia es igual a 22, 78 u 86."
    consultaSQL = """
                   SELECT *
                   FROM departamento
                   WHERE id_provincia = 22 OR id_provincia = 78 OR id_provincia = 86
                  """
    imprimirEjercicio(consigna, [departamento], consultaSQL, sql^consultaSQL)
    
    
    # -----------
    consigna = "h. Listar los registros de la tabla departamento cuyos códigos de provincia se encuentren entre el 50 y el 59 (ambos valores inclusive)."
    consultaSQL = """
                   SELECT *
                   FROM departamento
                   WHERE id_provincia >= 50 AND id_provincia <= 59
                  """
    imprimirEjercicio(consigna, [departamento], consultaSQL, sql^consultaSQL)
    
    
    print()
    print("# =============================================================================")
    print("# EJERCICIO B: Consultas multitabla (INNER JOIN)")
    print("# =============================================================================")
    
    consigna = "a. Devolver una lista con los código y nombres de departamentos, asociados al nombre de la provincia al que pertenecen."
    consultaSQL = """
                   SELECT d.id, d.descripcion, p.descripcion AS nombre_provincia
                   FROM departamento AS d
                   INNER JOIN provincia AS p
                   ON d.id_provincia=p.id
                  """
    imprimirEjercicio(consigna, [provincia, departamento], consultaSQL, sql^consultaSQL)
    
    
    # -----------
    consigna = "c. Devolver los casos registrados en la provincia de 'Chaco'."
    consultaSQL = """
                   SELECT c.*
                   FROM casos AS c
                   INNER JOIN departamento AS d
                   ON id_depto=d.id
                   INNER JOIN provincia AS p
                   ON d.id_provincia=p.id
                   WHERE p.descripcion = 'Chaco'
                  """
    imprimirEjercicio(consigna, [provincia, departamento, casos], consultaSQL, sql^consultaSQL)
    
    
    # -----------
    consigna = "d. Devolver aquellos casos de la provincia de 'Buenos Aires' cuyo campo cantidad supere los 10 casos."
    consultaSQL = """
                   SELECT c.*
                   FROM casos AS c
                   INNER JOIN departamento AS d
                   ON id_depto=d.id
                   INNER JOIN provincia AS p
                   ON d.id_provincia=p.id
                   WHERE p.descripcion = 'Buenos Aires' AND c.cantidad > 10
                  """
    imprimirEjercicio(consigna, [provincia, departamento, casos], consultaSQL, sql^consultaSQL)
    
    
    print()
    print("# =============================================================================")
    print("# EJERCICIO C: Consultas multitabla (OUTER JOIN)")
    print("# =============================================================================")
    
    consigna = "a. Devolver un listado con los nombres de los departamentos que no tienen ningún caso asociado."
    consultaSQL = """
                   SELECT d.descripcion
                   FROM departamento AS d
                   LEFT OUTER JOIN casos AS c ON d.id = c.id_depto
                   WHERE c.id IS NULL
                  """
    imprimirEjercicio(consigna, [casos, departamento], consultaSQL, sql^consultaSQL)
    
    
    # -----------
    consigna = "b. Devolver un listado con los tipos de evento que no tienen ningún caso asociado."
    consultaSQL = """
                   SELECT t.descripcion
                   FROM tipoevento AS t
                   LEFT OUTER JOIN casos AS c ON t.id = c.id_tipoevento
                   WHERE c.id IS NULL
                  """
    imprimirEjercicio(consigna, [casos, tipoevento], consultaSQL, sql^consultaSQL)
    
    
    print()
    print("# =============================================================================")
    print("# EJERCICIO D: Consultas resumen")
    print("# =============================================================================")
    
    consigna = "a. Calcular la cantidad total de casos que hay en la tabla casos"
    consultaSQL = """
                   SELECT COUNT(*) AS cant_casos
                   FROM casos
                  """
    imprimirEjercicio(consigna, [casos], consultaSQL, sql^consultaSQL)
    
    
    # -----------
    consigna = "b. Calcular la cantidad total de casos que hay en la tabla casos para cada año y cada tipo de caso. Presentar la información de la siguiente manera: descripción del tipo de caso, año y cantidad. Ordenarlo por tipo de caso (ascendente) y año (ascendente)."
    consultaSQL = """
                   SELECT t.descripcion, c.anio, COUNT(*) AS cant_casos
                   FROM casos AS c
                   INNER JOIN tipoevento AS t ON c.id_tipoevento = t.id
                   GROUP BY c.anio, t.descripcion
                   ORDER BY t.descripcion ASC, c.anio ASC
                  """
    imprimirEjercicio(consigna, [casos, tipoevento], consultaSQL, sql^consultaSQL)
    
    
    # -----------
    consigna = "c. Misma consulta que el ítem anterior, pero sólo para el año 2019."
    consultaSQL = """
                   SELECT t.descripcion, c.anio, COUNT(*) AS cant_casos
                   FROM casos AS c
                   INNER JOIN tipoevento AS t ON c.id_tipoevento = t.id
                   WHERE c.anio = 2019
                   GROUP BY c.anio, t.descripcion
                   ORDER BY t.descripcion ASC
                  """
    imprimirEjercicio(consigna, [casos, tipoevento], consultaSQL, sql^consultaSQL)
    
    
    # -----------
    consigna = "d. Calcular la cantidad total de departamentos que hay por provincia. Presentar la información ordenada por código de provincia."
    consultaSQL = """
                   SELECT id_provincia, COUNT(*) AS cant_deptos
                   FROM departamento
                   GROUP BY id_provincia
                   ORDER BY id_provincia
                  """
    imprimirEjercicio(consigna, [departamento], consultaSQL, sql^consultaSQL)
    
    
    # -----------
    consigna = "e. Listar los departamentos con menos cantidad de casos en el año 2019."
    consultaSQL = """
                    SELECT d.descripcion, COUNT(casos) AS cant_casos
                    FROM departamento AS d
                    INNER JOIN casos AS c ON d.id = c.id_depto
                    WHERE c.anio = 2019
                    GROUP BY d.id, d.descripcion
                    HAVING cant_casos = (
                        SELECT MIN(c) FROM (
                            SELECT COUNT(casos) AS c
                            FROM casos
                            WHERE anio = 2019 
                            GROUP BY id_depto
                        )
                    )
                  """
                 
    imprimirEjercicio(consigna, [departamento, casos], consultaSQL, sql^consultaSQL)
    a=sql^consultaSQL
    
    
# =============================================================================
# DEFINICION DE FUNCIÓN DE IMPRESIÓN EN PANTALLA
# =============================================================================
# Imprime en pantalla en un formato ordenado:
    # 1. Consigna
    # 2. Cada dataframe de la lista de dataframes de entrada
    # 3. Query
    # 4. Dataframe de salida
def imprimirEjercicio(consigna, listaDeDataframesDeEntrada, consultaSQL, dataframeResultadoDeConsultaSQL):
    
    print("# -----------------------------------------------------------------------------")
    print("# Consigna: ", consigna)
    print("# -----------------------------------------------------------------------------")
    print()
    for i in range(len(listaDeDataframesDeEntrada)):
        print("# Entrada 0",i,sep='')
        print("# -----------")
        print(listaDeDataframesDeEntrada[i])
        print()
    print("# SQL:")
    print("# ----")
    print(consultaSQL)
    print()
    print("# Salida:")
    print("# -------")
    print(dataframeResultadoDeConsultaSQL)
    print()
    print("# -----------------------------------------------------------------------------")
    print("# -----------------------------------------------------------------------------")
    print()
    print()
    
    
# =============================================================================
# EJECUCIÓN MAIN
# =============================================================================

if __name__ == "__main__":
    main()
