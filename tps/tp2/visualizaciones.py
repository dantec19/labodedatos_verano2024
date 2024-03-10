import numpy as np
import matplotlib.pyplot as plt
from entrenamiento_modelos import resultados_knn
from func_aux import conseguir_registros_letra


def ver_imagen_caracteristica(df, letra, funcion="media"):
    """
    Muestra una imagen característica de una letra dada en base a una función específica.
    
    Parametros:
    - df (DataFrame): DataFrame que contiene los datos.
    - letra (str): La letra para la cual se desea visualizar la imagen.
    - funcion (str, opcional): La función utilizada para calcular la característica (por defecto es "media").
    
    Devuelve:
    None
    """
    registros_letra = conseguir_registros_letra(df, letra)
    if funcion == "media":
        letra_mapeada = registros_letra.iloc[1:, 1:].mean()
    elif funcion == "desvio_estandar":
        letra_mapeada = registros_letra.iloc[1:, 1:].std()
    elif funcion == "mediana":
        letra_mapeada = registros_letra.iloc[1:, 1:].median()

    else:
        raise ValueError("Parámetro 'funcion' equivocado")

    pixeles = np.array(letra_mapeada)
    pixeles.reshape(28, 28)
    plt.matshow(pixeles.reshape(28, 28), cmap="gray")


def comparar_promedio_pixeles(df, letras):
    """
    Compara el promedio de color de píxeles de diferentes letras y visualiza un gráfico de líneas.

    Parametros:
    - df (DataFrame): DataFrame que contiene los datos.
    - letras (list): Lista de letras para comparar.

    Devuelve:
    None
    """

    plt.figure(figsize=(10, 6))

    for letra in letras:
        registros_letra = conseguir_registros_letra(df, letra)
        plt.plot(np.arange(1, 785), np.array(registros_letra.iloc[1:, 1:].mean()))

    str_letras = ", ".join(letra for letra in letras)

    plt.title(
        f"Gráfico de línea del promedio de color de píxeles de las letras {str_letras}"
    )
    plt.xlabel("Número de pixel")
    plt.ylabel("Valor en escala de grises (0-255)")
    plt.xticks(np.arange(1, 785, 56))
    plt.ylim(0, 260)


def graficar_resultados_knn(
    df, lista_cant_vecinos, cant_atributos, ax, matriz_confusion=False
):
    """
    Grafica los resultados del algoritmo KNN para diferentes cantidades de vecinos.

    Parametros:
    - df (DataFrame): DataFrame que contiene los datos.
    - lista_cant_vecinos (list): Lista de cantidades de vecinos a probar.
    - cant_atributos (int): Número de atributos utilizados.
    - ax (Axes): Objeto de ejes de Matplotlib para la visualización.
    - matriz_confusion (bool, opcional): Indica si se debe mostrar la matriz de confusión (por defecto es False).

    Devuelve:
    None
    """
    resultados_por_vecinos = {"k": [], "resultados": []}
    for cant_vecinos in lista_cant_vecinos:
        score = resultados_knn(df, cant_vecinos, cant_atributos, matriz_confusion)
        resultados_por_vecinos["k"].append(cant_vecinos)
        resultados_por_vecinos["resultados"].append(score)

    ax.scatter(
        data=resultados_por_vecinos,
        x="k",
        y="resultados",
        s=100,
        label=f"{cant_atributos} atributos",
    )


def comparar_modelos_knn(
    df, lista_cant_vecinos, lista_cant_atributos, matrices_confusion=False
):
    """
    Compara la precisión de modelos KNN con diferentes cantidades de vecinos y atributos, y visualiza los resultados.

    Parameters:
    - df (DataFrame): DataFrame que contiene los datos.
    - lista_cant_vecinos (list): Lista de cantidades de vecinos a probar.
    - lista_cant_atributos (list): Lista de cantidades de atributos a probar.
    - matrices_confusion (bool, opcional): Indica si se deben mostrar las matrices de confusión (por defecto es False).

    Returns:
    None
    """
    fig, ax = plt.subplots()
    for cant_atributos in lista_cant_atributos:
        graficar_resultados_knn(
            df, lista_cant_vecinos, cant_atributos, ax, matrices_confusion
        )

    ax.set_title(
        "Precisión de modelos con diferente cantidad de vecinos y atributos",
        fontsize="15",
    )

    plt.rcParams["figure.figsize"] = (15, 8)
    ax.set_xticks(list(range(1, 15)))
    ax.set_xlabel("k", fontsize="15", fontweight="bold")
    ax.set_ylabel("Score", fontsize="15", fontweight="bold")
    ax.xaxis.set_tick_params(labelsize=15)
    ax.yaxis.set_tick_params(labelsize=15)
    ax.set_xlim(0, 15)
    ax.set_ylim(0.6, 1)
    ax.legend()
    plt.show()