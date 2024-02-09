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
