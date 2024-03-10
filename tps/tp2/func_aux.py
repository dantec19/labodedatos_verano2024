import random


def label_a_letra(label):
    """
    Convierte un número de etiqueta a la letra correspondiente en mayúsculas.

    Parametros:
    - label (int): El número de etiqueta a convertir.

    Devuelve:
    - str: La letra correspondiente en mayúsculas.
    """
    return chr(label + 65)


def letra_a_label(letra):
    """
    Convierte una letra en mayúsculas a su número de etiqueta correspondiente.

    Parametros:
    - letra (str): La letra en mayúsculas a convertir.

    Devuelve:
    - int: El número de etiqueta correspondiente.
    """
    return ord(letra) - 65


def atributos_random(k):
    """
    Genera una lista de 'k' atributos aleatorios entre 1 y 784.

    Parametros:
    - k (int): El número de atributos aleatorios a generar.

    Devuelve:
    - list: Una lista de 'k' atributos aleatorios.
    """
    res = []
    for i in range(k):
        random.seed(i)
        res.append(random.randint(1, 784))
    return res


def conseguir_registros_letra(df, letra):
    """
    Obtiene los registros del DataFrame correspondientes a una letra específica.

    Parametros:
    - df (DataFrame): El DataFrame que contiene los datos.
    - letra (str): La letra en mayúsculas para la cual se desean los registros.

    Devuelve:
    - DataFrame: Subconjunto de registros correspondientes a la letra dada.
    """
    return df[df["label"] == letra_a_label(letra)]


def conseguir_desvio_estandar_promedio(df, letra):
    """
    Calcula el desvío estándar promedio de los píxeles para una letra específica.

    Parametros:
    - df (DataFrame): El DataFrame que contiene los datos.
    - letra (str): La letra en mayúsculas para la cual se calcula el desvío estándar promedio.

    Devuelve:
    - float: El desvío estándar promedio de los píxeles para la letra dada.
    """
    registros_letra = conseguir_registros_letra(df, letra)
    std_pixeles = registros_letra.iloc[1:, 1:].std()
    promedio_std_letra = std_pixeles.mean()
    return promedio_std_letra